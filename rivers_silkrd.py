import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.FlagMap):
    map.River(label="Kubha (kabul)", value=overpass("1676476"))
    map.River(label="Kama (kunar)", value=overpass("6608825"))
    map.River(label="Haraxvati (arghandab)", value=overpass("8623883"))
    map.River(label="Haetumant (helmand)", value=overpass("5252846"))
    map.River(label="Hari (hari)", value=overpass("3173475"))
    map.River(label="Vaksu (amu darya)", value=overpass("223008"))
    map.River(label="Jaxartes (syr darya)", value=overpass("1206456"))
    map.River(label="Sita (tarim)", value=overpass("2162521"))
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)