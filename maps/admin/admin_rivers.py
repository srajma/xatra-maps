import xatra

xatra.AdminRivers(sources=["naturalearth", "overpass"])
xatra.CSS(r""".river {stroke-width: 5;}""")

if __name__ == "__main__":
    import maps.base_options
    xatra.TitleBox("""Rivers.""")
    xatra.show(out_json="../maps/admin_rivers.json", out_html="../maps/admin_rivers.html")