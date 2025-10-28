"""Map of the North-West c. 4th century BC according to Pāṇiṇi (SS: VS Agarwala)"""

from matplotlib.colors import LinearSegmentedColormap
import xatra
from xatra import Icon
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
import maps.rivers.rivers_saptasindhu
import maps.rivers.rivers_silkrd
import maps.base_options

MOUNTAIN_ICON = Icon.geometric("triangle", color="#964B00", size=15)


def add_flags(map: xatra.Map):
    map.Flag(label="PRAKAṆVA", value=FERGHANA)
    map.Flag(label="VṚKA", value=HYRCANIA)
    map.Flag(label="PĀRTHAVA", value=PARTHIA)
    map.Flag(label="PĀRŚAVA", value=PERSIA, note="V.S. Agarwala Ch VII, Sec 8 p 446.")
    map.Flag(label="DĀMANI", value=DAMANI, note="V.S. Agarwala Ch VII, Sec 8 p 444.")
    map.Flag(label="HĀRAHŪRAKA", value=KANDAHAR, note="""
Its own native place is the commentary on such of its various forms iis Kāpīśāyana
 and Hārahūraka: (Arth. Trans. p. 145; Text. II.25). Obviously there were two varieties
 of the grape wine, the Kāpīśāyana produced in the region round Kāpīśī in north
 Afghanistan, and Hārahūraka in the south in the valley of
 the Harahvaiti or Arghandab.* The black raisins are still
 called harahūra, and it is possible that the Kāpīśāyana or
 northern variety of wine was made from green and the
 Hārahūraka or Kandhar wine from black grapes.
 - V.S. Agarwala Ch III Sec 6 p 117.
""")
    map.Flag(label="SĀRAVA", value=HERAT, note="""
It may be noted that Sarayu was also the name of a river in remote Rigvedic India
 flowing past Herat (derived from Hari-Rud; cf. Old-Persian
 Harayu from Vedic Sarayu). Darius I (516 B.C.) in his inscription mentions Haraiva,
 the people of Harayū, equal to Pāṇini’s Sārava. In the Elamite version of the Behistun
 inscription occurs the name Arriya (=Haraiva=Gk. Aria with its capital at Herat).
""")
    map.Flag(label="BĀLHĪKA", value=BACTRIA)
    map.Flag(label="ANDHAKAVARTA", value=ANDHAKAVARTA, note="V.S. Agarwala Ch VII Sec 7 p 435.")
    map.Flag(label="ROHITAGIRI", value=ROHITAGIRI)
    map.Flag(label="PAKTHA", value=PAKTHA)
    map.Flag(label="DVYAKṢĀYAṆA", value=AFG_MERU)
    map.Flag(label="UḌḌIYĀNA", value=UDDIYANA)
    map.Flag(label="APRĪTA", value=APRITA, note="or Trīrāvatīka, modern Tirāh. Modern Afridis.")
    map.Flag(label="KĀPIŚĀYANA", value=KAPISAYANA)
    map.Flag(label="TRYAKŚYĀYAṆA", value=TRYAKSYAYANA, note = "or Dvīrāvatika, modern Dir; or Madhumant, modern Mohmand.")
    map.Flag(label="KAMBOJA", value=KAMBOJA, note="Kamboja is usually associated with Kabul, but Pāṇini has associated it with the Meru (Pamir) mountains.")
    map.Flag(
        label="AŚVAKĀYANA",
        value=ASVAKAYANA,
        note="The Hastināyanas ruled the region around Puṣkalāvatī.",
    )
    map.Flag(label="MĀLĀVAT", value=gadm("PAK.5.6.3"), note="""VS Agarwala Ch II Sec 3 p 41: Patāñjali gives several new names of mountain-dwellers, of
 which Mālāvat (II.287) is noteworthy as corresponding to 
 Mallkand, the mountainous district north of Dargai, the home 
 of the Dargalas in the country south of the Swat river. """)
    map.Flag(label="AŚVĀYANA", value=ASVAYANA)
    map.Flag(label="NIGRAHĀRA", value=NIGRAHARA)
    map.Flag(
        label="DĀRADA",
        value=DARADA,
        note="Inhabited by Dardic peoples such as the Piśācas.",
    )
    map.Flag(
        label="KAMBOJA?",
        value=TJK_MERU,
        note="Kamboja is usually associated with Kabul, but Pāṇini has associated it with the Meru (Pamir) mountains.",
    )
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
    map.Flag(label="GLAUCUKAYĀNAKA", value=GLAUCUKAYANAKA, note ="""
The free clan called the Glaukanikoi (identical with the Glaucukāyanakas of the
 Kaśikā on Panini IV.3.99) whose country lay in the fertile and populous regions
 lying in the south of Kaśmīr (the Bhimber and Rajauri districts) between the upper courses of
 the Jhelum and the Chenab and the Ravi, had as many as thirty-seven cities, the smallest
 of which contained not fewer than 5,000 inhabitants, while many contained upwards of
 10,000. - VS Agarwala Ch II, Sec 5 p 73. The Abisares of Greek record was also located here
 at the same location, which is a bit odd.
""")
    map.Flag(label="KAŚMĪRA", value=KASHMIR)
    map.Flag(label="GANDHĀRA", value=GANDHARA, note="perhaps the Hastināyanas, i.e. an elephant-expedition force, ruled here.")
    map.Flag(label="VṚJISTHĀNA", value=VRJISTHANA, note="Vijayendra Kumar Mathur (1969), Aitihasik Sthanavali p 870: वृजिस्थान नामक एक ऐतिहासिक स्थान का उल्लेख प्रसिद्ध चीनी यात्री युवानच्वांग ने 'फो-लि शतंगना' नाम से किया है। सम्भवत: यह वर्तमान वज़ीरस्तान (पाकिस्तान) है।")
    map.Flag(label="VANAVYA", value=VANAVYA)
    map.Flag(label="VARNU", value=VARNU)
    map.Flag(label="KEKAYA", value=DOAB_IJ)
    map.Flag(
        label="SINDHU",
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
    #     map.Flag(label="AMBAṢṬHA", value=gadm("PAK.7.1.2"), note="""The Abastanoi/Sambasta of Greek accounts are mentioned to the South of the
    #  Mālavas, see e.g. <a href='https://www.ibiblio.org/britishraj/Jackson2/chapter04.html'>ibiblio.org/britishraj/Jackson2/chapter04.html</a>.
    #  The
    # """)
    map.Flag(label="???", value=LAVAPURA | DOAB_RS_N - AUDUMBARA, classes="flag-grey")
    map.Flag(label="MADRAKĀRA", value=MADRAKARA)
    map.Flag(
        label="TRIGARTA",
        value=TRIGARTA,
        note="Trigarta, Audumbara, Tilakhala, Rājanya -- all ruled this region",
    )
    map.Flag(label="KUṆINDA", value=KUNINDA, note="or Kulinda, or Kālakūṭa")
    map.Flag(label="BHĀRADVAJA", value=gadm("IND.35.6"))
    map.Flag(label="RAṄKU", value=gadm("IND.35.1"))
    map.Flag(label="AUDUMBARA", value=AUDUMBARA)
    map.Flag(label="TILAKHALA", value=TILAKHALA)
    map.Flag(label="RĀJANYA", value=RAJANYA)
    map.Flag(label="KURUKṢETRA", value=KURU_KSETRA_GREATER)
    map.Flag(label="KURUJANGALA", value=KURU_JANGALA)
    map.Flag(label="YAUDHEYA", value=YAUDHEYA)
    map.Flag(
        label="PĀRASKARA",
        value=YYY_MARU,
        classes="flag-grey",
        note="""Pāraskara (VI.1.157). Tliis is mentioned in the gaṇa Pāraskara-prabhṛti.
 Patañjali treats it as a country (Pāraskara deśaḥ, III.96). The name corresponds 
 to Thara-Pārkara (Thara being the Sindhi form of Thala meaning dry country or desert, 
 as opposed to Kachchha or jāṅgala country), one of the biggest districts of Sindh which
 once denoted the whole of its south-eastern part up to the coast of the Great Rann
 of Kachchha or Kachchha-Iriṇa. The Ṛktantra takes the name Pāraskara as that of a mountain,
 and the term Parakara for non-mountainous region, such as the Thar-Parkar district (Pāra parvate,
 IV.5.1O, Suryakant's edition, p. 41). - VS Agarwala Ch II, Sec 4.""",
    )
    map.Flag(label="MATSYA", value=MATSYA)
    map.Flag(
        label="SĀLVA",
        value=SALVA,
        note="""
V.S. Agarwala Ch IV, Sec 3: A confederacy of tribes including Ajamīḍha, Ajakranda, Bodha, Bhūliṅga.
 V.S. Agarwala Ch II, Sec 4: Also mentioned are Sālveya (=Sālvaputra=Sālveyaka), Sālvavayava. The Kāṣikā
 also describes the Udumbara, Tilakhala, Yugandhara, Śaradaṇḍa and Madrakāra as being Sālva tribes.
""",
    )
    map.Flag(label="SAUVIRA", value=SINDH)
    map.Flag(label="MASURAKARṆA", value=MASURAKARNA)
    map.Flag(label="MUCUKARṆA", value=MUCUKARNA)
    map.Flag(label="BRĀHMAṆAKA", value=BRAHMANAKA)
    map.Flag(label="INDRAVAKTRA", value=INDRAVAKTRA, note="V.S. Agarwala Ch 2, Sec 5 p 65-66. Inhabited by Kitavāḥ, Pāradāḥ, Vairāmāḥ peoples.")
    map.Flag(label="SINDHUVAKTRA", value=SINDHUVAKTRA, note="V.S. Agarwala Ch 2, Sec 5 p 65-66.")
    map.Flag(label="PĀRDĀYANA", value=PARDAYANA, note="V.S. Agarwala Ch 2, Sec 5 p 65-66. Vārteyas also dwelled here (V.S. Agarwala Ch VII Sec 8 p 450).")
    map.Flag(label="ĀRABHAṬA", value=ARABHATA, note="V.S. Agarwala Ch 2, Sec 5 p 65-66.")
    map.Flag(label="AGNI", value=KUTCH, note="Kaccha. Vibhujāgni = Great Rann of Kutch; Kāṇḍāgni = Little Rann of Kutch. V.S. Agarwala Ch 2, Sec 5 p 65-66.")
    map.Flag(label="SURĀṢṬRA", value=SURASTRA, note="Dāru-kaccha.")
    map.Flag(label="PIPPALĪKACCHA", value=LATA, note="Lata")
    map.Flag(label="ANARTA", value=ANARTA)
    # Glausai, Kathaioi. Phegus, Adrestians

    map.Point(label="Takṣaśilā", position=[33.7519137, 72.7970137])
    map.Point(label="Aṭaka", position=[33.7738058, 72.3291857])
    map.Point(
        label="Puṣkalāvatī",
        position=[34.1682553, 71.7066247],
        note="The Hastināyanas may have ruled this region; or they may have been cognate with the Aśvakāyanas.",
    )
    map.Point(label="Śalātura", position=[34.0484722, 72.3630084])
    map.Point(label="Kapiśi", position=[34.9446078, 69.2316018])
    map.Point(label="Bamiyan", position=[34.8128, 67.7801507])
    map.Point(label="Varaṇā", position=[34.8338387, 72.8750666], note="Aornos")
    map.Point(label="Maśakāvatī", position=[34.6468965, 72.0200283], note="Massaga")
    map.Point(label="Dvārka", position=[38.1856541, 70.6029253])
    map.Point(label="Mauñjāyana", position=[36.0197222, 70.771314])
    map.Point(label="Apakara", position=[31.6257828, 71.0385037])
    map.Point(label="Śākala", position=[32.4833721, 74.4599975], note='V.S. Agarwala Ch II, Sec 5 p 72 locates Śāṅgala and the Kaṭhas to be in Jhang district in Uśīnara, and distinct from Śākala; but this seems to no longer be the view.')
    map.Point(label="Cakravāla", position=[32.9306578, 72.7654423])
    map.Point(label="Śibipura", position=[30.8331294, 72.0653991])
    map.Point(label="Barbara", position=[24.7538782, 67.5180803])
    map.Point(label="Pāṭanaprastha", position=[32.2703182, 75.6312559])
    map.Point(label="Campa", position=[32.5473465, 76.1106229])
    map.Point(label="Gabḍikā", position=[32.4428475, 76.513443])
    map.Point(label="Kuluṭa", position=[31.9545839, 77.0906928])
    map.Point(label="Udbhāṇḍa", position=[33.8968548,72.2461023], note="""On this route lay the town called Udbhāṇḍa (Ohind) as the
 destination where the merchandise was unloaded for transhipment across the Indus. - V.S. Agarwala Ch IV, Sec 6 p 245.""")
    map.Point(label="Maṇḍāmatī", position=[31.7094582, 76.9201538])
    map.Point(label="Phalakapura", position=[31.0143239, 75.7758086])
    map.Point(label="Sunetra", position=[30.8840679,75.7991748])
    map.Point(label="Yugandhara", position=[30.1585396, 77.2786509])
    map.Point(label="Kurukṣetra", position=[29.96928, 76.8613021])
    map.Point(label="Śairīśaka", position=[29.5369779, 74.9892074])
    map.Point(label="Kapisthala", position=[29.7918366, 76.3296551])
    map.Point(label="Aiśukāri", position=[29.1561658, 75.6731383])
    map.Point(label="Rohītakā", position=[28.8894463, 76.460445])
    map.Point(label="Roṇī", position=[29.7446626,75.195733])
    map.Point(label="Hṛḍgolīya", position=[34.3521939,70.4856822])
    map.Point(label="Andhakavarta", position=[36.95098,65.0863755])
    map.Point(label="Naḍvala", position=[25.3762851,73.4335213])
    map.Point(label="Aśani", position=[34.0821216,70.6623351], note="""
e.g, Asani (Parśvādi group, V.3.117) perhaps, Shinwāris with their parent-stock of the Kārshbuns, to be identified 
 with Kārśāpaṇas in the same gaṇa. - V.S. Agarwala CH VII Sec 7 p 438.
""")
    map.Point(label="Bālhīka", position=[36.7571227,66.8740582])
    map.Point(label="Rohitagiri", position=[33.9434, 66.2476], icon=MOUNTAIN_ICON, note="Roha is an old name for Afghanistan. See V.S. Agarwala Ch VII, Sec 7, p 435.")
    map.Point(label="Añjanāgiri", position=[30.4999991,70.156367], icon=MOUNTAIN_ICON, note="or Trikakut, or Suleiman mountains. See V.S. Agarwala Ch II, Sec 3 p 39.")
    map.Point(label="Salt Range", position=[32.3289,72.2186], icon=MOUNTAIN_ICON)
    map.Point(label="Kiṃśulkāgiri", position=[27.8099,64.4678], icon=MOUNTAIN_ICON, note = "Or Hiṅgulā in Prakrit.")
    map.Point(label="Vidura", position=[32.4032679,74.7789954], icon=MOUNTAIN_ICON, note="""VS Agarwala Ch II, Sec 3 p 39:
 Pāṇini mentions some particular hills: (1) Tri-kakut 
 (V.4.147) so-called from its three peaks, a name first used in
 the Atharvaveda as the source of a salve (añjana), which may
 he identified with the Sulaiman mountain, famous as the source
 of antimony all over the Punjab and Sind (probably same as
 Sauvirāñjana; cf. Vedic Index I.329; (2) Vidura (IV.3.84)
 as the source of the precious stone called vaidūrya (cat’s eye/lapis lazuli),
 which according to Patanjali was quarried at Vālavaya and
 treated by the lapidaries in Vidura, probably Bidar (cf. Pargiter,
 Mārk. p. 365, for Vaidurya as Satpura); (3) Kiṃśulakā-giri
 (VI.3.117), to which the Gaṇapāṭha adds five more names, viz.,
 Śālvakāgiri, Añjanāgiri, Bhañjanāgiri, Lohitāgiri, Kukkuṭāgiri, 

These six names seem to be taken from some Bhuvankosha list, giving in order the ranges on the western frontiers from Afghanistan to Baluchistan.
 """)
    map.Point(label="Śālvakāgiri", position=[25.9999992,66.1397003], icon=MOUNTAIN_ICON, note = "See V.S. Agarwala Ch II, Sec 3 p 39-40.")
    map.Point(label="Bhañjanāgiri", position=[34.6336391,67.8086473], icon=MOUNTAIN_ICON, note="See V.S. Agarwala Ch II, Sec 3 p 39-40. Koh-i-Baba.")
    map.Point(label="Kukkuṭagiri", position=[34.0345,64.7754], icon=MOUNTAIN_ICON, note="See V.S. Agarwala Ch II, Sec 3 p 39-40.")
    map.Point(label="Dāmani", position=[29.5105547,64.2410892], icon =MOUNTAIN_ICON, note="Chagai hills.")
    map.Point(label="Anusamudradvīpa", position=[20.7246,70.9161])
    map.Point(
        label="Bahugarta",
        position=[22.6647,72.4933],
        note="Sabarmati river valley. V.S. Agarwala Ch II, śec 5 p 66."
    )
    map.Point(
        label="Cakragarta",
        position=[22.0834769,69.2641703]
    )
    map.Point(label="Haṃsamārga", position=[36.3103036,74.6081449])
    # map.Point(label="Ajamīḍha, Ajakranda?", position=[26.0963, 74.9048], note="")
    map.Point(
        label="Mṛttikāvatī",
        position=[26.65, 74.0307251],
        note="V.S. Agarwala Ch IV, Sec 3. Mṛttikāvatī is a Sālva capital; it might be Merta, though this is outside Sālva territory proper as identified (the region from North Bikaner to Alwar).",
    )
    map.Point(label="Śārkara", position=[27.7176044, 68.7924545])
    map.Point(label="Rauruka", position=[27.6728038, 68.8718273])
    map.Point(
        label="Brāhmaṇaka",
        position=[25.8801594, 68.7673041],
        note="""
It is mentioned in Paniru's sūtra V. 2.71. Patañjali definitely calls it a janapada (Brāhmaṇako
 nama janapadaḥ II.298). The significance of its name is brought out by the Kāśikā, which describes
 it as the land of Brahmins who were āyudhajīvins or followers of military art.
 (yatrāyudhajīvino Brāhmaṇāḥ santi), Their military traditions continued up to the time of Alexander
 whose invasion they resisted with patriotic heroism (Plutarch, Alex., 59) . The Greeks call them
 Brachmanoi and locate them in middle Sind (Arrian, VI.I6), of which the capital is still called
 Brahmanabad (Cunningham, Ancient Geog., p. 310). It may be noted that even Rajasekhara (9th century A. D.)
 names Brāhmaṇavaha ('abode of Brāhmaṇas') as one of the janapadas of the west. The Muslim geographers called
 Bahmanwā after this old tradition. - VS Agarwala Ch II, Sec 4.""",
    )

    map.Text(
        label="Ambaṣṭha",
        position=[29.2576, 71.0651],
        classes="uncertain-label uncertain-label-ambastha",
        note="""The cognate Abastanoi/Sambasta of Greek accounts are mentioned to the South of the
 Mālavas, see e.g. <a href='https://www.ibiblio.org/britishraj/Jackson2/chapter04.html'>ibiblio.org/britishraj/Jackson2/chapter04.html</a>.
 The Vasāti are also mentioned in the same region, see V.S. Agarwala Ch VII, Sec 8 p 453.
""",
    )
    map.Text(
        label="Śaubhreya?",
        position=[30.1404, 71.3068],
        classes="uncertain-label uncertain-label-saubreya",
        note="""V.S. Agarwala Ch VII, Sec 8 p 449. "On both banks of the river."
""",
    )
    map.Text(
        label="Śaubhreya?",
        position=[28.6906,70.0928],
        classes="uncertain-label uncertain-label-saubreya-2",
        note="""V.S. Agarwala Ch VII, Sec 8 p 449. "On both banks of the river."
""",
    )
    map.Text(
        label="Vasāti?",
        position=[29.8502, 67.9504],
        note="Ossadioi of Greek accounts. Shown here in VS Agarwala's final map."
    )
    map.Text(
        label="Śaudrāyaṇa?",
        position=[28.2076,69.8126],
        classes="uncertain-label uncertain-label-saudrayana",
        note="Diodorous couples the Sodrae with Massane as occupying the opposite banks of the Indus . Cunningham equates the Massane with the Mausarnaioi of Ptolemy, which name corresponds to the Masuurakarna of the Gana Patha II-4-49, IV-1-112."
    )
    map.Text(
        label="Saubhuta",
        position=[31.9055,71.9165],
        classes="uncertain-label uncertain-label-saubhuti",
        note='V.S. Agarwala Ch II, Sec 5 p 72. "Saubhuta was thus a part of Kekaya in the Salt Range."'
    )
    map.Text(
        label="Kaṭha",
        position=[32.3892,74.4324],
        classes="uncertain-label uncertain-label-katha",
        note='V.S. Agarwala Ch II, Sec 5 p 72 locates Śāṅgala and the Kaṭhas to be in Jhang district in Uśīnara, and distinct from Śākala; but this seems to no longer be the view.'
    )

    map.CSS(r"""
    .uncertain-label { font-size: 12px; color: #444;}
    .flag-grey { fill: #888888 !important; color: grey !important; fill-opacity: 0.25 !important; }
    """)


if __name__ == "__main__":
    map = xatra.Map()
    maps.base_options.add_flags(map)
    add_flags(map)
    maps.rivers.rivers_saptasindhu.add_flags(map)
    map.River(label="Kubha", value=overpass("1676476"), note="Kabul")
    map.River(label="Kāma", value=overpass("6608825"), note="Kunar")
    map.River(label="Vaksu (amu darya)", value=overpass("223008"), show_label=True)

    map.CSS(r"""
        .admin { opacity: 0.35; }
        .flag-grey { fill: #888888 !important; color: grey !important; }
    """)
    map.zoom(6)
    map.TitleBox("""
    Map of the Audicya (northern) country c. 4th century BC according to Pāṇiṇi (SS: VS Agarwala)
    """)
    map.show(out_json="../maps/nw_panini.json", out_html="../maps/nw_panini.html")
