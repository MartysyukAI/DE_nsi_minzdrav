from psycopg.rows import dict_row

from src.db.connection import get_connection


def insert_records(records: list[dict]):

    query = """
    INSERT INTO nsi.raw_medical_organizations (
        record_hash,
        organization_id,
        full_name,
        short_name,
        ogrn,
        inn,
        address,
        department_id,
        registry_inclusion_date,
        source_version,
        raw_payload
    )
    VALUES (
        %(record_hash)s,
        %(organization_id)s,
        %(full_name)s,
        %(short_name)s,
        %(ogrn)s,
        %(inn)s,
        %(address)s,
        %(department_id)s,
        %(registry_inclusion_date)s,
        %(source_version)s,
        %(raw_payload)s
    )
    ON CONFLICT (record_hash) DO NOTHING
    """

    with get_connection() as conn:

        with conn.cursor(row_factory=dict_row) as cur:

            cur.executemany(query, records)

        conn.commit()