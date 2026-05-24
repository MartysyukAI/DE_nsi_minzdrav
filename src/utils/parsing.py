from datetime import datetime


def parse_date(value: str | None):
    if not value:
        return None

    try:
        return datetime.strptime(value, "%d.%m.%Y").date()
    except Exception:
        return None