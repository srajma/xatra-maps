"""A map of _Nations_ (not states) of the overland Silk Road in 
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.Map):
    map.Flag(label="DARADA", value=DARADA)
    map.Flag(label="MARASA", value=LADAKH)
    map.Flag(label="INNER_KAMBOJA", value=INNER_KAMBOJA)
    map.Flag(label="GEDROSIA", value=BALOCH)
    map.Flag(label="KAMBOJA", value=KAMBOJA)
    map.Flag(label="MERU", value=MERU)
    map.Flag(label="ZARANJ", value=ZARANJ)
    map.Flag(label="KANDAHAR", value=KANDAHAR)
    map.Flag(label="ROHITAGIRI", value=ROHITAGIRI, classes="wild-tracts")
    map.Flag(label="HERAT", value=HERAT)
    map.Flag(label="MARGIANA", value=MARGIANA)
    map.Flag(label="BACTRIA", value=BACTRIA)
    map.Flag(label="SOGDIA_PROPER", value=SOGDIA_PROPER)
    map.Flag(label="FERGHANA", value=FERGHANA)
    map.Flag(label="KHWAREZM", value=KHWAREZM)
    map.Flag(label="KASHGAR", value=KASHGAR)
    map.Flag(label="KHOTAN", value=KHOTAN)
    map.Flag(label="AGNI", value=AGNI)
    map.Flag(label="AKSU", value=AKSU)
    map.Flag(label="KUCHA", value=KUCHA)
    map.Flag(label="ROURAN", value=ROURAN)
    map.Flag(label="QIEMO", value=QIEMO)
    map.Flag(label="KORLA", value=KORLA)
    map.Flag(label="TURFAN", value=TURFAN)
    map.Flag(label="TIBET", value=TIBET)
    map.Flag(label="YYY_HIMALAYAN", classes="wild-tracts", value=HIMALAYAN)
    map.CSS(r"""
    .names-unknown {fill: #444444; color: #444444 !important;}
    .wild-tracts {fill: #888888; color: #888888 !important;}
    .flag-label {font-size: 10px}
    .path-label {font-size: 10px}
    .river-label {font-size: 10px}
    """
    )

if __name__ == "__main__":
    map = xatra.Map()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
    add_flags(map)
    map.TitleBox("""
    Nations, not states, of the Overland Silk Road in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    map.show(out_json="docs/nations_silkroad_overland.json", out_html="docs/nations_silkroad_overland.html")

