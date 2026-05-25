from src.db.connection import get_connection


class HubRepository:

    def ensure_hub(self, org_id: str):

        hkey = self._hash(org_id)

        sql = """
        INSERT INTO nsi.hub_organization (
            hub_org_hash_key,
            org_id
        )
        VALUES (%s, %s)
        ON CONFLICT (hub_org_hash_key) DO NOTHING
        """

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (hkey, org_id))
            conn.commit()

        return hkey

    def _hash(self, org_id: str) -> str:
        import hashlib
        return hashlib.md5(org_id.encode()).hexdigest()