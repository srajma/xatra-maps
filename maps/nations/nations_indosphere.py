"""A map of _Nations_ (not states) of the ~Indosphere region in
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap
import maps.nations.nations_india, maps.nations.nations_silkroad_maritime, maps.nations.nations_silkroad_overland, maps.rivers.rivers_gangetic, maps.rivers.rivers_peninsular, maps.rivers.rivers_saptasindhu, maps.rivers.rivers_silkrd
import maps.base_options

def add_flags(map: xatra.Map):
    maps.nations.nations_india.add_flags(map)
    maps.nations.nations_silkroad_maritime.add_flags(map)
    maps.nations.nations_silkroad_overland.add_flags(map)
    maps.rivers.rivers_gangetic.add_flags(map)
    maps.rivers.rivers_peninsular.add_flags(map)
    maps.rivers.rivers_saptasindhu.add_flags(map)
    maps.rivers.rivers_silkrd.add_flags(map)


if __name__ == "__main__":
    map = xatra.Map()
    maps.base_options.add_flags(map)
    add_flags(map)
    map.TitleBox("""
    Nations, not states, of the ~Indosphere region in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    map.show(
        out_json="../maps/nations_indosphere.json",
        out_html="../maps/nations_indosphere.html",
    )
