import os
import datetime
import zipfile
from typing import List
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from app.models.state import State
from app.models.city import City
from app.models.neighborhood import Neighborhood
from app.models.address import Address
from app.models.global_variable import get_global_variable_value
from app.models.global_variable import update_global_variable_value
from utils.commom_utils import str_to_datetime


class Command(BaseCommand):
    class VerbosityLevels:
        errors_only = 0
        imported_rows = 1
        created_objects = 2

    help = 'Load a list of addresses from a CSV file in format "City;Address;Neighborhood;UF;Zip"'

    states_cache: List[dict] = []
    cities_cache: List[dict] = []
    neighborhood_cache: List[dict] = []

    neighborhood_queryset = Neighborhood.objects.all().select_related('city', 'city__state')
    city_queryset = City.objects.all().select_related('state')
    address_queryset = Address.objects.all().select_related('neighborhood',
                                                            'neighborhood__city',
                                                            'neighborhood__city__state')

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self._input_file_path = ''
        self._csv_files_path = []
        self._current_csv_file_path = ''
        self._verbosity_level = 0
        self.addresses_datetime = None
        self.is_zip_file = False

    def add_arguments(self, parser):
        parser.add_argument('input_file_path', type=str)
        parser.add_argument('--verbositylevel', type=int, default=0)

    @transaction.atomic
    def handle(self, *args, **options):
        print("Started: ", datetime.datetime.now())
        self._input_file_path = options.get('input_file_path')
        self._verbosity_level = options.get('verbositylevel', 0)
        if not self.should_import():
            print('The last importation date is bigger than the addresses date. It was already imported')
        else:
            self._load_states_cache()
            self._load_cities_cache()
            self._load_neighborhood_cache()
            self.load()
            update_global_variable_value('LAST_ADDRESSES_UPDATE', self.addresses_datetime)
        print("Finished: ", datetime.datetime.now())

    def should_import(self):
        self.get_addresses_date()
        last_addresses_update_date = get_global_variable_value('LAST_ADDRESSES_UPDATE')
        return last_addresses_update_date is None or last_addresses_update_date < self.addresses_datetime

    def read_all_csv_lines(self) -> List[str]:
        if not os.path.exists(self._current_csv_file_path):
            raise CommandError('File "{}" not found'.format(self._current_csv_file_path))

        with open(self._current_csv_file_path, 'r', encoding='utf8') as csv_file:
            lines = csv_file.readlines()
            csv_file.close()
            return lines

    def get_addresses_date(self):
        input_file_dir = os.path.dirname(self._input_file_path)
        addresses_date_file = os.path.join(input_file_dir, 'addresses_date.txt')
        if not os.path.exists(addresses_date_file):
            raise CommandError('Addresses date file "{}" does not exists'.format(addresses_date_file))

        with open(addresses_date_file, 'r') as file:
            date_str = file.readline()
            self.addresses_datetime = str_to_datetime(date_str)

    def _load_states_cache(self):
        self.states_cache.clear()
        [self.add_state_in_cache(state) for state in State.objects.all()]

    def _load_cities_cache(self):
        self.cities_cache.clear()
        [self.add_city_in_cache(city) for city in self.city_queryset]

    def _load_neighborhood_cache(self):
        self.neighborhood_cache.clear()
        [self.add_neighborhood_in_cache(neighborhood) for neighborhood in self.neighborhood_queryset]

    def add_state_in_cache(self, state: State):
        self.states_cache.append({"id": state.id, "initials": state.initials})

    def _get_state_from_cache(self, uf_initials: str) -> dict:
        return [state for state in self.states_cache if state.get('initials') == uf_initials][0]

    def get_city_from_cache(self, description: str, state_id: int) -> {dict, None}:
        try:
            return [city
                    for city
                    in self.cities_cache
                    if city.get('description') == description and city.get('state_id') == state_id][0]
        except IndexError:
            return None

    def get_neighborhood_from_cache(self, description: str, city_id: int) -> {dict, None}:
        try:
            return [neighborhood
                    for neighborhood
                    in self.neighborhood_cache
                    if neighborhood.get('description') == description and neighborhood.get('city_id') == city_id][0]
        except IndexError:
            return None

    def add_city_in_cache(self, city: City):
        new_city = {"id": city.id, "description": city.description, "state_id": city.state.id}
        self.cities_cache.append(new_city)
        return new_city

    def add_neighborhood_in_cache(self, neighborhood: Neighborhood):
        new_neighborhood = {"id": neighborhood.id,
                            "description": neighborhood.description,
                            "city_id": neighborhood.city.id}
        self.neighborhood_cache.append(new_neighborhood)
        return new_neighborhood

    def _load_city(self, state: dict, city_description: str) -> dict:
        city_from_cache = self.get_city_from_cache(city_description, state.get('id'))

        if city_from_cache is None:
            city_data = {"description": city_description, "state_id": state.get("id")}

            city, created = self.city_queryset.get_or_create(**city_data, defaults=city_data)
            if created:
                city_from_cache = self.add_city_in_cache(city)

                if self._verbosity_level >= self.VerbosityLevels.created_objects:
                    print('Created city "{}" in state "{}"'.format(city.description, state.get("initials")))

        return city_from_cache

    def _load_neighborhood(self, city: dict, neighborhood_name: str) -> dict:
        neighborhood_from_cache = self.get_neighborhood_from_cache(neighborhood_name, city.get('id'))

        if neighborhood_from_cache is None:
            neighborhood_data = {"description": neighborhood_name, "city_id": city.get('id')}
            neighborhood, created = self.neighborhood_queryset.get_or_create(**neighborhood_data,
                                                                             defaults=neighborhood_data)

            if created:
                neighborhood_from_cache = self.add_neighborhood_in_cache(neighborhood)

                if self._verbosity_level >= self.VerbosityLevels.created_objects:
                    error_message_mask = 'Created neighborhood "{}" in city "{}" and state "{}"'
                    print(error_message_mask.format(neighborhood.description,
                                                    neighborhood.city.description,
                                                    neighborhood.city.state.initials))

        return neighborhood_from_cache

    def _load_address(self, neighborhood: dict, address_text: str, zip_code: str) -> Address:
        address_data = {'neighborhood_id': neighborhood.get("id"),
                        'zip_code': zip_code,
                        'description': address_text}
        address, created = self.address_queryset.get_or_create(**address_data, defaults=address_data)

        if self._verbosity_level >= self.VerbosityLevels.created_objects and created:
            address_log_mask = 'Created address "{}" in neighborhood "{}", city "{}" and state "{}"'
            print(address_log_mask.format(address.description,
                                          address.neighborhood.description,
                                          address.neighborhood.city.description,
                                          address.neighborhood.city.state.initials))

        return address

    def extract_csvs_from_zip(self):
        with zipfile.ZipFile(self._input_file_path) as zip_arch:
            inner_files = zip_arch.namelist()

            csv_files = [file for file in inner_files if file.endswith('.csv')]

            if csv_files is None or len(csv_files) == 0:
                raise CommandError("The input file is a zip file, but it doesn't contain CSV files")

            for csv_file in csv_files:
                try:
                    zip_arch.extract(csv_file, os.path.dirname(self._input_file_path))
                    self._csv_files_path.append(os.path.join(os.path.dirname(self._input_file_path), csv_file))
                except Exception as e:
                    raise CommandError('Extract of file "{}" from zip has failed.', csv_file)

    @classmethod
    def get_city_dict(cls, csv_line: str) -> {dict, None}:
        csv_line = csv_line.strip()

        if csv_line.endswith(';'):
            csv_line = csv_line[0:-1]

        address_fields = csv_line.strip().split(';')

        if len(address_fields) != 5:
            return None

        for i in range(0, len(address_fields)):
            address_fields[i] = address_fields[i].strip()
            if not address_fields[i]:
                address_fields[i] = ''

        city_name, address_text, neighborhood_name, uf_initials, zip_code = address_fields

        zip_code = zip_code.replace('-', '')

        return {
            'city_name': city_name,
            'address_text': address_text,
            'neighborhood_name': neighborhood_name,
            'uf_initials': uf_initials,
            'zip_code': zip_code
        }

    def import_csv_file(self, csv_file):
        self._current_csv_file_path = csv_file
        file_lines = self.read_all_csv_lines()

        for index, line in enumerate(file_lines):
            try:
                if index == 0:
                    # Skip header
                    continue

                city_data = self.get_city_dict(line)

                if not city_data:
                    raise CommandError('Adress data "{}" in line "{}" is not valid'.format(line, index + 1))

                state = self._get_state_from_cache(city_data.get('uf_initials'))

                city = self._load_city(state, city_data.get('city_name'))

                neighborhood = self._load_neighborhood(city, city_data.get('neighborhood_name'))

                self._load_address(neighborhood, city_data.get('address_text'), city_data.get('zip_code'))

                if self._verbosity_level >= self.VerbosityLevels.imported_rows:
                    print('line "{}" imported'.format(index + 1))
            except Exception as e:
                error_mask = 'Failed to import line "{}" from file "{}". Error: {}'
                raise CommandError(error_mask.format(index + 1,
                                                     self._current_csv_file_path,
                                                     e))
        if self.is_zip_file:
            os.remove(self._current_csv_file_path)

    def load(self):
        self.is_zip_file = zipfile.is_zipfile(self._input_file_path)
        if self.is_zip_file:
            self.extract_csvs_from_zip()
        else:
            self._csv_files_path.append(self._input_file_path)

        for csv_file in self._csv_files_path:
            self.import_csv_file(csv_file)
