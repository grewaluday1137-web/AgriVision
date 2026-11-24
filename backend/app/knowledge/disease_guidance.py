from typing import Dict, Any, Optional

GUIDANCE_DATABASE: Dict[str, Dict[str, Any]] = {
    "Apple___Apple_scab": {
        "disease_key": "Apple___Apple_scab",
        "plant": "Apple",
        "disease_name": "Apple Scab",
        "is_healthy": False,
        "description": "Apple scab is a severe fungal disease caused by Venturia inaequalis affecting leaves, petioles, and fruit, leading to olive-green or dark brown velvety spots.",
        "symptoms": [
            "Olive-green to brown velvety lesions on the upper leaf surface.",
            "Yellowing and premature leaf drop.",
            "Scabby, cracked, or corky lesions on fruit reducing marketability."
        ],
        "organic_controls": [
            "Apply wettable sulfur or liquid lime sulfur during early bud break.",
            "Spray neem oil or bio-fungicides based on Bacillus subtilis.",
            "Shred and compost fallen leaves thoroughly in autumn to eliminate overwintering spores."
        ],
        "chemical_controls": [
            "Captan 50 WP or Mancozeb applied preventatively at tight cluster and pink stages.",
            "Myclobutanil or Difenoconazole for systemic curative control when symptoms emerge."
        ],
        "prevention_measures": [
            "Prune canopy regularly to increase sunlight penetration and air circulation.",
            "Plant scab-resistant cultivars such as Liberty, Enterprise, or Freedom.",
            "Avoid overhead irrigation to keep foliage dry during spring development."
        ]
    },
    "Apple___Black_rot": {
        "disease_key": "Apple___Black_rot",
        "plant": "Apple",
        "disease_name": "Black Rot",
        "is_healthy": False,
        "description": "Black rot (caused by Botryosphaeria obtusa) causes 'frog-eye' leaf spots, branch cankers, and dark mummified fruit on apple trees.",
        "symptoms": [
            "Circular purple leaf spots that enlarge into brown spots with purple margins ('frog-eye' pattern).",
            "Sunken reddish-brown cankers on twigs and limbs.",
            "Firm, leathery black rot on fruit with concentric dark rings."
        ],
        "organic_controls": [
            "Promptly prune dead wood, mummified apples, and limb cankers at least 6 inches below infected tissue.",
            "Apply copper sulfate or sulfur fungicides during dormancy.",
            "Maintain soil vitality with balanced compost to reduce tree stress."
        ],
        "chemical_controls": [
            "Thiophanate-methyl or Captan sprays applied from petal fall through harvest cover sprays.",
            "Strobilurin fungicides (e.g., Pyraclostrobin) applied during warm rainy periods."
        ],
        "prevention_measures": [
            "Sanitize pruning tools between cuts using 70% alcohol or 10% bleach solution.",
            "Remove all mummified apples from the orchard before spring bud break.",
            "Control insect pests that wound fruit and create infection entry points."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "disease_key": "Apple___Cedar_apple_rust",
        "plant": "Apple",
        "disease_name": "Cedar Apple Rust",
        "is_healthy": False,
        "description": "Cedar apple rust is a heteroecious fungus (Gymnosporangium juniperi-virginianae) that requires both apple trees and eastern red cedar/juniper to complete its two-year lifecycle.",
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surfaces appearing in late spring.",
            "Small raised black dots (pycnia) within the center of orange spots.",
            "Tube-like fungal protrusions (aecia) on leaf undersides shedding powdery orange spores."
        ],
        "organic_controls": [
            "Eradicate nearby wild juniper and red cedar hosts within a 1-mile radius where feasible.",
            "Apply sulfur or copper formulations at blossom time when spore horns are gelatinous on cedars.",
            "Hand-pick early infected leaves on backyard dwarf trees."
        ],
        "chemical_controls": [
            "Myclobutanil (Immunox) applied preventatively from pink bud until petal fall.",
            "Mancozeb or Propiconazole applied before rain events in early spring."
        ],
        "prevention_measures": [
            "Plant resistant apple varieties like Redfree, Liberty, and William's Pride.",
            "Avoid planting susceptible apple trees in close proximity to decorative juniper species.",
            "Inspect neighboring juniper trees in early spring to prune gall formations."
        ]
    },
    "Apple___healthy": {
        "disease_key": "Apple___healthy",
        "plant": "Apple",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "The apple foliage exhibits healthy, deep green pigmentation with crisp margins and active photosynthesis. No fungal, bacterial, or pest damage detected.",
        "symptoms": [
            "Uniform vibrant green coloration across upper and lower surfaces.",
            "Smooth blade texture with distinct, uninterrupted venation.",
            "Absence of chlorosis, necrosis, curling, or fungal fruiting bodies."
        ],
        "organic_controls": [
            "Continue seasonal compost tea or balanced organic foliar nutrition.",
            "Apply beneficial mycorrhizal fungi to enhance nutrient uptake."
        ],
        "chemical_controls": [
            "No chemical intervention required; preserve beneficial predatory insects."
        ],
        "prevention_measures": [
            "Maintain consistent drip irrigation and regular soil moisture checks.",
            "Monitor weekly for aphid, spider mite, and codling moth presence.",
            "Apply a preventative dormant oil spray in late winter to suppress overwintering scale insects."
        ]
    },
    "Blueberry___healthy": {
        "disease_key": "Blueberry___healthy",
        "plant": "Blueberry",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Blueberry leaves show optimal chlorophyll distribution, balanced nutrient absorption, and vigor typical of well-maintained acidic soil cultivation.",
        "symptoms": [
            "Lush green, waxy leaves with upright vigor.",
            "Normal internodal spacing and healthy shoot development.",
            "Free from rust, mummy berry signs, or iron chlorosis."
        ],
        "organic_controls": [
            "Maintain pine bark or sawdust mulch layer (2-3 inches) to preserve soil moisture and organic acidity."
        ],
        "chemical_controls": [
            "No chemical fungicides necessary."
        ],
        "prevention_measures": [
            "Regularly monitor soil pH, keeping it strictly between 4.5 and 5.2.",
            "Ensure excellent drainage as blueberries are susceptible to Phytophthora root rot in standing water."
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "disease_key": "Cherry_(including_sour)___Powdery_mildew",
        "plant": "Cherry",
        "disease_name": "Powdery Mildew",
        "is_healthy": False,
        "description": "Podosphaera clandestina causes powdery mildew on cherries, forming conspicuous white powdery fungal mycelium on leaves and green fruit stems.",
        "symptoms": [
            "White to grayish powdery coating on the undersides of young leaves.",
            "Leaf distortion, curling, and crinkling along margins.",
            "Retarded shoot growth and potential blemishes on immature cherry fruit."
        ],
        "organic_controls": [
            "Spray potassium bicarbonate (e.g., MilStop) or horticultural sulfur.",
            "Apply diluted milk spray (40% milk, 60% water) on sunny days to trigger antiseptic photochemical reactions.",
            "Use neem oil or jojoba oil emulsions to coat foliage and kill fungal spores."
        ],
        "chemical_controls": [
            "Apply Quinoxyfen, Fluopyram, or Tebuconazole rotated to prevent resistance.",
            "Start sprays at shuck fall and repeat every 10–14 days through harvest if conditions are humid."
        ],
        "prevention_measures": [
            "Prune inner canopy to maintain high airflow and dry foliage.",
            "Avoid excessive nitrogen fertilization that produces flush, succulent, mildew-susceptible growth.",
            "Water trees at the root base using micro-sprinklers rather than overhead guns."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "disease_key": "Cherry_(including_sour)___healthy",
        "plant": "Cherry",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "The cherry foliage is healthy, vibrant, and robust with no signs of fungal leaf spot, powdery mildew, or bacterial canker.",
        "symptoms": [
            "Smooth, lustrous green leaves with defined serrated borders.",
            "Vigorous shoot growth and clean bark integrity.",
            "Absence of 'shot-hole' perforations or powdery fungal patches."
        ],
        "organic_controls": [
            "Maintain root zone mulch and apply seaweed foliar spray during vegetative flush."
        ],
        "chemical_controls": [
            "No chemical sprays needed."
        ],
        "prevention_measures": [
            "Prune only in dry summer weather to prevent bacterial canker (Pseudomonas) ingress.",
            "Monitor for cherry fruit fly and Japanese beetle activity during warm periods."
        ]
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "disease_key": "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "plant": "Corn",
        "disease_name": "Gray Leaf Spot",
        "is_healthy": False,
        "description": "Cercospora zeae-maydis is an economically damaging foliar disease favored by warm, humid weather and reduced-tillage continuous corn systems.",
        "symptoms": [
            "Tan to gray, narrow, rectangular lesions restricted by leaf veins.",
            "Lesions merge during severe outbreaks causing extensive leaf blighting.",
            "Premature stalk lodging and substantial grain fill reduction."
        ],
        "organic_controls": [
            "Incorporate crop residue deeply into soil using conservation tillage after harvest.",
            "Rotate corn fields with non-host crops like soybeans or alfalfa for at least two seasons.",
            "Apply bio-fungicides containing Trichoderma or Bacillus amyloliquefaciens."
        ],
        "chemical_controls": [
            "Apply dual-action fungicides containing Azoxystrobin + Difenoconazole or Pyraclostrobin + Fluxapyroxad.",
            "Target application at VT-R1 (tasseling to silking stage) when lesions appear on lower canopy."
        ],
        "prevention_measures": [
            "Plant gray leaf spot resistant hybrid seed varieties.",
            "Ensure adequate plant spacing to facilitate airflow within the field canopy.",
            "Avoid continuous corn cropping in minimum-till river bottom fields."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "disease_key": "Corn_(maize)___Common_rust_",
        "plant": "Corn",
        "disease_name": "Common Rust",
        "is_healthy": False,
        "description": "Common rust is caused by Puccinia sorghi, appearing as reddish-brown powdery pustules that erupt on both upper and lower leaf surfaces.",
        "symptoms": [
            "Cinnamon-brown to brick-red oval pustules scattered across both leaf surfaces.",
            "Pustules rupture epidermal tissue shedding powdery spores when touched.",
            "Severe infections turn leaves yellow, wither prematurely, and reduce cob development."
        ],
        "organic_controls": [
            "Plant resistant sweet corn or field corn hybrids.",
            "Apply micronized sulfur dust in early crop stages if rust pressure is detected early.",
            "Encourage diverse crop rotations to minimize spore reservoirs."
        ],
        "chemical_controls": [
            "Apply triazole fungicides (Propiconazole, Tebuconazole) if pustules spread prior to silking.",
            "Consider strobilurin treatments when cooler, moist weather forecasts favor rust progression."
        ],
        "prevention_measures": [
            "Early planting enables the crop to advance past critical reproductive stages before peak rust arrival.",
            "Scout weekly starting at V6 through tasseling."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "disease_key": "Corn_(maize)___Northern_Leaf_Blight",
        "plant": "Corn",
        "disease_name": "Northern Leaf Blight",
        "is_healthy": False,
        "description": "Northern corn leaf blight (Exserohilum turcicum) creates large, cigar-shaped grayish-green lesions that reduce photosynthetic area and lead to stalk cannibalization.",
        "symptoms": [
            "Long, elliptical, 'cigar-shaped' grayish-green lesions (1 to 6 inches long).",
            "Lesions turn tan with dark spore bands under humid conditions.",
            "Leaves turn dry and dead resembling frost damage in advanced stages."
        ],
        "organic_controls": [
            "Till crop debris to accelerate residue decomposition where erosion permits.",
            "Rotate with non-grass crops for two consecutive years.",
            "Apply preventative copper-based bio-rational sprays for organic specialty corn."
        ],
        "chemical_controls": [
            "Apply systemic fungicides like Pyraclostrobin + Metconazole or Azoxystrobin + Propiconazole.",
            "Time application at early tasseling (VT) if upper leaves show early lesions."
        ],
        "prevention_measures": [
            "Select resistant hybrids containing Ht-resistance genes (Ht1, Ht2, Ht3, or HtN).",
            "Maintain balanced soil fertility, avoiding high nitrogen combined with low potassium."
        ]
    },
    "Corn_(maize)___healthy": {
        "disease_key": "Corn_(maize)___healthy",
        "plant": "Corn",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Corn crop exhibits robust green leaf canopy, strong stalk structure, and healthy chlorophyll density with no symptoms of foliar blights or rust.",
        "symptoms": [
            "Broad, dark green arching leaves without chlorosis or necrosis.",
            "Clean leaf sheaths and sturdy brace roots.",
            "Uniform ear development and vigorous silk emergence."
        ],
        "organic_controls": [
            "Apply balanced nitrogen side-dressing and organic kelp foliar sprays during vegetative expansion."
        ],
        "chemical_controls": [
            "No chemical sprays necessary."
        ],
        "prevention_measures": [
            "Maintain soil drainage and scout for armyworms and corn earworms.",
            "Perform soil fertility testing to optimize N-P-K side-dress applications."
        ]
    },
    "Grape___Black_rot": {
        "disease_key": "Grape___Black_rot",
        "plant": "Grape",
        "disease_name": "Black Rot",
        "is_healthy": False,
        "description": "Guignardia bidwellii causes black rot in grapes, which attacks leaves, shoots, and fruit clusters, turning succulent berries into hard, shriveled black mummies.",
        "symptoms": [
            "Small yellowish circular leaf spots with dark reddish-brown borders containing tiny black specks.",
            "Fruit rots rapidly from light brown soft decay to black shriveled hard mummies.",
            "Elongated black lesions on green canes and tendrils."
        ],
        "organic_controls": [
            "Prune and destroy all mummified berries hanging on vines or fallen onto the vineyard floor.",
            "Spray copper hydroxide and lime sulfur before bud swell.",
            "Maximize canopy exposure with open trellis systems like VSP (Vertical Shoot Positioning)."
        ],
        "chemical_controls": [
            "Mancozeb or Ziram applied at 1-inch shoot growth through post-bloom.",
            "Myclobutanil, Tebuconazole, or Kresoxim-methyl applied during peak bloom and fruit set."
        ],
        "prevention_measures": [
            "Cultivate beneath the vine row to bury overwintered mummies.",
            "Trellis canes high to keep leaves away from ground moisture.",
            "Maintain a rigorous preventive spray program during rainy spring cycles."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "disease_key": "Grape___Esca_(Black_Measles)",
        "plant": "Grape",
        "disease_name": "Esca (Black Measles)",
        "is_healthy": False,
        "description": "Esca is a complex fungal vascular decline disease (Phaeomoniella chlamydospora, Phaeoacremonium) causing severe 'tiger-stripe' leaf patterns and spotted berry collapse.",
        "symptoms": [
            "Interveinal chlorosis and necrosis creating a distinctive 'tiger-stripe' pattern on leaves.",
            "Small dark purple spots on fruit berries resembling measles.",
            "Sudden midsummer apoplexy where vines suddenly wilt and collapse in heat."
        ],
        "organic_controls": [
            "Treat pruning wounds immediately with bio-fungicides like Trichoderma atroviride.",
            "Renew affected vines by retraining healthy suckers from below trunk cankers.",
            "Practice double pruning in winter to minimize deep wood infections."
        ],
        "chemical_controls": [
            "Apply wound sealants containing Thiophanate-methyl immediately following pruning cuts.",
            "No curative systemic chemical exists; management is purely preventive."
        ],
        "prevention_measures": [
            "Never prune vines during wet, humid weather when fungal ascospores are airborne.",
            "Disinfect pruning shears regularly with 70% denatured alcohol.",
            "Purchase certified pathogen-free nursery rootstock."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "disease_key": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
        "plant": "Grape",
        "disease_name": "Leaf Blight (Isariopsis Spot)",
        "is_healthy": False,
        "description": "Pseudocercospora cladosporioides causes leaf blight, producing irregular dark brown necrotic lesions on older leaves, causing defoliation in late summer.",
        "symptoms": [
            "Irregular, angular dark brown to black spots on mature leaves.",
            "Lesions coalesce causing large portions of the leaf blade to dry and curl.",
            "Premature defoliation exposing grape clusters to sunburn."
        ],
        "organic_controls": [
            "Apply Bordeaux mixture (copper sulfate + slaked lime) post-harvest or early season.",
            "Remove and compost fallen vineyard debris.",
            "Improve trellis canopy air circulation."
        ],
        "chemical_controls": [
            "Apply broad-spectrum fungicides such as Mancozeb, Captan, or Azoxystrobin.",
            "Target sprays during late spring and early summer."
        ],
        "prevention_measures": [
            "Regular shoot thinning and leaf pulling around fruit zones.",
            "Ensure proper vine spacing and row orientation to capture morning sun."
        ]
    },
    "Grape___healthy": {
        "disease_key": "Grape___healthy",
        "plant": "Grape",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Grape vine leaves demonstrate balanced vigor, clear green lamina, and healthy tendril production with no signs of fungal or bacterial decline.",
        "symptoms": [
            "Uniform vibrant green leaves with firm turgidity.",
            "Clean leaf petioles without cankers or streaking.",
            "Full, unblemished grape berry development."
        ],
        "organic_controls": [
            "Apply foliar seaweed extracts and compost teas to boost natural vine immunity."
        ],
        "chemical_controls": [
            "No chemical intervention needed."
        ],
        "prevention_measures": [
            "Maintain trellis wires and perform periodic shoot positioning.",
            "Scout for grape berry moth and leafhoppers."
        ]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "disease_key": "Orange___Haunglongbing_(Citrus_greening)",
        "plant": "Orange",
        "disease_name": "Citrus Greening (Huanglongbing)",
        "is_healthy": False,
        "description": "Huanglongbing (HLB) is a devastating, incurable bacterial disease (Candidatus Liberibacter asiaticus) transmitted by the Asian citrus psyllid, causing root decline and bitter misshapen fruit.",
        "symptoms": [
            "Asymmetric, blotchy mottle chlorosis across the leaf veins (unlike symmetric nutrient deficiency).",
            "Thickened, yellowed veins with corky appearance.",
            "Small, lopsided, bitter fruit that stays green at the bottom; premature fruit drop."
        ],
        "organic_controls": [
            "Aggressive control of the Asian citrus psyllid using natural predators (Tamarixia radiata wasp).",
            "Apply horticultural oils and insecticidal soaps to suffocate psyllid nymphs.",
            "Provide intensive nutritional foliar sprays (zinc, manganese, potassium) to prolong tree vigor."
        ],
        "chemical_controls": [
            "Systemic insecticides (Imidacloprid, Thiamethoxam) to suppress vector psyllid populations.",
            "Oxytetracycline trunk injections where officially approved for commercial orchards."
        ],
        "prevention_measures": [
            "Plant only certified disease-free citrus trees produced in insect-proof screened nurseries.",
            "Strictly eradicate confirmed infected trees to eliminate bacterial reservoirs.",
            "Report suspected citrus greening to local agricultural authorities immediately."
        ]
    },
    "Peach___Bacterial_spot": {
        "disease_key": "Peach___Bacterial_spot",
        "plant": "Peach",
        "disease_name": "Bacterial Spot",
        "is_healthy": False,
        "description": "Xanthomonas arboricola pv. pruni affects peaches and nectarines, causing purplish-black angular leaf spots that drop out, giving a 'shot-hole' appearance.",
        "symptoms": [
            "Small, water-soaked angular leaf spots turning dark purple to black.",
            "Centers of spots drop out, producing a characteristic 'shot-hole' perforation.",
            "Pitted, cracked, gum-exuding lesions on peach fruit skin."
        ],
        "organic_controls": [
            "Apply fixed copper sprays during dormant and delayed-dormant stages.",
            "Use bio-fungicides/bactericides containing Bacillus subtilis or copper octanoate.",
            "Avoid planting in extremely sandy soils where windblown sand damages cuticle."
        ],
        "chemical_controls": [
            "Oxytetracycline (Mycoshield) applied weekly during warm, wet post-bloom conditions.",
            "Low-rate copper applications during growing season (strictly monitored to prevent copper phytotoxicity)."
        ],
        "prevention_measures": [
            "Select resistant cultivars such as Candor, Biscoe, Harrow Beauty, or Clayton.",
            "Maintain moderate tree vigor and avoid excessive nitrogen fertilizer.",
            "Plant windbreaks around sandy orchard perimeters."
        ]
    },
    "Peach___healthy": {
        "disease_key": "Peach___healthy",
        "plant": "Peach",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Peach tree foliage displays long, lanceolate, healthy green blades with crisp borders and no signs of bacterial spot, leaf curl, or borers.",
        "symptoms": [
            "Supple, glossy green lance-shaped leaves.",
            "Absence of blisters, puckering, or red chlorosis.",
            "Vigorous extension shoot development."
        ],
        "organic_controls": [
            "Maintain organic orchard floor mulch and beneficial insect hedgerows."
        ],
        "chemical_controls": [
            "No chemical intervention required."
        ],
        "prevention_measures": [
            "Apply standard dormant copper/oil spray in late autumn to prevent spring peach leaf curl.",
            "Scout for peach tree borer frass at soil level."
        ]
    },
    "Pepper,_bell___Bacterial_spot": {
        "disease_key": "Pepper,_bell___Bacterial_spot",
        "plant": "Bell Pepper",
        "disease_name": "Bacterial Spot",
        "is_healthy": False,
        "description": "Xanthomonas campestris pv. vesicatoria causes bacterial spot in peppers, causing water-soaked spots on leaves and raised blistered warts on pepper fruit.",
        "symptoms": [
            "Small, water-soaked, irregular lesions on lower leaf surfaces.",
            "Spots turn dark brown with pale centers, often surrounded by yellow halos.",
            "Substantial defoliation causing sunscald damage to exposed peppers."
        ],
        "organic_controls": [
            "Treat seeds with hot water (50°C for 25 minutes) before planting to eradicate seed-borne bacteria.",
            "Apply copper sulfate or copper hydroxide combined with beneficial bio-bactericides.",
            "Mulch heavily with straw or plastic to prevent rain-splash from soil."
        ],
        "chemical_controls": [
            "Copper hydroxide tank-mixed with Mancozeb (increases free copper ion activity).",
            "Acibenzolar-S-methyl (Actigard) to activate systemic acquired plant resistance."
        ],
        "prevention_measures": [
            "Plant certified disease-free, bacterial-spot-resistant pepper hybrids.",
            "Never work or harvest within the pepper patch when plants are wet.",
            "Practice a 3-year crop rotation away from solanaceous family members (tomato, potato, eggplant)."
        ]
    },
    "Pepper,_bell___healthy": {
        "disease_key": "Pepper,_bell___healthy",
        "plant": "Bell Pepper",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Bell pepper plants show robust broad leaves, upright stems, and dark green glossy surfaces indicative of healthy root absorption.",
        "symptoms": [
            "Deep green, glossy leaf blades with smooth margins.",
            "Active floral bud initiation and firm, healthy stem nodes.",
            "Zero spotting, wilting, or mosaic mottling."
        ],
        "organic_controls": [
            "Apply calcium-rich fish hydrolysate or bone meal to prevent blossom end rot in developing peppers."
        ],
        "chemical_controls": [
            "No chemical controls needed."
        ],
        "prevention_measures": [
            "Maintain even soil moisture with drip irrigation to support steady fruit set.",
            "Monitor weekly for aphids and pepper weevils."
        ]
    },
    "Potato___Early_blight": {
        "disease_key": "Potato___Early_blight",
        "plant": "Potato",
        "disease_name": "Early Blight",
        "is_healthy": False,
        "description": "Early blight is caused by the necrotrophic fungus Alternaria solani, characterized by dark brown circular spots with distinct concentric rings ('target-board' pattern).",
        "symptoms": [
            "Concentric rings on dark brown leaf lesions creating a 'target board' effect.",
            "Yellow chlorotic halos surrounding developing lesions.",
            "Older lower foliage affected first, progressing upward as the plant matures."
        ],
        "organic_controls": [
            "Apply preventative copper octanoate or copper hydroxide fungicides.",
            "Enhance plant vigor with compost tea and balanced organic potassium.",
            "Remove lower infected foliage from small plots."
        ],
        "chemical_controls": [
            "Chlorothalonil or Mancozeb applied as protective contact sprays.",
            "Azoxystrobin, Boscalid, or Difenoconazole for systemic curative intervention."
        ],
        "prevention_measures": [
            "Plant certified, disease-free seed tubers.",
            "Maintain strict 3-year crop rotation with non-solanaceous crops.",
            "Avoid overhead sprinkler irrigation late in the afternoon."
        ]
    },
    "Potato___Late_blight": {
        "disease_key": "Potato___Late_blight",
        "plant": "Potato",
        "disease_name": "Late Blight",
        "is_healthy": False,
        "description": "Phytophthora infestans (the pathogen behind the Irish Potato Famine) is an aggressive oomycete that destroys potato foliage and causes dry rot in tubers under cool, humid conditions.",
        "symptoms": [
            "Dark, water-soaked irregular lesions on leaves that rapidly enlarge into black blighted areas.",
            "White velvety fungal growth on leaf undersides under humid/dew conditions.",
            "Stems develop dark brown cankers, causing entire vine collapse within days."
        ],
        "organic_controls": [
            "Apply preventative copper-based sprays (Bordeaux mixture) prior to high-risk weather.",
            "Immediately destroy and bury or burn heavily infected vines to prevent spore drift.",
            "Plant late blight-resistant potato cultivars like Sarpo Mira or Defender."
        ],
        "chemical_controls": [
            "Apply Mandipropamid, Dimethomorph, or Cymoxanil in combination with protectants like Mancozeb.",
            "Time applications using local late-blight forecasting advisory systems."
        ],
        "prevention_measures": [
            "Never allow volunteer potatoes or cull piles to sprout near production fields.",
            "Kill potato vines (desiccation) at least 2 weeks before harvesting tubers to prevent spore transfer to skins."
        ]
    },
    "Potato___healthy": {
        "disease_key": "Potato___healthy",
        "plant": "Potato",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "The potato plant demonstrates healthy compound leaves, firm turgid leaflets, and productive canopy coverage supporting tuber bulking.",
        "symptoms": [
            "Vibrant green compound leaves with crisp leaflet borders.",
            "Sturdy, upright stem habit with no blackleg or wilt.",
            "Clean foliage free from lesions, mosaic, or leaf roll."
        ],
        "organic_controls": [
            "Maintain hill height with clean soil/straw to protect developing tubers from sunlight."
        ],
        "chemical_controls": [
            "No chemical sprays needed."
        ],
        "prevention_measures": [
            "Scout for Colorado potato beetle larvae and potato leafhoppers.",
            "Maintain consistent soil moisture throughout the flowering and tuber initiation period."
        ]
    },
    "Raspberry___healthy": {
        "disease_key": "Raspberry___healthy",
        "plant": "Raspberry",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Raspberry cane foliage shows balanced growth, silvery underside pubescence, and robust primocane expansion free from spur blight or rust.",
        "symptoms": [
            "Compound serrated green leaves with clean undersides.",
            "Vigorous cane extension with healthy thorn/bark color.",
            "No yellow rust pustules or anthracnose spots."
        ],
        "organic_controls": [
            "Mulch cane base with clean wood chips and provide trellis support."
        ],
        "chemical_controls": [
            "No chemical intervention needed."
        ],
        "prevention_measures": [
            "Prune out old floricanes immediately following summer harvest to promote autumn primocane airflow.",
            "Keep rows narrow (2 feet wide) for maximum solar penetration."
        ]
    },
    "Soybean___healthy": {
        "disease_key": "Soybean___healthy",
        "plant": "Soybean",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Soybean trifoliate leaves are healthy, deep emerald green, showing active nodulation and photosynthesis without fungal rust or mosaic virus.",
        "symptoms": [
            "Uniform green trifoliate leaflets with intact margins.",
            "Active flowering and pod set along stem nodes.",
            "Zero frog-eye leaf spots, brown stem rot, or soybean cyst nematode chlorosis."
        ],
        "organic_controls": [
            "Encourage beneficial soil rhizobia bacteria for biological atmospheric nitrogen fixation."
        ],
        "chemical_controls": [
            "No chemicals necessary."
        ],
        "prevention_measures": [
            "Scout for stinkbugs and soybean aphids during pod-fill (R3-R5 stages).",
            "Maintain crop rotation with corn to break nematode and fungal life cycles."
        ]
    },
    "Squash___Powdery_mildew": {
        "disease_key": "Squash___Powdery_mildew",
        "plant": "Squash",
        "disease_name": "Powdery Mildew",
        "is_healthy": False,
        "description": "Podosphaera xanthii infects cucurbit crops, producing white talcum-powder-like patches on leaves and petioles that cause leaves to brown and die prematurely.",
        "symptoms": [
            "Circular white powdery fungal spots on upper and lower leaf surfaces.",
            "Spots rapidly expand to cover the entire leaf surface.",
            "Infected leaves turn yellow, then brown and papery, causing fruit sunscald."
        ],
        "organic_controls": [
            "Spray potassium bicarbonate (1 tbsp per gallon water with horticultural oil).",
            "Apply neem oil or sulfur fungicides at first appearance of powdery specks.",
            "Apply bio-fungicides based on Bacillus pumilus."
        ],
        "chemical_controls": [
            "Apply Quinoxyfen, Triflumizole, or Myclobutanil rotated across FRAC groups.",
            "Spray early morning when temperatures are below 30°C to prevent spray burn."
        ],
        "prevention_measures": [
            "Select powdery mildew resistant squash and pumpkin hybrids.",
            "Provide wide plant spacing (4-6 feet between rows) for optimal aeration.",
            "Avoid planting late-season cucurbits downwind of established infected plantings."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "disease_key": "Strawberry___Leaf_scorch",
        "plant": "Strawberry",
        "disease_name": "Leaf Scorch",
        "is_healthy": False,
        "description": "Diplocarpon earlianum causes leaf scorch in strawberry patches, producing numerous dark purple irregular spots that can cause the entire leaf to appear scorched and dried.",
        "symptoms": [
            "Small, irregular purple spots on upper leaf surfaces without white centers (distinguishing it from common leaf spot).",
            "Lesions enlarge and coalesce, turning the leaf margins brown and scorched.",
            "Fruit calyx (green cap) becomes infected and turns brown, reducing market value."
        ],
        "organic_controls": [
            "Rake and remove old dead leaves during post-harvest bed renovation.",
            "Apply copper-based fungicides in early spring as new crown leaves emerge.",
            "Avoid overhead irrigation; use drip tape beneath mulch."
        ],
        "chemical_controls": [
            "Captan or Myclobutanil applied during pre-bloom and bloom windows.",
            "Azoxystrobin or Pyraclostrobin rotated to prevent fungal resistance."
        ],
        "prevention_measures": [
            "Plant certified disease-free strawberry runners.",
            "Renovate strawberry beds annually by mowing old foliage and thinning plants.",
            "Plant in full sun in well-drained sandy loam soil."
        ]
    },
    "Strawberry___healthy": {
        "disease_key": "Strawberry___healthy",
        "plant": "Strawberry",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "Strawberry plant displays healthy trifoliate leaves with vibrant green coloration, crisp serrated margins, and active crown health.",
        "symptoms": [
            "Deep green trifoliate leaves with prominent veins.",
            "Vigorous runner production and firm white flowers.",
            "Zero leaf spots, powdery mildew, or angular leaf spot lesions."
        ],
        "organic_controls": [
            "Maintain clean straw or plastic mulch to keep fruit and leaves off bare soil."
        ],
        "chemical_controls": [
            "No chemical intervention needed."
        ],
        "prevention_measures": [
            "Scout for two-spotted spider mites on leaf undersides in warm weather.",
            "Ensure regular drip irrigation during bloom and fruit swell."
        ]
    },
    "Tomato___Bacterial_spot": {
        "disease_key": "Tomato___Bacterial_spot",
        "plant": "Tomato",
        "disease_name": "Bacterial Spot",
        "is_healthy": False,
        "description": "Bacterial spot (Xanthomonas spp.) causes small, greasy brown spots on leaves, stems, and fruit, exacerbated by warm temperatures and frequent splashing rain.",
        "symptoms": [
            "Small (less than 3 mm), dark, water-soaked circular spots on leaves.",
            "Spots turn brown to black with yellow halos; leaves take on a ragged, torn look.",
            "Raised, scab-like, scabby black blisters on developing green tomatoes."
        ],
        "organic_controls": [
            "Apply liquid copper octanoate combined with microbial bio-pesticides.",
            "Soak seeds in 50°C hot water for 25 minutes prior to planting.",
            "Prune lower suckers to minimize soil splashing."
        ],
        "chemical_controls": [
            "Fixed copper mixed with Mancozeb spray program applied every 7–10 days.",
            "Actigard (systemic acquired resistance inducer) applied early in crop cycle."
        ],
        "prevention_measures": [
            "Use drip irrigation instead of overhead sprinklers.",
            "Rotate tomato plots on a 3-year cycle away from peppers and eggplants.",
            "Sterilize garden stakes and trellis cages with bleach solution."
        ]
    },
    "Tomato___Early_blight": {
        "disease_key": "Tomato___Early_blight",
        "plant": "Tomato",
        "disease_name": "Early Blight",
        "is_healthy": False,
        "description": "Alternaria linariae causes early blight on tomatoes, producing distinctive dark brown circular lesions with concentric rings ('target-board' pattern), starting on the oldest lower leaves.",
        "symptoms": [
            "Dark brown to black spots with concentric rings on lower leaves.",
            "Surrounding leaf tissue turns yellow, followed by leaf drop.",
            "Dark, sunken, leathery cankers on stems and fruit stem end."
        ],
        "organic_controls": [
            "Prune off the bottom 12–18 inches of tomato foliage to prevent ground contact.",
            "Apply copper sulfate or sulfur-based organic fungicides early in the season.",
            "Apply 2–3 inches of straw mulch under plants to block soil-dwelling fungal spores."
        ],
        "chemical_controls": [
            "Chlorothalonil (Daconil) or Mancozeb as preventative protective sprays.",
            "Azoxystrobin or Difenoconazole applied when early lesions are identified."
        ],
        "prevention_measures": [
            "Space tomato plants 24–36 inches apart to maximize air drying.",
            "Stake or cage indeterminate vines off the ground.",
            "Rotate crops annually away from solanaceous plants."
        ]
    },
    "Tomato___Late_blight": {
        "disease_key": "Tomato___Late_blight",
        "plant": "Tomato",
        "disease_name": "Late Blight",
        "is_healthy": False,
        "description": "Phytophthora infestans is a devastating water mold causing rapid blackened foliage collapse, white mildew growth under damp conditions, and firm brown rot on fruit.",
        "symptoms": [
            "Large, dark, water-soaked lesions that rapidly expand across leaves and stems.",
            "White cottony fungal growth on leaf undersides in humid or rainy weather.",
            "Golden brown, greasy, firm rot on green and ripe tomato fruit."
        ],
        "organic_controls": [
            "Apply preventative copper hydroxide sprays before humid, rainy weather.",
            "Promptly pull and bag up infected plants on dry days to protect neighboring crops.",
            "Plant resistant tomato varieties like Mountain Magic, Defiant, or Iron Lady."
        ],
        "chemical_controls": [
            "Mandipropamid (Revus), Cymoxanil, or Fluopicolide combined with protectant fungicides.",
            "Begin protective spray regimens when late blight has been reported in your regional forecast."
        ],
        "prevention_measures": [
            "Never compost late-blight-infected tomato vines.",
            "Avoid overhead irrigation; water only at the soil level in the morning.",
            "Keep greenhouse and high-tunnel vents open to minimize relative humidity."
        ]
    },
    "Tomato___Leaf_Mold": {
        "disease_key": "Tomato___Leaf_Mold",
        "plant": "Tomato",
        "disease_name": "Leaf Mold",
        "is_healthy": False,
        "description": "Passalora fulva causes tomato leaf mold, common in greenhouses and high tunnels with relative humidity above 85%, producing pale green/yellow spots on top and olive-brown mold underneath.",
        "symptoms": [
            "Pale yellow spots on the upper leaf surface without defined borders.",
            "Dense, olive-green to brown velvety fungal growth directly under the yellow spots.",
            "Leaves curl, wither, and drop prematurely, reducing photosynthetic capacity."
        ],
        "organic_controls": [
            "Ventilate greenhouses and utilize circulation fans to keep relative humidity below 80%.",
            "Apply bio-fungicides based on Bacillus subtilis or copper soap.",
            "Prune dense suckers to open the canopy."
        ],
        "chemical_controls": [
            "Apply Chlorothalonil, Mancozeb, or Difenoconazole at first symptom onset.",
            "Alternate with strobilurin fungicides for resistance management."
        ],
        "prevention_measures": [
            "Use greenhouse heating and ventilation cycles to purge nocturnal condensation.",
            "Select leaf-mold-resistant hybrid varieties.",
            "Avoid splashing water on foliage during watering."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "disease_key": "Tomato___Septoria_leaf_spot",
        "plant": "Tomato",
        "disease_name": "Septoria Leaf Spot",
        "is_healthy": False,
        "description": "Septoria lycopersici causes small, circular spots with dark brown margins and gray centers containing tiny black specks (pycnidia), quickly defoliating tomato plants from the bottom up.",
        "symptoms": [
            "Numerous small circular spots (2-3 mm) with dark brown borders and light gray centers.",
            "Tiny black pimple-like fruiting bodies visible inside the gray centers with a hand lens.",
            "Progressive bottom-up defoliation leaving fruit susceptible to sunscald."
        ],
        "organic_controls": [
            "Remove lower infected leaves as soon as first spots appear on bottom branches.",
            "Apply copper fungicides or bio-fungicide sprays every 7–10 days.",
            "Mulch heavily around the plant base to prevent rain splash."
        ],
        "chemical_controls": [
            "Chlorothalonil or Mancozeb as standard preventative treatments.",
            "Quadris Top (Azoxystrobin + Difenoconazole) for curative control."
        ],
        "prevention_measures": [
            "Practice minimum 2-year crop rotation.",
            "Water with soaker hoses or drip irrigation.",
            "Clean up all tomato crop debris at the end of the growing season."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "disease_key": "Tomato___Spider_mites Two-spotted_spider_mite",
        "plant": "Tomato",
        "disease_name": "Two-Spotted Spider Mites",
        "is_healthy": False,
        "description": "Tetranychus urticae are microscopic sap-sucking arachnids that proliferate in hot, dry, dusty conditions, causing fine yellow stippling and webbing over tomato leaves.",
        "symptoms": [
            "Fine yellow or white stippling (tiny dots) on the upper leaf surface.",
            "Delicate silken webbing on leaf undersides and between branch forks.",
            "Leaves turn bronze, dry out, and drop; plants become stunted."
        ],
        "organic_controls": [
            "Release predatory mites like Phytoseiulus persimilis or Neoseiulus californicus.",
            "Spray insecticidal soap, neem oil, or rosemary oil miticide thoroughly on leaf undersides.",
            "Blast plants with a strong stream of water to knock mites off and destroy webbing."
        ],
        "chemical_controls": [
            "Apply selective miticides such as Bifenazate (Acramite) or Abamectin.",
            "Avoid broad-spectrum pyrethroids, which kill beneficial predatory insects and cause mite flare-ups."
        ],
        "prevention_measures": [
            "Keep orchard and garden pathways watered or mulched to suppress dust.",
            "Maintain adequate irrigation; drought-stressed plants are preferred mite hosts."
        ]
    },
    "Tomato___Target_Spot": {
        "disease_key": "Tomato___Target_Spot",
        "plant": "Tomato",
        "disease_name": "Target Spot",
        "is_healthy": False,
        "description": "Corynespora cassiicola causes target spot on tomatoes in warm, humid climates, producing brown lesions with light brown centers and dark concentric rings on leaves and fruit.",
        "symptoms": [
            "Brown pinpoint spots on leaves that enlarge to circular lesions with pale brown centers.",
            "Dark concentric rings resembling a target board.",
            "Sunken, brown, circular lesions on tomato fruit with cratered margins."
        ],
        "organic_controls": [
            "Prune dense lower foliage to enhance air movement within the vine rows.",
            "Spray copper hydroxide formulations regularly during humid periods.",
            "Sanitize garden tools and stakes."
        ],
        "chemical_controls": [
            "Apply Chlorothalonil or Boscalid fungicides.",
            "Rotate with Pyraclostrobin or Famoxadone for integrated pest management."
        ],
        "prevention_measures": [
            "Space plants adequately to avoid dense overlapping canopies.",
            "Avoid overhead irrigation and control weeds that act as alternate hosts."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "disease_key": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "plant": "Tomato",
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "description": "TYLCV is a destructive begomovirus transmitted by the sweetpotato whitefly (Bemisia tabaci), causing upward cupping of leaves, severe stunting, and complete flower drop.",
        "symptoms": [
            "Upward curling and cupping of leaflets into a spoon-like shape.",
            "Interveinal yellowing (chlorosis) along leaf margins.",
            "Severe plant stunting, bushy upright habit, and failure to set fruit."
        ],
        "organic_controls": [
            "Eradicate whitefly vectors using yellow sticky traps and insecticidal soap sprays.",
            "Cover young seedlings with fine insect-exclusion netting (50-mesh).",
            "Immediately pull up and destroy infected plants in sealed plastic bags."
        ],
        "chemical_controls": [
            "No antiviral chemicals exist; control is achieved by targeting whitefly vectors with insecticides (e.g., Spiromesifen, Dinotefuran)."
        ],
        "prevention_measures": [
            "Plant TYLCV-resistant tomato cultivars (e.g., Tycoon, Chef's Choice, SV8232TE).",
            "Maintain a whitefly-free nursery for all transplant seedlings.",
            "Eliminate solanaceous weeds around field borders."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "disease_key": "Tomato___Tomato_mosaic_virus",
        "plant": "Tomato",
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "description": "ToMV is an exceptionally stable, highly contagious tobamovirus spread mechanically by hands, tools, and seeds, causing mottled yellow-green leaves and internal fruit browning.",
        "symptoms": [
            "Mottled light and dark green mosaic patterns on leaves.",
            "Distorted, blistered, or fern-like 'shoestring' leaf growth.",
            "Uneven fruit ripening and brown internal necrotic streaks inside fruit walls."
        ],
        "organic_controls": [
            "Wash hands and dip tools in non-fat dry milk solution (20%) or 10% TSP to inactivate viral proteins.",
            "Carefully rogue and destroy infected plants without touching healthy neighbors.",
            "Do not allow tobacco users to handle tomato plants without thorough hand sanitation."
        ],
        "chemical_controls": [
            "No chemical viricides exist; management relies entirely on sanitation and resistance."
        ],
        "prevention_measures": [
            "Plant ToMV-resistant cultivars (labeled with 'T' or 'ToMV').",
            "Purchase certified clean seeds or soak seeds in 10% trisodium phosphate (TSP) for 15 minutes.",
            "Thoroughly steam-sterilize or replace potting soil between seasons."
        ]
    },
    "Tomato___healthy": {
        "disease_key": "Tomato___healthy",
        "plant": "Tomato",
        "disease_name": "Healthy Foliage",
        "is_healthy": True,
        "description": "The tomato foliage is healthy, deep green, robust, and actively producing blossoms without signs of viral mosaic, bacterial spots, or fungal blights.",
        "symptoms": [
            "Deep green, serrated, turgid leaflets with healthy glandular trichomes (hairs).",
            "Sturdy central stem and branches supporting uniform flower clusters.",
            "Zero spotting, wilting, mosaic mottling, or fungal sporulation."
        ],
        "organic_controls": [
            "Apply balanced organic tomato fertilizer (moderate nitrogen, high phosphorus and potassium).",
            "Spray compost tea to maintain beneficial phyllosphere microbial populations."
        ],
        "chemical_controls": [
            "No chemical applications required."
        ],
        "prevention_measures": [
            "Maintain regular drip irrigation and side-dress with calcium to prevent blossom end rot.",
            "Prune bottom leaves up to 12 inches off the ground as plants mature.",
            "Mulch with clean straw or black landscape fabric."
        ]
    }
}

def format_guidance_entry(entry: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not entry:
        return None
    res = dict(entry)
    res["crop"] = entry.get("plant", "")
    res["disease"] = entry.get("disease_name", "")
    res["summary"] = entry.get("description", "")
    res["organic_treatments"] = entry.get("organic_controls", [])
    res["chemical_treatments"] = entry.get("chemical_controls", [])
    res["prevention_methods"] = entry.get("prevention_measures", [])
    return res

def get_disease_guidance(disease_key: str) -> Optional[Dict[str, Any]]:
    raw = GUIDANCE_DATABASE.get(disease_key)
    return format_guidance_entry(raw)

def list_all_guidance() -> list:
    return [format_guidance_entry(v) for v in GUIDANCE_DATABASE.values()]

def get_guidance(disease_key: str) -> Optional[Dict[str, Any]]:
    return get_disease_guidance(disease_key)

def get_all_guidance() -> Dict[str, Dict[str, Any]]:
    return GUIDANCE_DATABASE
