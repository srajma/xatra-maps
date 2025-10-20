"""A map of _Nations_ (not states) of the overland Silk Road in 
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
import maps.base_options

def add_flags(map: xatra.Map):
    map.Flag(label="ZZZ_TIBET_BURMA_INTERM", classes="names-unknown", value=TIBET_BURMA_INTERM)
    map.Flag(label="ZZZ_YUNNAN_BURMA_INTERM", classes="names-unknown", value=YUNNAN_BURMA_INTERM)
    map.Flag(label="ZZZ_KAREN", classes="names-unknown", value=KAREN)
    map.Flag(label="ZZZ_SIAM_BURMA_INTERM", classes="names-unknown", value=SIAM_BURMA_INTERM)
    map.Flag(label="BURMA_UPPER", value=BURMA_UPPER)
    map.Flag(label="BURMA_LOWER", value=BURMA_LOWER)
    map.Flag(label="SIAM", value=SIAM)
    map.Flag(label="LAOS", value=LAOS)
    map.Flag(label="KHMER", value=KHMER)
    map.Flag(label="CHAM", value=CHAM)
    map.Flag(label="NORTH_VIETNAM", value=NORTH_VIETNAM)
    map.Flag(label="BORNEO", value=BORNEO)
    map.Flag(label="MALAY_PENINSULA", value=MALAY_PENINSULA)
    map.Flag(label="SUMATRA", value=SUMATRA)
    map.Flag(label="JAVA", value=JAVA)
    map.Flag(label="ZZZ_LESSER_SUNDA", classes="names-unknown", value=LESSER_SUNDA)
    map.Flag(label="ZZZ_MALUKU", classes="names-unknown", value=MALUKU)
    map.Flag(label="ZZZ_SULAWESI", classes="names-unknown", value=SULAWESI)
    map.Flag(label="ZZZ_KEPULAUAN", classes="names-unknown", value=KEPULAUAN)
    map.Flag(label="ZZZ_BANGKA", classes="names-unknown", value=BANGKA)
    map.Flag(label="ANDAMAN_NICOBAR", value=ANDAMAN_NICOBAR)
    map.CSS(r"""
    .names-unknown {fill: #444444; color: #444444 !important;}
    .wild-tracts {fill: #888888; color: #888888 !important;}
    .flag-label {font-size: 10px}
    .path-label {font-size: 10px}
    .river-label {font-size: 10px}
    """
    )

if __name__ == "__main__":
    map = xatra.Map()
    maps.base_options.add_flags(map)
    add_flags(map)
    map.TitleBox("""
    Nations, not states, of the Maritime Silk Road in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    map.show(out_json="docs/nations_silkroad_maritime.json", out_html="docs/nations_silkroad_maritime.html")

