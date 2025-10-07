"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
import rivers_gangetic
import rivers_peninsular
import rivers_saptasindhu
import rivers_silkrd

def add_flags(map: xatra.FlagMap):
    map.Admin(gadm="IND", level=3, color_by_level=2)
    map.Admin(gadm="PAK", level=3, color_by_level=2) # level-3 GADM divisions in Pak are more like districts, but we don't have finer data
    map.Admin(gadm="BGD", level=3, color_by_level=2)
    map.Admin(gadm="AFG", level=2, color_by_level=2) # level-2 is the best we have for Afghanistan
    map.Admin(gadm="NPL", level=3, color_by_level=2) # level-3 GADM divisions in Nepal are more like districts, but level-4 is WAY too fine
    map.Admin(gadm="BTN", level=2, color_by_level=2) # level-2 is the best we have for Bhutan, and they're like taluks anyway
    map.Admin(gadm="LKA", level=2, color_by_level=2) # level-2 is the best we have for Lanka, and they're like taluks anyway


if __name__ == "__main__":
    map = xatra.FlagMap()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
    add_flags(map)
    rivers_gangetic.add_flags(map)
    rivers_peninsular.add_flags(map)
    rivers_saptasindhu.add_flags(map)
    rivers_silkrd.add_flags(map)
    map.TitleBox("""
    Indian taluks (level-3 subdivisions).
    <br>
    <code>
    map.Admin(gadm="IND", level=3)
    map.Admin(gadm="PAK", level=3) # level-3 GADM divisions in Pak are more like districts, but we don't have finer data
    map.Admin(gadm="BGD", level=3)
    map.Admin(gadm="AFG", level=2) # level-2 is the best we have for Afghanistan
    map.Admin(gadm="NPL", level=3) # level-3 GADM divisions in Nepal are more like districts, but level-4 is WAY too fine
    map.Admin(gadm="BTN", level=2) # level-2 is the best we have for Bhutan, and they're like taluks anyway
    map.Admin(gadm="LKA", level=2) # level-2 is the best we have for Lanka, and they're like taluks anyway
    </code>
    """)
    map.CSS(r"""
    .river {
        stroke-width: 5;
    }
    """)
    map.show(out_json="docs/admin_india_3.json", out_html="docs/admin_india_3.html")

