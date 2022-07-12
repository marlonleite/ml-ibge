import requests


class IBGE:
    IBGE_API_URL = "https://servicodados.ibge.gov.br/api"

    @classmethod
    def get_states(cls):
        path = f"{cls.IBGE_API_URL}/v1/localidades/estados"
        return cls._call_api(path)

    @classmethod
    def get_cities(cls, uf: str):
        path = f"{cls.IBGE_API_URL}/v1/localidades/estados/{uf}/distritos"
        return cls._call_api(path)

    @classmethod
    def _call_api(cls, path: str):
        params = {"view": "nivelado", "orderBy": "nome"}
        response = requests.get(path, params=params)

        return response.json()
