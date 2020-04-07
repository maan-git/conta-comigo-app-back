from abc import ABC
from abc import abstractmethod


class ExternalAddressProvider(ABC):
    @abstractmethod
    def get_address_by_zip(self, zip_code: str):
        """
        Gets an address from an external source and returns a dictionary in the following format:
        {
            'state_initials': '',
            'city_name': '',
            'neighborhood_name': '',
            'address': '',
            'zip': '' (no formatting chars)
        }
        """
        pass
