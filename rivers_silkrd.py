import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.FlagMap):
    map.River(label="Kubha (kabul)", value=overpass("1676476"), show_label=True)
    map.River(label="Kama (kunar)", value=overpass("6608825"), show_label=True)
    map.River(label="Haraxvati (arghandab)", value=overpass("8623883"), show_label=True)
    map.River(label="Haetumant (helmand)", value=overpass("5252846"), show_label=True)
    map.River(label="Hari (hari)", value=overpass("3173475"), show_label=True)
    map.River(label="Vaksu (amu darya)", value=overpass("223008"), show_label=True)
    map.River(label="Jaxartes (syr darya)", value=overpass("1206456"), show_label=True)
    map.River(label="Sita (tarim)", value=overpass("2162521"), show_label=True)
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)