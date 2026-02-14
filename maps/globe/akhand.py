from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra.loaders import gadm, naturalearth
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence


FUNDAMENTAL_COLONIES = SEA | NEI_HIM | TARIM | SOCOTRA
BRIEF_COLONIES = (
    BALOCH
    | KANDAHAR
    | ZARANJ
    | AFG_MISC
    # | KAMBOJA
    # | YANA
    | BACTRIA
    # | MARGIANA
    # | SOGDIA
    | MERU
    | MONGOLIA
    | MITANNI
    | ARMENIA
)
FUNDAMENTAL_HB = TIBET | JAPAN | KOREA | SOGDIA | MARGIANA
DEEP_INFLUENCE = CHINA_PROPER | MANCHURIA | BUDDHIST_RUSSIA | NORTH_VIETNAM
EXPLORED = (MEDITERRANEAN_EAST | AFRICA_EAST_SPOTTY | GULF | LEVANT | IRANIC) - (
    DEEP_INFLUENCE
    | FUNDAMENTAL_HB
    | BRIEF_COLONIES
    | FUNDAMENTAL_COLONIES
    | SUBCONTINENT_PROPER
    | DARADA
    | KAMBOJA
    | YANA
)

xatra.Flag(label="INDIAN CORE", value=SUBCONTINENT_PROPER, classes="indian-core")
xatra.Flag(
    label="FUNDAMENTAL COLONIES",
    value=FUNDAMENTAL_COLONIES,
    classes="fundamental-colonies",
)
xatra.Flag(label="DARADA", value=DARADA, classes="borderline")
xatra.Flag(label="KAMBOJA", value = GREATER_KAMBOJA, classes="borderline")
xatra.Flag(label="HIMALAYAS", value=YYY_HIMALAYAN - BRIEF_COLONIES - DARADA - GREATER_KAMBOJA - TIBET, classes="borderline")
xatra.Flag(label="BRIEF COLONIES", value=BRIEF_COLONIES, classes="brief-colonies")
xatra.Flag(
    label="FUNDAMENTALLY HINDU/BUDDHIST",
    value=FUNDAMENTAL_HB,
    classes="fundamentally-hindu-buddhist",
)
xatra.Flag(label="DEEP INFLUENCE", value=DEEP_INFLUENCE, classes="deep-influence")
xatra.Flag(label="RAIDED", value=PRATIHARA_RAIDS, classes="raided")
xatra.Flag(label="EXPLORED", value=EXPLORED, classes="explored")
xatra.CSS(r"""
.indian-core {fill: #740001; color: #740001 !important;}
.fundamental-colonies {fill: #e80000; color: #e80000 !important;}
.brief-colonies {fill: #fc4e2b; color: #fc4e2b !important;}
.fundamentally-hindu-buddhist {fill: #f5820b; color: #f5820b !important;}
.deep-influence {fill: #a425d6; color: #a425d6 !important;}
.raided {fill: #936a27; color: #936a27 !important;}
.explored {fill: #698db3; color: #698db3 !important;}
.borderline {fill: #ff0000; color: #ff0000 !important;}
""")

if __name__ == "__main__":
    import maps.base_options
    import maps.rivers.rivers_gangetic
    import maps.rivers.rivers_peninsular
    import maps.rivers.rivers_saptasindhu
    import maps.rivers.rivers_silkrd
    xatra.TitleBox("""
Indian interactions with the world.<br>
<b>Indian core</b>: India proper<br>
<b>Fundamentally Indian</b>: Countries whose civilizations were fundamentally an Indian endeavour.<br>
<b>Brief occupation:</b> Countries that were ruled by an Indian for a brief period of time.<br>
<b>Fundamentally Hindu/Buddhist:</b> Countries whose civilizations were fundamentally Hindu/Buddhist, but no direct Indian rule.<br>
<b>Deep Influence:</b> Countries that were significantly influenced by Indiian religion and philosophy.<br>
<b>Raided:</b> Brief raids in the 7th (by Chalukyas? Or Chach of Sindh?) and 9th centuries (by the Pratiharas).<br>
<b>Explored:</b> Countries that were visited by Indians in antiquity.<br>
""")
    xatra.show(out_json="../maps/akhand.json", out_html="../maps/akhand.html")
