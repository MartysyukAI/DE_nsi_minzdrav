import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    NSI_BASE_URL = os.getenv("NSI_BASE_URL")
    NSI_OID = os.getenv("NSI_OID")
    NSI_VERSION = os.getenv("NSI_VERSION")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")