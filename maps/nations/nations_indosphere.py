"""A map of _Nations_ (not states) of the ~Indosphere region in
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap


import maps.nations.nations_india
import maps.nations.nations_silkroad_maritime
import maps.nations.nations_silkroad_overland
import maps.rivers.rivers_gangetic
import maps.rivers.rivers_peninsular
import maps.rivers.rivers_saptasindhu
import maps.rivers.rivers_silkrd


if __name__ == "__main__":
    import maps.base_options
    xatra.TitleBox("""
    Nations, not states, of the ~Indosphere region in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    xatra.show(
        out_json="../maps/nations_indosphere.json",
        out_html="../maps/nations_indosphere.html",
    )
