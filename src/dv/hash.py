import hashlib
import json


def sat_hash(record: dict) -> str:

    def normalize(v):
        if hasattr(v, "isoformat"):
            return v.isoformat()
        return v    
    
    """
    hashdiff = атрибуты из sat_organization_attrs (кроме технических)
    """

    payload = {
        'full_name': record.get('full_name'),
        'short_name': record.get('short_name'),
        'inn': record.get('inn'),
        'ogrn': record.get('ogrn'),
        'address': record.get('address'),
        'ved_affiliation_id': record.get('mo_dept_id'),
        'inclusion_date': normalize(record.get('create_date'))
    }

    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    
    return hashlib.md5(raw.encode('utf-8')).hexdigest()