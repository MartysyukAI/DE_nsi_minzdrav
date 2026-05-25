import hashlib


def generate_record_hash(organization_id: str, source_version: str) -> str:
    raw_key = f'{organization_id}|{source_version}'
    return hashlib.md5(raw_key.encode('utf-8')).hexdigest()