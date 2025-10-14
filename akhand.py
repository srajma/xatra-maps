from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
import rivers_gangetic
import rivers_peninsular
import rivers_saptasindhu
import rivers_silkrd

FUNDAMENTAL_COLONIES = SEA | NEI_HIM | TARIM | SOCOTRA
BRIEF_COLONIES = (
    BALOCH
    | KANDAHAR
    | ZARANJ
    | AFG_MISC
    | KAMBOJA
    | BACTRIA
    | MARGIANA
    | SOGDIA
    | MERU
    | MONGOLIA
    | MITANNI
    | ARMENIA
)
FUNDAMENTAL_HB = TIBET | JAPAN | KOREA
DEEP_INFLUENCE = CHINA_PROPER | MANCHURIA | BUDDHIST_RUSSIA | NORTH_VIETNAM
EXPLORED = (MEDITERRANEAN_EAST | AFRICA_EAST_SPOTTY | GULF | LEVANT | IRANIC) - (
    DEEP_INFLUENCE
    | FUNDAMENTAL_HB
    | BRIEF_COLONIES
    | FUNDAMENTAL_COLONIES
    | SUBCONTINENT_PROPER
)

if __name__ == "__main__":
    map = xatra.Map()
    map.BaseOption("OpenStreetMap", default=True)
    map.BaseOption("Esri.WorldImagery")
    map.BaseOption("OpenTopoMap")
    map.BaseOption("Esri.WorldPhysical")
    map.Flag(label="INDIAN CORE", value=SUBCONTINENT_PROPER, classes="indian-core")
    map.Flag(
        label="FUNDAMENTAL COLONIES",
        value=FUNDAMENTAL_COLONIES,
        classes="fundamental-colonies",
    )
    map.Flag(label="HIMALAYAS", value=YYY_HIMALAYAN, classes="himalayas")
    map.Flag(label="BRIEF COLONIES", value=BRIEF_COLONIES, classes="brief-colonies")
    map.Flag(
        label="FUNDAMENTALLY HINDU/BUDDHIST",
        value=FUNDAMENTAL_HB,
        classes="fundamentally-hindu-buddhist",
    )
    map.Flag(label="DEEP INFLUENCE", value=DEEP_INFLUENCE, classes="deep-influence")
    map.Flag(label="RAIDED", value=PRATIHARA_RAIDS, classes="raided")
    map.Flag(label="EXPLORED", value=EXPLORED, classes="explored")
    rivers_gangetic.add_flags(map)
    rivers_peninsular.add_flags(map)
    rivers_saptasindhu.add_flags(map)
    rivers_silkrd.add_flags(map)
    map.TitleBox("""
Greater Indian Sphere.<br>
<b>Indian core</b>: India proper<br>
<b>Fundamental colonies</b>: Countries whose civilizations were fundamentally an Indian endeavour.<br>
<b>Brief colonies:</b> Countries that were ruled by an Indian for a brief period of time.<br>
<b>Fundamentally Hindu/Buddhist:</b> Countries whose civilizations were fundamentally Hindu/Buddhist, but no direct Indian rule.<br>
<b>Deep Influence:</b> Countries that were significantly influenced by Indiian religion and philosophy.<br>
<b>Raided:</b> Brief raids by Chachas and Pratiharas.<br>
<b>Explored:</b> Countries that were visited by Indians in antiquity.<br>
""")
    map.CSS(r"""
    .indian-core {fill: #740001; color: #740001 !important;}
    .fundamental-colonies {fill: #e80000; color: #e80000 !important;}
    .brief-colonies {fill: #fc4e2b; color: #fc4e2b !important;}
    .fundamentally-hindu-buddhist {fill: #f5820b; color: #f5820b !important;}
    .deep-influence {fill: #a425d6; color: #a425d6 !important;}
    .raided {fill: #936a27; color: #936a27 !important;}
    .explored {fill: #698db3; color: #698db3 !important;}
    .himalayas {fill: #ff0000; color: #ff0000 !important;}
    """)
    map.show(out_json="docs/akhand.json", out_html="docs/akhand.html")
