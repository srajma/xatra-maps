"""A map of _Nations_ (not states) of the ~Indosphere region in
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap
import nations_india, nations_silkroad_maritime, nations_silkroad_overland, rivers_gangetic, rivers_peninsular, rivers_saptasindhu, rivers_silkrd


def add_flags(map: xatra.FlagMap):
    nations_india.add_flags(map)
    nations_silkroad_maritime.add_flags(map)
    nations_silkroad_overland.add_flags(map)
    rivers_gangetic.add_flags(map)
    rivers_peninsular.add_flags(map)
    rivers_saptasindhu.add_flags(map)
    rivers_silkrd.add_flags(map)


if __name__ == "__main__":
    map = xatra.FlagMap()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
    add_flags(map)
    map.TitleBox("""
    Nations, not states, of the ~Indosphere region in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    map.show(
        out_json="docs/nations_indosphere.json",
        out_html="docs/nations_indosphere.html",
    )
