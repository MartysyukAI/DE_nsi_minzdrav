import psycopg
from src.settings import Settings
import time


def get_connection(retries=10):
    for i in range(retries):
        try:
            return psycopg.connect(
                host=Settings.POSTGRES_HOST,
                port=Settings.POSTGRES_PORT,
                dbname=Settings.POSTGRES_DB,
                user=Settings.POSTGRES_USER,
                password=Settings.POSTGRES_PASSWORD
            )
        except psycopg.OperationalError:
            print(f"DB not ready, retry {i+1}/{retries}")
            time.sleep(2)

    raise Exception("DB is not available")