"""A map of _Nations_ (not states) of the overland Silk Road in 
the ancient period. Can be regarded as a first-order approximation,
roughly valid in the period between 800 BC and 800 AD."""

import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap
import maps.base_options

def add_flags(map: xatra.Map):
    map.Flag(label="VṚJISTHĀNA", value=VRJISTHANA, note="Vijayendra Kumar Mathur (1969), Aitihasik Sthanavali p 870: वृजिस्थान नामक एक ऐतिहासिक स्थान का उल्लेख प्रसिद्ध चीनी यात्री युवानच्वांग ने 'फो-लि शतंगना' नाम से किया है। सम्भवत: यह वर्तमान वज़ीरस्तान (पाकिस्तान) है।")
    map.Flag(label="VARNU", value=VARNU)
    map.Flag(label="VANAVYA", value=VANAVYA)
    map.Flag(label="APRĪTA", value=APRITA, note="or Trīrāvatīka, modern Tirāh.")
    map.Flag(label="SATTAGYDIA?", value=PSEUDOSATTAGYDIA_S, classes="names-unknown")
    map.Flag(label="KAMBOJA", value=KAMBOJA)
    map.Flag(label="KĀPIŚĀYANA", value=KAPISAYANA)
    map.Flag(label="TRYAKŚYĀYAṆA", value=TRYAKSYAYANA, note = "or Dvīrāvatika, modern Dir; or Madhumant, modern Mohmand.")
    map.Flag(
        label="AŚVAKĀYANA",
        value=ASVAKAYANA,
        note="The Hastināyanas may have have been cognate with the Aśvakāyanas, or ruled the region around Puṣkalāvatī.",
    )
    map.Flag(label="AŚVĀYANA", value=ASVAYANA)
    map.Flag(label="NIGRAHĀRA", value=NIGRAHARA)
    map.Flag(label="URAŚĀ", value=URASA, note="Hazara")
#     map.Flag(
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
    map.Flag(label="UḌḌIYĀNA", value=UDDIYANA)
    map.Flag(label="DARADA", value=DARADA)
    map.Flag(label="MARASA", value=LADAKH)
    map.Flag(label="GEDROSIA", value=BALOCH)
    map.Flag(label="KAMBOJA", value=KAMBOJA)
    map.Flag(label="MERU", value=MERU)
    map.Flag(label="ZARANJ", value=ZARANJ)
    map.Flag(label="KANDAHAR", value=KANDAHAR)
    map.Flag(label="HERAT", value=HERAT)
    map.Flag(label="ROHITAGIRI", value=ROHITAGIRI)
    map.Flag(label="PAKTHA", value=PAKTHA)
    map.Flag(label="BAHLIKA", value=BACTRIA)
    map.Flag(label="MARGUS", value=MARGIANA)
    map.Flag(label="SOGD", value=SOGDIA_PROPER)
    map.Flag(label="PRAKAṆVA", value=FERGHANA)
    map.Flag(label="KHWAREZM", value=KHWAREZM)
    map.Flag(label="KASHGAR", value=KASHGAR)
    map.Flag(label="KHOTAN", value=KHOTAN)
    map.Flag(label="AGNI", value=AGNI)
    map.Flag(label="AKSU", value=AKSU)
    map.Flag(label="KUCHA", value=KUCHA)
    map.Flag(label="ROURAN", value=ROURAN)
    map.Flag(label="QIEMO", value=QIEMO)
    map.Flag(label="KORLA", value=KORLA)
    map.Flag(label="TURFAN", value=TURFAN)
    map.Flag(label="BHOṬA", value=TIBET)
    map.Flag(label="YYY_HIMALAYAN", classes="wild-tracts", value=HIMALAYAN)
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
    Nations, not states, of the Overland Silk Road in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    """)
    map.show(out_json="../maps/nations_silkroad_overland.json", out_html="../maps/nations_silkroad_overland.html")

