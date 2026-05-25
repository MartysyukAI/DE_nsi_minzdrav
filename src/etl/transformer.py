from src.utils.address import build_address
from src.utils.hashing import generate_record_hash
from src.utils.parsing import parse_date


def transform(record: dict, version: str) -> dict:

    return {

        'raw_record_hash': generate_record_hash(
            record['oid'],
            version
        ),

        'source_record_id': record.get('id'),

        'org_id': record.get('oid'),

        'full_name': record.get('nameFull'),
        'short_name': record.get('nameShort'),

        'inn': record.get('inn'),
        'kpp': record.get('kpp'),
        'ogrn': record.get('ogrn'),

        'address': build_address(record),

        'region_id': str(record.get('regionId'))
        if record.get('regionId') else None,

        'region_name': record.get('regionName'),

        'medical_subject_name': record.get('medicalSubjectName'),

        'organization_type': str(record.get('organizationType'))
        if record.get('organizationType') else None,

        'mo_dept_id': str(record.get('moDeptId'))
        if record.get('moDeptId') else None,

        'mo_dept_name': record.get('moDeptName'),

        'create_date': parse_date(
            record.get('createDate')
        ),

        'modify_date': parse_date(
            record.get('modifyDate')
        ),

        'delete_date': parse_date(
            record.get('deleteDate')
        ),

        'delete_reason': record.get('deleteReason'),

        'raw_payload': record,

        'source_version': version,

        'record_source': 'nsi.rosminzdrav.ru'
    }