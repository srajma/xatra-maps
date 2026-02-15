"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence

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
xatra.Flag(
    label="ŚAVASA",
    value=SAVASA,
    note="""Of these Kekaya and Savasa may be
located between the Jhelum and the Chenab, the first in the
south and the second in the north respectively, and Madra and
Uśīnara between the Chenab and the Ravi in the north and
south respectively. The divisions become clear on the xatra.
The Divyāvadāna refers to the Śvasas in Uttarāpatha with
headquarters at Takṣaśilā to which Aśoka was deputed by his
father Bindusāra as Viceroy to quell their rebellion. The name
Śavasa or Śvasa seems to be preserved in the modern name 
Chhibha comprising Punch, Rajauri and Bhimbhara. - VS Agarwala Ch II, Sec 4.""",
)
xatra.Flag(label="UḌḌIYĀNA", value=UDDIYANA)
xatra.Flag(label="DARADA", value=DARADA)


xatra.Flag(label="KASHMIR", value=KASHMIR)
xatra.Flag(label="JAMMU", value=JAMMU)
# xatra.Flag(label="POJK", value=POJK)
xatra.Flag(label="KASHMIR", value= KASHMIR)
xatra.Flag(label="JAMMU", value= JAMMU)
xatra.Flag(label="GANDHĀRA", value=GANDHARA)
xatra.Flag(label="KEKAYA", value=DOAB_IJ)
xatra.Flag(
    label="SINDHU (PJ)",
    value=PAK_THALL,
    note=""""Sindhu as a janapada may be identified with Sind-Sāgar Doāb,
the region between the Jhelum and the Indus. Most of it is now the sandy desert
of Thal." (VS Agarwala Ch II, Sec 4.)""",
)
xatra.Flag(label="MADRA", value=MADRA)
xatra.Flag(
    label="UŚĪNARA",
    value=USINARA,
    note="Equivalent to Śibi/Śivi. Agalasseis of Greek accounts also dwelled somewhere here.",
)
xatra.Flag(label="MĀLAVA", value=MALAVA)
xatra.Flag(label="KṢUDRAKA", value=KSUDRAKA)
xatra.Flag(label="MADRA_EE", value=MADRA_EE, classes="names-unknown")
xatra.Flag(label="SINDHU-SAUVIRA", value=SINDH)

# xatra.Flag(label="PSEUDOSATTAGYDIA", value=PSEUDOSATTAGYDIA)
# xatra.Flag(label="SINDH", value=SINDH)
# xatra.Flag(label="GANDHARA_W", value=GANDHARA_W)
# xatra.Flag(label="DOAB_IJ_N", value=DOAB_IJ_N)
# xatra.Flag(label="DOAB_IJ_S", value=DOAB_IJ_S)
# xatra.Flag(label="DOAB_JC", value=DOAB_JC)
# xatra.Flag(label="DOAB_CR", value=DOAB_CR)
# xatra.Flag(label="DOAB_RS_N", value=DOAB_RS_N)
# xatra.Flag(label="DOAB_RS_C", value=DOAB_RS_C)
# xatra.Flag(label="DOAB_RS_S", value=DOAB_RS_S)

