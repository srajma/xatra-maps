import xatra

def add_flags(map: xatra.Map, default="Esri.WorldTopoMap"):
    for base in [
        "Esri.WorldTopoMap",
        "OpenStreetMap",
        "Esri.WorldImagery",
        "OpenTopoMap",
        "Esri.WorldPhysical",
    ]:
        is_default = base == default
        map.BaseOption(base, default=is_default)