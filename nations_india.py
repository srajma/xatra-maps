"""A map of _Nations_ (not states) of India in the ancient period. 
Can be regarded as a first-order approximation, roughly valid in  
the period between 800 BC and 800 AD."""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
import rivers_gangetic
import rivers_peninsular
import rivers_saptasindhu

def add_flags(map: xatra.Map):
    map.Flag(label="KASHMIR", value=KASHMIR)
    map.Flag(label="JAMMU", value=JAMMU)
    map.Flag(label="KASHMIR_TBC", value=KASHMIR_TBC)
    map.Flag(label="VARNU", value=PSEUDOSATTAGYDIA)
    map.Flag(label="SINDH", value=SINDH)
    map.Flag(label="GANDHARA_W", value=GANDHARA_W)
    map.Flag(label="DOAB_IJ_N", value=DOAB_IJ_N)
    map.Flag(label="DOAB_IJ_S", value=DOAB_IJ_S)
    map.Flag(label="DOAB_JC", value=DOAB_JC)
    map.Flag(label="DOAB_CR", value=DOAB_CR)
    map.Flag(label="DOAB_RS_N", value=DOAB_RS_N)
    map.Flag(label="DOAB_RS_C", value=DOAB_RS_C)
    map.Flag(label="DOAB_RS_S", value=DOAB_RS_S)
    map.Flag(label="TRIGARTA", value=TRIGARTA)
    map.Flag(label="KUNINDA", value=KUNINDA)
    map.Flag(label="KUTCH", value=KUTCH)
    map.Flag(label="SURASTRA", value=SURASTRA)
    map.Flag(label="ANARTA", value=ANARTA)
    map.Flag(label="LATA", value=LATA)
    map.Flag(label="KUKURA", value=KUKURA)
    map.Flag(label="MATSYA", value=MATSYA)
    map.Flag(label="BRAHMAVARTA", value=BRAHMAVARTA)
    map.Flag(label="KURU_PROPER", value=KURU_PROPER)
    map.Flag(label="KURU_KSETRA_GREATER", value=KURU_KSETRA_GREATER)
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
    map.Flag(label="GREATER_PUNE", classes="names-unknown", value=GREATER_PUNE)
    map.Flag(label="HADOTI", classes="names-unknown", value=HADOTI)
    map.Flag(label="BIHAR_NORTHEAST", classes="names-unknown", value=BIHAR_NORTHEAST)
    map.Flag(label="BAHAWALPUR", classes="names-unknown", value=BAHAWALPUR)
    map.CSS(r"""
    .names-unknown {fill: #444444; color: #444444 !important;}
    .wild-tracts {fill: #888888; color: #888888 !important;}
    """
    )

if __name__ == "__main__":
    map = xatra.Map()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
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

