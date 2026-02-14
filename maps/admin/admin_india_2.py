"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra

xatra.Admin(gadm="IND", level=2, color_by_level=1)
xatra.Admin(gadm="Z06.1", level=3, color_by_level=1)  # special handling for Pakistani-occupied Jammu & Kashmir
xatra.Admin(gadm="PAK", level=3, color_by_level=1) # level-3 GADM divisions in Pak are more like districts
xatra.Admin(gadm="BGD", level=2, color_by_level=1)
xatra.Admin(gadm="AFG", level=2, color_by_level=1)
xatra.Admin(gadm="NPL", level=3, color_by_level=1) # level-3 GADM divisions in Nepal are more like districts
xatra.Admin(gadm="BTN", level=2, color_by_level=1)
xatra.Admin(gadm="LKA", level=2, color_by_level=1)


if __name__ == "__main__":
    import maps.base_options
    import maps.rivers.rivers_gangetic
    import maps.rivers.rivers_peninsular
    import maps.rivers.rivers_saptasindhu
    import maps.rivers.rivers_silkrd
    xatra.TitleBox("""
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
    xatra.CSS(r"""
    .river {
        stroke-width: 5;
    }
    """)
    xatra.show(out_json="../maps/admin_india_2.json", out_html="../maps/admin_india_2.html")

