from src.dv.hash import sat_hash
from src.dv.hub_repo import HubRepository
from src.dv.sat_repo import SatelliteRepository
from src.dv.tracking_repo import TrackingRepository


class DVService:

    def __init__(self):
        self.hub = HubRepository()
        self.sat = SatelliteRepository()
        self.trk = TrackingRepository()

    def process(self, record: dict, load_date):

        org_id = record['org_id']

# hub
        hub_key = self.hub.ensure_hub(org_id)

# satellite
        new_hash = sat_hash(record)
        old_hash = self.sat.get_last_hash(hub_key)

        sat_changed = new_hash != old_hash

        if sat_changed:
            self.sat.insert_sat(hub_key, record, new_hash, load_date)

# tracking по ключевым бизнес-атрибутам
        tracked_fields = [
            'full_name',
            'short_name',
            'address',
            'ved_affiliation_id'
        ]

        if sat_changed:
            for field in tracked_fields:

                new_value = record.get(field)

                if new_value is None:
                    continue

                self.trk.close_old(
                    hub_key,
                    field,
                    load_date
                )

                self.trk.insert_new(
                    hub_key,
                    field,
                    str(new_value),
                    load_date
                )