xatra.Flag(label="TRIGARTA", value=TRIGARTA)
xatra.Flag(label="KUNINDA", value=KUNINDA)
xatra.Flag(label="BHĀRADVAJA", value=gadm("IND.35.6"))
xatra.Flag(label="AUDUMBARA", value=AUDUMBARA)
xatra.Flag(label="GABDIKA", value=GABDIKA)
xatra.Flag(label="YAKRLOMAN", value=YAKRLOMAN)
xatra.Flag(label="TILAKHALA", value=TILAKHALA)
xatra.Flag(label="RĀJANYA", value=RAJANYA)
xatra.Flag(label="KUTCH", value=KUTCH)
xatra.Flag(label="SURASTRA", value=SURASTRA)
xatra.Flag(label="ANARTA", value=ANARTA)
xatra.Flag(label="LATA", value=LATA)
xatra.Flag(label="KUKURA", value=KUKURA)
xatra.Flag(label="MATSYA", value=MATSYA)
xatra.Flag(label="BRAHMAVARTA", value=BRAHMAVARTA)
xatra.Flag(label="KURU_PROPER", value=KURU_PROPER)
xatra.Flag(label="KURUKSETRA", value=KURU_KSETRA_GREATER)
xatra.Flag(label="JANGALA", value=JANGALA)
xatra.Flag(label="PANCALA_N", value=PANCALA_N)
xatra.Flag(label="PANCALA_S", value=PANCALA_S)
xatra.Flag(label="SURASENA", value=SURASENA)
xatra.Flag(label="VATSA", value=VATSA)
xatra.Flag(label="KOSALA", value=KOSALA)
xatra.Flag(label="KASI", value=KASI)
xatra.Flag(label="MALLA", value=MALLA)
xatra.Flag(label="VIDEHA", value=VIDEHA)
xatra.Flag(label="SAKYA", value=SAKYA)
xatra.Flag(label="LICCHAVI", value=LICCHAVI)
xatra.Flag(label="MAGADHA", value=MAGADHA)
xatra.Flag(label="TERAI", value=TERAI)
xatra.Flag(label="AVANTI", value=AVANTI)
xatra.Flag(label="AKARA", value=AKARA)
xatra.Flag(label="KUNTI", value=DASARNA, note="Kunti = Dāśārṇa")
xatra.Flag(label="CINTI", value=CEDI, note="Cinti = Cedi")
xatra.Flag(label="PULINDA", value=PULINDA)
xatra.Flag(label="ANGA", value=ANGA)
xatra.Flag(label="GAUDA", value=GAUDA)
xatra.Flag(label="RADHA", value=RADHA)
xatra.Flag(label="SUHMA", value=SUHMA)
xatra.Flag(label="PUNDRA", value=PUNDRA)
xatra.Flag(label="VANGA", value=VANGA)
xatra.Flag(label="SAMATATA", value=SAMATATA)
xatra.Flag(label="LAUHITYA", value=LAUHITYA)
xatra.Flag(label="UTKALA", value=UTKALA)
xatra.Flag(label="KALINGA", value=KALINGA)
xatra.Flag(label="VIDARBHA", value=VIDARBHA)
xatra.Flag(label="RSIKA", value=RSIKA)
xatra.Flag(label="MULAKA", value=MULAKA)
xatra.Flag(label="ASMAKA", value=ASMAKA)
xatra.Flag(label="APARANTA", value=APARANTA)
xatra.Flag(label="KUNTALA", value=KUNTALA)
xatra.Flag(label="KADAMBA", value=KADAMBA)
xatra.Flag(label="GANGA", value=CAUVERIC)
xatra.Flag(label="MAHISAKA", value=MAHISAKA)
xatra.Flag(label="TELINGA", value=VENGI)
xatra.Flag(label="ALUPA", value=TULU)
xatra.Flag(label="CERA", value=CERA)
xatra.Flag(label="AY", value=AY)
xatra.Flag(label="EZHIMALA", value=EZHIMALA)
xatra.Flag(label="KANCI", value=KANCI)
xatra.Flag(label="COLA", value=COLA)
xatra.Flag(label="PANDYA", value=PANDYA)
xatra.Flag(label="KONGU", value=KONGU)
xatra.Flag(label="SIMHALA", value=SIMHALA)
xatra.Flag(label="COORG", value=COORG)
xatra.Flag(label="DANDAKARANYA", classes="wild-tracts", value=GREAT_FOREST)
xatra.Flag(label="KALAKAVANA", classes="wild-tracts", value=UP_KALAKAVANA)
xatra.Flag(label="MARU", classes="wild-tracts", value=RJ_MARU)
xatra.Flag(label="NAIMISA", classes="wild-tracts", value=UP_NAIMISA)
xatra.Flag(label="BAYALU", classes="names-unknown", value=BAYALU)
xatra.Flag(label="PUNE", classes="names-unknown", value=GREATER_PUNE)
xatra.Flag(label="HADOTI", classes="names-unknown", value=HADOTI)
xatra.Flag(label="BIHAR_NE", classes="names-unknown", value=BIHAR_NORTHEAST)
xatra.Flag(label="BAHAWALPUR", classes="names-unknown", value=BAHAWALPUR)
xatra.CSS(r"""
.names-unknown {fill: #444444; color: #444444 !important;}
.wild-tracts {fill: #888888; color: #888888 !important;}
.flag-label {font-size: 10px}
.path-label {font-size: 10px}
.river-label {font-size: 10px}
"""
)

if __name__ == "__main__":
    import maps.rivers.rivers_gangetic
    import maps.rivers.rivers_peninsular
    import maps.rivers.rivers_saptasindhu
    import maps.base_options

    xatra.TitleBox("""
    Nations, not states, of the Indian core in antiquity. 
    Roughly valid in the period 800 BC to 1200, think of it as a 
    first-order approximation or a reference guide. 
    <br>
    Light grey are wild tracts, dark grey are regions whose names
    in that time are unknown to me.
    <br>
    """)
    xatra.show(out_json="../maps/nations_india.json", out_html="../maps/nations_india.html")

