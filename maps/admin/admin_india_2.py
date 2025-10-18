"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
import maps.rivers.rivers_gangetic
import maps.rivers.rivers_peninsular
import maps.rivers.rivers_saptasindhu
import maps.rivers.rivers_silkrd

def add_flags(map: xatra.Map):
    map.Admin(gadm="IND", level=2, color_by_level=1)
    map.Admin(gadm="PAK", level=3, color_by_level=1) # level-3 GADM divisions in Pak are more like districts
    map.Admin(gadm="BGD", level=2, color_by_level=1)
    map.Admin(gadm="AFG", level=2, color_by_level=1)
    map.Admin(gadm="NPL", level=3, color_by_level=1) # level-3 GADM divisions in Nepal are more like districts
    map.Admin(gadm="BTN", level=2, color_by_level=1)
    map.Admin(gadm="LKA", level=2, color_by_level=1)


if __name__ == "__main__":
    map = xatra.Map()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
    add_flags(map)
    maps.rivers.rivers_gangetic.add_flags(map)
    maps.rivers.rivers_peninsular.add_flags(map)
    maps.rivers.rivers_saptasindhu.add_flags(map)
    maps.rivers.rivers_silkrd.add_flags(map)
    map.TitleBox("""
    Indian districts (level-2 subdivisions).
    <br>
    <code>
    map.Admin(gadm="IND", level=2, color_by_level=1)
    map.Admin(gadm="PAK", level=3, color_by_level=1) # level-3 GADM divisions in Pak are more like districts
    map.Admin(gadm="BGD", level=2, color_by_level=1)
    map.Admin(gadm="AFG", level=2, color_by_level=1)
    map.Admin(gadm="NPL", level=3, color_by_level=1) # level-3 GADM divisions in Nepal are more like districts
    map.Admin(gadm="BTN", level=2, color_by_level=1)
    map.Admin(gadm="LKA", level=2, color_by_level=1)
    </code>
    """)
    map.CSS(r"""
    .river {
        stroke-width: 5;
    }
    """)
    map.show(out_json="docs/admin_india_2.json", out_html="docs/admin_india_2.html")

