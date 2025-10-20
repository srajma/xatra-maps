import xatra
from xatra.territory_library import *
from xatra import Icon
# import maps.nations.nations_silkroad_maritime
import sea_suvarnabhumi
from sea_suvarnabhumi import CITY_ICON, PORT_ICON, REF_MOTI_CHANDRA, REF_MAJUMDAR, colon
import maps.base_options

def add_flags(map: xatra.Map):
    map.Flag(label="SUVARṆABHŪMĪ", value=SEA)
    map.Flag(label="MEDITERRANEAN", value=MEDITERRANEAN)
    map.Flag(label="GULF", value=GULF)
    map.Flag(label="AFRICA_EAST_SPOTTY", value=AFRICA_EAST_SPOTTY)
    map.Flag(label="LEVANT", value=LEVANT)
    map.Flag(label="IRANIC", value=IRANIC)
    map.Flag(label="JAMBUDVĪPA", value=SUBCONTINENT_PROPER - SIMHALA)
    map.Flag(label="SIMHALA", value=SIMHALA)
    map.Flag(label="CHINA", value=CHINA_PROPER | NORTH_VIETNAM)
    sea_suvarnabhumi.add_flags(map)
    map.Point(
        label="Dvīpa Sukhadara",
        position=[12.486956, 53.826729],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other"
    )
    map.Point(
        label="Romā",
        position=[41.887902, 12.516424],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other"
    )
    map.Point(
        label="Gaṅgana/Kāliyadvīpa",
        position=[-6.109298, 39.423733],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other",
        note=REF_MOTI_CHANDRA.format("p. 133")
    )
    map.Point(
        label="Apāragaṅgana",
        position=[-7.462715, 39.326029],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other",
        note=REF_MOTI_CHANDRA.format("p. 133")
    ),
    map.Point(
        label="Alassaṇḍa/<br>Yavanapura",
        position=[31.210757, 29.919430],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other",
        note=REF_MOTI_CHANDRA.format("p. 133")
    ),
    map.Point(
        label="Barbara?",
        position=[10.438412, 45.012126],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other"
    ),
    map.Point(
        label="Antākhī",
        position=[36.209129, 36.178443],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other",
        note=REF_MOTI_CHANDRA.format("p. xiv")
    ),
    map.Point(
        label="Bāveru",
        position=[32.519873, 44.423970],
        icon=PORT_ICON,
        show_label=True,
        classes="port-label-other"
    ),
    # funny thing AI came up with, not real:
    # map.Point(
    #     label="Kālakācārya",
    #     position=[-0.789275, 36.428155]
    # ),
    map.Text(
        label="SIṂHALA",
        position=[7.526199, 80.774671],
        classes="general-label-other general-label-other-simhala"
    )
    map.Text(
        label="Pārasīka",
        position=[31.244868, 53.597872],
        classes="general-label-other general-label-other-parasika"
    ),
    map.Text(
        label="Khuramāla Sea/<br>Pārasavāsa Sea",
        position=[26.191326, 52.671155],
        classes="general-label-other general-label-other-khuramala",
        note=REF_MOTI_CHANDRA.format("p. 61"),
    ),
    map.Text(
        label="Dadhimāla Sea",
        position=[20.083571, 38.700488],
        classes="general-label-other general-label-other-dadhimala",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    map.Text(
        label="Agnimāla Sea",
        position=[12.332840, 47.519639],
        classes="general-label-other general-label-other-agnimala",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    map.Text(
        label="Marukāntāra Desert",
        position=[18.953132, 35.475510],
        classes="general-label-other general-label-other-marukantara",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    map.Text(
        label=colon("Nīlakuṣamāla?", "(Suez gulf)"),
        position=[28.576944, 33.147515],
        classes="general-label-other general-label-other-nilakusamala",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    map.Text(
        label=colon("Nalamāla?", "(old Suez canal)"),
        position=[31.094234, 32.296720],
        classes="general-label-other general-label-other-nalamala",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    map.Text(
        label="Yavana",
        position=[39.134265, 21.801574],
        classes="general-label-other general-label-other-yavana",
        note=REF_MOTI_CHANDRA.format("p. 133"),
    ),
    map.Text(
        label="Parama-yavana",
        position=[38.453380, 29.463347],
        classes="general-label-other general-label-other-paramayavana",
        note=REF_MOTI_CHANDRA.format("p. 133"),
    ),
    map.Text(
        label="Roma-Viṣaya",
        position=[43.347301, 11.792144],
        classes="general-label-other general-label-other-romavisaya",
    ),
    map.Text(
        label="Valabhāmukha Sea",
        position=[35.392349, 19.468104],
        classes="general-label-other general-label-other-valabhamukha",
        note=REF_MOTI_CHANDRA.format("p. 61, 63"),
    ),
    # IT'S DOING KALAKACARYA AGAIN!!!
    # map.Text(
    #     label="Kālakācārya",
    #     position=[-0.789275, 36.428155],
    #     classes="general-label-other general-label-other-kalakacarya",
    #     note="p. 61, 63",
    # ),
    map.Text(
        label="Yavana",
        position=[33.964831, 27.000472],
        classes="general-label-other general-label-other-yavana-big",
    ),
    map.Text(
        label="Jambudvīpa",
        position=[21.407506, 78.480723],
        classes="general-label-other general-label-other-jambudvipa",
    ),
    map.Text(
        label="Cīnā",
        position=[30.750277, 114.330864],
        classes="general-label-other general-label-other-cina",
    ),
    map.Text(
        label="Kālayavana?",
        position=[10.068956, 38.311893],
        classes="general-label-other general-label-other-kalayavana",
    ),

    map.CSS("""
        .general-label-other {
            color: #666666;
            text-transform: uppercase;
            font-weight: bold;
        }
        .port-label-other {color: black; line-height: 1;}
        .city-label-other {color: blue; line-height: 1;}
        
        .general-label-other-parasika {
            transform: rotate(45deg) !important;
        }
        .general-label-other-khuramala {
            transform: rotate(38deg) !important;
        }
        .general-label-other-dadhimala {
            transform: rotate(60deg) !important;
        }
        .general-label-other-agnimala {
            transform: rotate(-20deg) !important;
        }
        .general-label-other-marukantara {
            transform: rotate(60deg) !important;
        }
        .general-label-other-nilakusamala {
            font-size: 0.85em; line-height: 1
        }
        .general-label-other-nalamala {
            font-size: 0.85em; line-height: 1; transform: rotate(10deg) !important;
        }
        .general-label-other-yavana-big {
            font-size: 18pt;
        }
        .general-label-other-jambudvipa {
            font-size: 24pt;
            color: #333;
        }
        .general-label-other-cina {
            font-size: 18pt;
        }
        .general-label-other-kalayavana {
            font-size: 18pt; transform: rotate(45deg) !important;
        }
        .flag-label {display: none;}
    """)


if __name__ == "__main__":
    map = xatra.Map()
    maps.base_options.add_flags(map, default="Esri.WorldPhysical")
    add_flags(map)
    map.TitleBox(f"""
    Sea routes of India < 300 AD. Southeast Asia shows states and colonies in 1st and 2nd centuries. 
    <br><br>
    <b>Sources:</b><br>
    RC Majumdar (1979), Ancient Indian colonization in Southeast Asia. p. 20-33.<br>
    Moti Chandra (1977), Trade and Trade Routes in Ancient India. p. 132-133, xiv
    <br><br>
    {PORT_ICON.to_html()} <span style="color:black">Cities and ports mentioned in Indian literature</span><br>
    {CITY_ICON.to_html()} <span style="color:blue">Capitals of Indian(-ized) states known from local or Chinese history</span><br><br>
    """)
    map.zoom(4)
    map.focus(30.0,78.0)
    map.show(out_json="docs/sea.json", out_html="docs/sea.html")
