from src.api.client import NSIClient
from src.db.repository import MedicalOrganizationRepository
from src.etl.transformer import transform
from src.settings import Settings


def main():

    client = NSIClient(Settings.NSI_BASE_URL)
    repository = MedicalOrganizationRepository()

    print("STEP 1: get filename")
    filename = client.get_filename(Settings.NSI_OID, Settings.NSI_VERSION)
    print("ZIP filename:", filename)

    print("STEP 2: download zip")
    zip_bytes = client.download_zip(filename)
    print("ZIP size:", len(zip_bytes))

    print("STEP 3: extract json")
    data = client.extract_json(zip_bytes)
    records = data["records"]
    print("Records extracted:", len(records))

    print("STEP 4: transform")
    transformed = [transform(r, Settings.NSI_VERSION) for r in records]
    print("Records transformed:", len(transformed))

    print("STEP 5: load to postgres")
    repository.insert_records(transformed)

    print("DONE")


if __name__ == "__main__":
    main()