"""A map of _Nations_ (not states) of the overland Silk Road in 
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence


xatra.Flag(label="ZZZ_TIBET_BURMA_INTERM", classes="names-unknown", value=TIBET_BURMA_INTERM)
xatra.Flag(label="ZZZ_YUNNAN_BURMA_INTERM", classes="names-unknown", value=YUNNAN_BURMA_INTERM)
xatra.Flag(label="ZZZ_KAREN", classes="names-unknown", value=KAREN)
xatra.Flag(label="ZZZ_SIAM_BURMA_INTERM", classes="names-unknown", value=SIAM_BURMA_INTERM)
xatra.Flag(label="BURMA_UPPER", value=BURMA_UPPER)
xatra.Flag(label="BURMA_LOWER", value=BURMA_LOWER)
xatra.Flag(label="SIAM", value=SIAM)
xatra.Flag(label="LAOS", value=LAOS)
xatra.Flag(label="KHMER", value=KHMER)
xatra.Flag(label="CHAM", value=CHAM)
xatra.Flag(label="NORTH_VIETNAM", value=NORTH_VIETNAM)
xatra.Flag(label="BORNEO", value=BORNEO)
xatra.Flag(label="MALAY_PENINSULA", value=MALAY_PENINSULA)
xatra.Flag(label="SUMATRA", value=SUMATRA)
xatra.Flag(label="JAVA", value=JAVA)
xatra.Flag(label="ZZZ_LESSER_SUNDA", classes="names-unknown", value=LESSER_SUNDA)
xatra.Flag(label="ZZZ_MALUKU", classes="names-unknown", value=MALUKU)
xatra.Flag(label="ZZZ_SULAWESI", classes="names-unknown", value=SULAWESI)
xatra.Flag(label="ZZZ_KEPULAUAN", classes="names-unknown", value=KEPULAUAN)
xatra.Flag(label="ZZZ_BANGKA", classes="names-unknown", value=BANGKA)
xatra.Flag(label="ANDAMAN_NICOBAR", value=ANDAMAN_NICOBAR)
xatra.CSS(r"""
.names-unknown {fill: #444444; color: #444444 !important;}
.wild-tracts {fill: #888888; color: #888888 !important;}
.flag-label {font-size: 10px}
.path-label {font-size: 10px}
.river-label {font-size: 10px}
"""
)

if __name__ == "__main__":
    import maps.base_options
    xatra.TitleBox("""
    Nations, not states, of the Maritime Silk Road in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    xatra.show(out_json="../maps/nations_silkroad_maritime.json", out_html="../maps/nations_silkroad_maritime.html")

