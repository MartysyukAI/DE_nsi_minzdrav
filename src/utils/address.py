def build_address(r: dict) -> str | None:

    parts = [
        r.get("regionName"),
        r.get("addrRegionName"),
        r.get("areaName"),
        r.get("streetName"),
        r.get("house"),
    ]

    result = ", ".join([p for p in parts if p])

    return result if result else None