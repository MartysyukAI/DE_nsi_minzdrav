import json

from src.api.client import NSIClient
from src.db.repository import insert_records
from src.utils.hashing import generate_record_hash


def parse_records(root):

    records = []

    for element in root.findall(".//record"):

        organization_id = element.findtext("id")

        source_version = CURRENT_VERSION

        record = {
            "record_hash": generate_record_hash(
                organization_id,
                source_version,
            ),

            "organization_id": organization_id,

            "full_name": element.findtext("fullName"),

            "short_name": element.findtext("shortName"),

            "ogrn": element.findtext("ogrn"),

            "inn": element.findtext("inn"),

            "address": element.findtext("address"),

            "department_id": element.findtext("departmentId"),

            "registry_inclusion_date":
                element.findtext("registryInclusionDate"),

            "source_version": source_version,

            "raw_payload": json.dumps({
                child.tag: child.text
                for child in element
            }),
        }

        records.append(record)

    return records


def main():

    client = NSIClient()

    passport = client.get_passport()

    global CURRENT_VERSION
    CURRENT_VERSION = passport["version"]

    zip_content = client.download_zip()

    root = client.extract_xml_root(zip_content)

    records = parse_records(root)

    insert_records(records)

    print(f"Loaded {len(records)} records")


if __name__ == "__main__":
    main()