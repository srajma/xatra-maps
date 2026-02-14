"""A map of _Nations_ (not states) of the overland Silk Road in 
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

xatra.Flag(label="VṚJISTHĀNA", value=VRJISTHANA, note="Vijayendra Kumar Mathur (1969), Aitihasik Sthanavali p 870: वृजिस्थान नामक एक ऐतिहासिक स्थान का उल्लेख प्रसिद्ध चीनी यात्री युवानच्वांग ने 'फो-लि शतंगना' नाम से किया है। सम्भवत: यह वर्तमान वज़ीरस्तान (पाकिस्तान) है।")
xatra.Flag(label="VARNU", value=VARNU)
xatra.Flag(label="VANAVYA", value=VANAVYA)
xatra.Flag(label="APRĪTA", value=APRITA, note="or Trīrāvatīka, modern Tirāh.")
xatra.Flag(label="SATTAGYDIA?", value=PSEUDOSATTAGYDIA_S, classes="names-unknown")
xatra.Flag(label="KAMBOJA", value=KAMBOJA)
xatra.Flag(label="KĀPIŚĀYANA", value=KAPISAYANA)
xatra.Flag(label="TRYAKŚYĀYAṆA", value=TRYAKSYAYANA, note = "or Dvīrāvatika, modern Dir; or Madhumant, modern Mohmand.")
xatra.Flag(
    label="AŚVAKĀYANA",
    value=ASVAKAYANA,
    note="The Hastināyanas may have have been cognate with the Aśvakāyanas, or ruled the region around Puṣkalāvatī.",
)
xatra.Flag(label="AŚVĀYANA", value=ASVAYANA)
xatra.Flag(label="NIGRAHĀRA", value=NIGRAHARA)
xatra.Flag(label="URAŚĀ", value=URASA, note="Hazara")
#     xatra.Flag(
#         label="ŚAVASA",
#         value=SAVASA,
#         note="""Of these Kekaya and Savasa may be
#  located between the Jhelum and the Chenab, the first in the
#  south and the second in the north respectively, and Madra and
#  Uśīnara between the Chenab and the Ravi in the north and
#  south respectively. The divisions become clear on the map.
#  The Divyāvadāna refers to the Śvasas in Uttarāpatha with
#  headquarters at Takṣaśilā to which Aśoka was deputed by his
#  father Bindusāra as Viceroy to quell their rebellion. The name
#  Śavasa or Śvasa seems to be preserved in the modern name 
#  Chhibha comprising Punch, Rajauri and Bhimbhara. - VS Agarwala Ch II, Sec 4.""",
#     )
xatra.Flag(label="UḌḌIYĀNA", value=UDDIYANA)
xatra.Flag(label="DARADA", value=DARADA)
xatra.Flag(label="MARASA", value=LADAKH)
xatra.Flag(label="GEDROSIA", value=BALOCH)
xatra.Flag(label="KAMBOJA", value=KAMBOJA)
xatra.Flag(label="MERU", value=MERU)
xatra.Flag(label="ZARANJ", value=ZARANJ)
xatra.Flag(label="KANDAHAR", value=KANDAHAR)
xatra.Flag(label="HERAT", value=HERAT)
xatra.Flag(label="ROHITAGIRI", value=ROHITAGIRI)
xatra.Flag(label="PAKTHA", value=PAKTHA)
xatra.Flag(label="BAHLIKA", value=BACTRIA)
xatra.Flag(label="MARGUS", value=MARGIANA)
xatra.Flag(label="SOGD", value=SOGDIA_PROPER)
xatra.Flag(label="PRAKAṆVA", value=FERGHANA)
xatra.Flag(label="KHWAREZM", value=KHWAREZM)
xatra.Flag(label="KASHGAR", value=KASHGAR)
xatra.Flag(label="KHOTAN", value=KHOTAN)
xatra.Flag(label="AGNI", value=AGNI)
xatra.Flag(label="AKSU", value=AKSU)
xatra.Flag(label="KUCHA", value=KUCHA)
xatra.Flag(label="ROURAN", value=ROURAN)
xatra.Flag(label="QIEMO", value=QIEMO)
xatra.Flag(label="KORLA", value=KORLA)
xatra.Flag(label="TURFAN", value=TURFAN)
xatra.Flag(label="BHOṬA", value=TIBET)
xatra.Flag(label="YYY_HIMALAYAN", classes="wild-tracts", value=HIMALAYAN)
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
    Nations, not states, of the Overland Silk Road in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    xatra.show(out_json="../maps/nations_silkroad_overland.json", out_html="../maps/nations_silkroad_overland.html")

