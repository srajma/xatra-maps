import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.Map):
    map.River(label="Sindhu", value=overpass("1159233"), show_label=True, note="Indus")
    map.River(label="Vitastā", value=overpass("8306691"), show_label=True, note="Jhelum<br>Hydaspes")
    map.River(label="Asiknī", value=overpass("6085682"), show_label=True, note="Candrabhāga<br>Iskaāati<br>Chenab<br>Acesines")
    map.River(label="Irāvatī", value=overpass("8894611"), show_label=True, note="Puruśni<br>Ravi<br>Hydraotes")
    map.River(label="Śatadru", value=overpass("325142"), show_label=True, note="Śutudri<br>Sutlej<br>Zaradros<br>Hesidrus")
    map.River(label="Vipāśa", value=overpass("10693630"), show_label=True, note="Beas<br>Hyphasis")
    map.River(label="Sarasvatī", value=overpass("5388381"), show_label=True, note="Ghaggar")
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)