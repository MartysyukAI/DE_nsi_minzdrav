from src.db.connection import get_connection
from psycopg.types.json import Json


class MedicalOrganizationRepository:

    INSERT_SQL = """
    INSERT INTO nsi.raw_medical_organizations (

        raw_record_hash,

        source_record_id,

        org_id,

        full_name,
        short_name,

        inn,
        kpp,
        ogrn,

        address,

        region_id,
        region_name,

        medical_subject_name,
        organization_type,

        mo_dept_id,
        mo_dept_name,

        create_date,
        modify_date,
        delete_date,
        delete_reason,

        raw_payload,

        source_version,
        record_source

    )
    VALUES (

        %(raw_record_hash)s,

        %(source_record_id)s,

        %(org_id)s,

        %(full_name)s,
        %(short_name)s,

        %(inn)s,
        %(kpp)s,
        %(ogrn)s,

        %(address)s,

        %(region_id)s,
        %(region_name)s,

        %(medical_subject_name)s,
        %(organization_type)s,

        %(mo_dept_id)s,
        %(mo_dept_name)s,

        %(create_date)s,
        %(modify_date)s,
        %(delete_date)s,
        %(delete_reason)s,

        %(raw_payload)s,

        %(source_version)s,
        %(record_source)s
    )
    ON CONFLICT (raw_record_hash)
    DO NOTHING
    """

    def insert_records(
        self,
        records: list[dict],
        batch_size: int = 2000
    ):

        total = len(records)

        with get_connection() as conn:

            with conn.cursor() as cur:

                for i in range(0, total, batch_size):

                    batch = records[i:i + batch_size]

                    prepared_batch = []

                    for row in batch:

                        row['raw_payload'] = Json(
                            row['raw_payload']
                        )

                        prepared_batch.append(row)

                    cur.executemany(
                        self.INSERT_SQL,
                        batch
                    )

                    conn.commit()

                    print(
                        f'[LOAD] '
                        f'{min(i + batch_size, total)}/{total}'
                    )