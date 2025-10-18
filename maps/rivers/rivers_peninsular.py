import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.Map):
    map.River(label="Narmada", value=overpass("5405552"), show_label=True)
    map.River(label="Godavari", value=overpass("2826093"), show_label=True)
    map.River(label="Krsnaveni", value=overpass("337204"), show_label=True)
    map.River(label="Bhimarathi", value=overpass("2858525"), show_label=True)
    map.River(label="Tungabhadra", value=overpass("2742213"), show_label=True)
    map.River(label="kaveri", value=overpass("2704746"), show_label=True)
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)