from src.db.connection import get_connection


class TrackingRepository:

    def close_old(self, hub_key: str, attr: str, new_date):

        sql = '''
        UPDATE nsi.sat_organization_changes
        SET valid_to = (%s::date - INTERVAL '1 day')
        WHERE hub_org_hash_key = %s
          AND attribute_name = %s
          AND valid_to IS NULL
        '''

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_date, hub_key, attr))
            conn.commit()

    def insert_new(self, hub_key: str, attr: str, value: str, from_date):

        sql = '''
        INSERT INTO nsi.sat_organization_changes (
            hub_org_hash_key,
            attribute_name,
            attribute_value,
            valid_from,
            valid_to
        )
        VALUES (%s, %s, %s, %s, NULL)
        '''

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (
                    hub_key,
                    attr,
                    value,
                    from_date
                ))
            conn.commit()