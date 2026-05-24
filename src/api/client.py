import requests
import urllib3
import zipfile
import json
from io import BytesIO

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class NSIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_filename(self, oid: str, version: str, file_format: str = 'json') -> str:
        url = f'{self.base_url}/api/dataFiles'

        response = requests.get(
            url,
            params={
                'identifier': oid,
                'version': version,
                'format': file_format
            },
            verify=False,
            timeout=60
        )
        response.raise_for_status()
        return response.json()[0]
    
    def download_zip(self, filename: str) -> bytes:

        url = f'{self.base_url}/api/dataFiles/{filename}'

        response = requests.get(url, verify=False, timeout=120)

        response.raise_for_status()
        return response.content
    
    def extract_json(self, zip_bytes: bytes) -> dict:

        with zipfile.ZipeFile(BytesIO(zip_bytes)) as z:
            json_file = z.namelist()[0]

            with z.open(json_file) as f:
                return json.load(f)