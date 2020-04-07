import requests
import json
from app.services.external_address_provider import ExternalAddressProvider


class ExternalProviderRepVirtual(ExternalAddressProvider):
    republica_virtual_url = 'http://cep.republicavirtual.com.br/web_cep.php'

    def get_address_by_zip(self, zip_code: str):
        try:
            response = requests.get(self.republica_virtual_url, params={'cep': zip_code, 'formato': 'json'})
        except:
            # TODO write log
            return None

        if response.status_code != 200:
            # TODO write log
            return None

        response_str = response.content.decode('iso-8859-1')
        response_dict = json.loads(response_str)

        result = None

        if response_dict.get('resultado') != '0':
            result = {
                'state_initials': response_dict.get('uf'),
                'city_name': response_dict.get('cidade'),
                'neighborhood_name': response_dict.get('bairro'),
                'address': '{} {}'.format(response_dict.get('tipo_logradouro'), response_dict.get('logradouro')),
                'zip': zip_code
            }

        return result
