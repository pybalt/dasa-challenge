import requests
import json
from app.utils.logger import logger


class API:

    BASE_URL = 'https://eje.juscaba.gob.ar/iol-api/api/public/expedientes'

    @staticmethod
    def get(sub_url: str, params: str):
        logger.info(f"GET on: {API.BASE_URL}/{sub_url} with params: {params}")

        return requests.get(f"{API.BASE_URL}/{sub_url}", params=params)

    @staticmethod
    def post(sub_url: str, params: str, payload: object):
        logger.info(f"POST on: {API.BASE_URL}/{sub_url}")

        return requests.post(f"{API.BASE_URL}/{sub_url}", params=params, data=payload)

    @staticmethod
    def get_list(filter: json):
        payload = {'info': json.dumps(filter)}
        data = API.post("lista", params=None, payload=payload)
        data.raise_for_status()

        return data.json()

    @staticmethod
    def get_record_details(exp_id: int):
        data = API.get("ficha",
                       params={"expId": exp_id})
        data.raise_for_status()

        return data.json()
