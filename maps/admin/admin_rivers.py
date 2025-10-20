import xatra
import maps.base_options

def add_flags(map: xatra.Map):
    map.AdminRivers(sources=["naturalearth", "overpass"])
    map.CSS(r""".river {stroke-width: 5;}""")

if __name__ == "__main__":
    m = xatra.Map()
    maps.base_options.add_flags(m)
    add_flags(m)
    m.TitleBox("""Rivers.""")

    m.show(out_json="docs/admin_rivers.json", out_html="docs/admin_rivers.html")