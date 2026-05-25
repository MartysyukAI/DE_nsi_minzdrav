from src.db.connection import get_connection


class SatelliteRepository:

    def get_last_hash(self, hub_key: str):

        sql = '''
        SELECT hashdiff
        FROM nsi.sat_organization_attrs
        WHERE hub_org_hash_key = %s
        ORDER BY load_date DESC
        LIMIT 1
        '''

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (hub_key,))
                row = cur.fetchone()

        return row[0] if row else None

    def insert_sat(self, hub_key: str, record: dict, hashdiff: str, load_date):

        sql = '''
        INSERT INTO nsi.sat_organization_attrs (
            hub_org_hash_key,
            hashdiff,
            full_name,
            short_name,
            inn,
            ogrn,
            address,
            ved_affiliation_id,
            inclusion_date,
            load_date
        )
        VALUES (
            %s, %s,
            %s, %s, %s, %s,
            %s, %s,
            %s, %s
        )
        '''

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (
                    hub_key,
                    hashdiff,
                    record.get('full_name'),
                    record.get('short_name'),
                    record.get('inn'),
                    record.get('ogrn'),
                    record.get('address'),
                    record.get('mo_dept_id'),
                    record.get('create_date'),
                    load_date
                ))
            conn.commit()