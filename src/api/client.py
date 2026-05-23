import os
import zipfile
from io import BytesIO
import xml.etree.ElementTree as ET
import requests
from dotenv import load_dotenv

load_dotenv()


class NSIClient:

    def __init__(self):

        self.base_url = os.getenv('API_BASE_URL')
        self.token = os.getenv('API_TOKEN')
        self.oid = os.getenv('NSI_OID')

        self.session = requests.Session()

        self.session.headers.update(
            {
                'X-Oncor-API-Token': self.token
            }
        )

    def get_passport(self):

        url = (
            f'{self.base_url}'
            f'/api/1.0/json/nsi.rosminzdrav.ru/passport'
        )

        response = self.session.get(
            url,
            params={'oid': self.oid},
            timeout=30,
#            verify=False
        )

        response.raise_for_status()

        return response.json()
    
    def download_zip(self):

        url = (
            f'{self.base_url}'
            f'/api/1.0/json/nsi.rosminzdrav.ru/zip'
        )

        response = self.session.get(
            url,
            params={'oid': self.oid},
            timeout=60,
        )

        response.raise_for_status()

        return response.content
    
    def extract_xml_root(self, zip_content: bytes):

        with zipfile.ZipFile(BytesIO(zip_content)) as archive:
            xml_files = [f for f in archive.namelist() if f.endswith('.xml')]
            xml_filename = xml_files[0]
            with archive.open(xml_filename) as xml_file:
                tree = ET.parse(xml_file)

                return tree.getroot()
            
