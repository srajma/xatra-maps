"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
import maps.rivers.rivers_gangetic as rivers_gangetic
import maps.rivers.rivers_peninsular as rivers_peninsular
import maps.rivers.rivers_saptasindhu as rivers_saptasindhu
import maps.base_options
def add_flags(map: xatra.Map):
    map.Flag(label="KASHMIR", value=KASHMIR)
    map.Flag(label="JAMMU", value=JAMMU)
    # map.Flag(label="POJK", value=POJK)
    map.Flag(label="KASHMIR", value= KASHMIR)
    map.Flag(label="JAMMU", value= JAMMU)
    map.Flag(label="VARNU", value=VARNU)
    map.Flag(label="VANAVYA", value=VANAVYA)
    map.Flag(label="VṚJISTHĀNA", value=VRJISTHANA, note="Vijayendra Kumar Mathur (1969), Aitihasik Sthanavali p 870: वृजिस्थान नामक एक ऐतिहासिक स्थान का उल्लेख प्रसिद्ध चीनी यात्री युवानच्वांग ने 'फो-लि शतंगना' नाम से किया है। सम्भवत: यह वर्तमान वज़ीरस्तान (पाकिस्तान) है।")
    map.Flag(label="KAMBOJA", value=KAMBOJA)
    map.Flag(label="GANDHĀRA", value=GANDHARA)
    map.Flag(label="KEKAYA", value=DOAB_IJ)
    map.Flag(
        label="SINDHU (PJ)",
        value=PAK_THALL,
        note=""""Sindhu as a janapada may be identified with Sind-Sāgar Doāb,
 the region between the Jhelum and the Indus. Most of it is now the sandy desert
 of Thal." (VS Agarwala Ch II, Sec 4.)""",
    )
    map.Flag(label="MADRA", value=MADRA)
    map.Flag(
        label="UŚĪNARA",
        value=USINARA,
        note="Equivalent to Śibi/Śivi. Agalasseis of Greek accounts also dwelled somewhere here.",
    )
    map.Flag(label="MĀLAVA", value=MALAVA)
    map.Flag(label="KṢUDRAKA", value=KSUDRAKA)
    map.Flag(label="LAVAPURA?", value=LAVAPURA | DOAB_RS_N - AUDUMBARA, classes="names-unknown")
    map.Flag(label="SINDHU-SAUVIRA", value=SINDH)

    # map.Flag(label="PSEUDOSATTAGYDIA", value=PSEUDOSATTAGYDIA)
    # map.Flag(label="SINDH", value=SINDH)
    # map.Flag(label="GANDHARA_W", value=GANDHARA_W)
    # map.Flag(label="DOAB_IJ_N", value=DOAB_IJ_N)
    # map.Flag(label="DOAB_IJ_S", value=DOAB_IJ_S)
    # map.Flag(label="DOAB_JC", value=DOAB_JC)
    # map.Flag(label="DOAB_CR", value=DOAB_CR)
    # map.Flag(label="DOAB_RS_N", value=DOAB_RS_N)
    # map.Flag(label="DOAB_RS_C", value=DOAB_RS_C)
    # map.Flag(label="DOAB_RS_S", value=DOAB_RS_S)
    map.Flag(label="UḌḌIYĀNA", value=UDDIYANA)
    map.Flag(label="APRĪTA", value=APRITA, note="or Trīrāvatīka, modern Tirāh.")
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
    map.Flag(
        label="ŚAVASA",
        value=SAVASA,
        note="""Of these Kekaya and Savasa may be
 located between the Jhelum and the Chenab, the first in the
 south and the second in the north respectively, and Madra and
 Uśīnara between the Chenab and the Ravi in the north and
 south respectively. The divisions become clear on the map.
 The Divyāvadāna refers to the Śvasas in Uttarāpatha with
 headquarters at Takṣaśilā to which Aśoka was deputed by his
 father Bindusāra as Viceroy to quell their rebellion. The name
 Śavasa or Śvasa seems to be preserved in the modern name 
 Chhibha comprising Punch, Rajauri and Bhimbhara. - VS Agarwala Ch II, Sec 4.""",
    )
    map.Flag(label="SATTAGYDIA?", value=PSEUDOSATTAGYDIA_S, classes="names-unknown")

    map.Flag(label="TRIGARTA", value=TRIGARTA)
    map.Flag(label="KUNINDA", value=KUNINDA)
    map.Flag(label="BHĀRADVAJA", value=gadm("IND.35.6"))
    map.Flag(label="AUDUMBARA", value=AUDUMBARA)
    map.Flag(label="TILAKHALA", value=TILAKHALA)
    map.Flag(label="RĀJANYA", value=RAJANYA)
    map.Flag(label="KUTCH", value=KUTCH)
    map.Flag(label="SURASTRA", value=SURASTRA)
    map.Flag(label="ANARTA", value=ANARTA)
    map.Flag(label="LATA", value=LATA)
    map.Flag(label="KUKURA", value=KUKURA)
    map.Flag(label="MATSYA", value=MATSYA)
    map.Flag(label="BRAHMAVARTA", value=BRAHMAVARTA)
    map.Flag(label="KURU_PROPER", value=KURU_PROPER)
    map.Flag(label="KURUKSETRA", value=KURU_KSETRA_GREATER)
    map.Flag(label="JANGALA", value=JANGALA)
    map.Flag(label="PANCALA_N", value=PANCALA_N)
    map.Flag(label="PANCALA_S", value=PANCALA_S)
    map.Flag(label="SURASENA", value=SURASENA)
    map.Flag(label="VATSA", value=VATSA)
    map.Flag(label="KOSALA", value=KOSALA)
    map.Flag(label="KASI", value=KASI)
    map.Flag(label="MALLA", value=MALLA)
    map.Flag(label="VIDEHA", value=VIDEHA)
    map.Flag(label="SAKYA", value=SAKYA)
    map.Flag(label="LICCHAVI", value=LICCHAVI)
    map.Flag(label="MAGADHA", value=MAGADHA)
    map.Flag(label="TERAI", value=TERAI)
    map.Flag(label="AVANTI", value=AVANTI)
    map.Flag(label="AKARA", value=AKARA)
    map.Flag(label="DASARNA", value=DASARNA)
    map.Flag(label="CEDI", value=CEDI)
    map.Flag(label="PULINDA", value=PULINDA)
    map.Flag(label="ANGA", value=ANGA)
    map.Flag(label="GAUDA", value=GAUDA)
    map.Flag(label="RADHA", value=RADHA)
    map.Flag(label="SUHMA", value=SUHMA)
    map.Flag(label="PUNDRA", value=PUNDRA)
    map.Flag(label="VANGA", value=VANGA)
    map.Flag(label="SAMATATA", value=SAMATATA)
    map.Flag(label="LAUHITYA", value=LAUHITYA)
    map.Flag(label="UTKALA", value=UTKALA)
    map.Flag(label="KALINGA", value=KALINGA)
    map.Flag(label="VIDARBHA", value=VIDARBHA)
    map.Flag(label="RSIKA", value=RSIKA)
    map.Flag(label="MULAKA", value=MULAKA)
    map.Flag(label="ASMAKA", value=ASMAKA)
    map.Flag(label="APARANTA", value=APARANTA)
    map.Flag(label="KUNTALA", value=KUNTALA)
    map.Flag(label="KADAMBA", value=KADAMBA)
    map.Flag(label="GANGA", value=CAUVERIC)
    map.Flag(label="MAHISAKA", value=MAHISAKA)
    map.Flag(label="TELINGA", value=VENGI)
    map.Flag(label="ALUPA", value=TULU)
    map.Flag(label="CERA", value=CERA)
    map.Flag(label="AY", value=AY)
    map.Flag(label="EZHIMALA", value=EZHIMALA)
    map.Flag(label="KANCI", value=KANCI)
    map.Flag(label="COLA", value=COLA)
    map.Flag(label="PANDYA", value=PANDYA)
    map.Flag(label="KONGU", value=KONGU)
    map.Flag(label="SIMHALA", value=SIMHALA)
    map.Flag(label="COORG", value=COORG)
    map.Flag(label="DANDAKARANYA", classes="wild-tracts", value=GREAT_FOREST)
    map.Flag(label="KALAKAVANA", classes="wild-tracts", value=UP_KALAKAVANA)
    map.Flag(label="MARU", classes="wild-tracts", value=RJ_MARU)
    map.Flag(label="NAIMISA", classes="wild-tracts", value=UP_NAIMISA)
    map.Flag(label="BAYALU", classes="names-unknown", value=BAYALU)
    map.Flag(label="PUNE", classes="names-unknown", value=GREATER_PUNE)
    map.Flag(label="HADOTI", classes="names-unknown", value=HADOTI)
    map.Flag(label="BIHAR_NE", classes="names-unknown", value=BIHAR_NORTHEAST)
    map.Flag(label="BAHAWALPUR", classes="names-unknown", value=BAHAWALPUR)
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
    rivers_gangetic.add_flags(map)
    rivers_peninsular.add_flags(map)
    rivers_saptasindhu.add_flags(map)
    map.TitleBox("""
    Nations, not states, of the Indian core in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    <br>
    Light grey are wild tracts, dark grey are regions whose names
    in that time are unknown to me.
    <br>
    """)
    map.show(out_json="docs/nations_india.json", out_html="docs/nations_india.html")

