from src.utils.hashing import make_md5
from src.utils.address import build_address
from src.utils.parsing import parse_date


def transform(record: dict, version: str) -> dict:

    return {
        "record_hash": make_md5(record["oid"], version),

        "org_id": record.get("oid"),

        "oid": record.get("oid"),

        "full_name": record.get("nameFull"),
        "short_name": record.get("nameShort"),

        "inn": record.get("inn"),
        "kpp": record.get("kpp"),
        "ogrn": record.get("ogrn"),

        "address": build_address(record),

        "region_id": record.get("regionId"),
        "region_name": record.get("regionName"),

        "medical_subject_name": record.get("medicalSubjectName"),
        "organization_type": record.get("organizationType"),

        "mo_dept_id": record.get("moDeptId"),
        "mo_dept_name": record.get("moDeptName"),

        "create_date": parse_date(record.get("createDate")),
        "modify_date": parse_date(record.get("modifyDate")),
        "delete_date": parse_date(record.get("deleteDate")),
        "delete_reason": record.get("deleteReason"),

        "source_version": version,
        "record_source": "nsi.rosminzdrav.ru",

        "raw_payload": record
    }