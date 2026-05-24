import psycopg
from src.settings import Settings


def get_connection():

    return psycopg.connect(
        host=Settings.POSTGRES_HOST,
        port=Settings.POSTGRES_PORT,
        dbname=Settings.POSTGRES_DB,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD
    )