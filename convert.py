import asyncio
import edge_tts
import os

# ==========================================
# EDIT THIS PART: Paste your article text here
# ==========================================
ARTICLE_TEXT = """
African Yam: The King of Crops
Did you know the true African yam (Dioscorea rotundata) is celebrated with annual harvest festivals across West Africa where no one eats the new crop until the ancestors are served first? Its dense, starchy flesh transforms into elastic pounded yam (Iyan), sun-dried chips for dark Amala, and roasted street wedges. Just never confuse it with the soft, orange-fleshed sweet potatoes sold as "yams" in American supermarkets.

The African Yam—scientifically classified under the genus Dioscorea and most famously represented by the White Guinea Yam (Dioscorea rotundata) and Yellow Guinea Yam (Dioscorea cayenensis)—is a cherished indigenous root crop native to the river basins, savannas, and forest edges of West and Central Africa. Across the fertile "Yam Belt," stretching from Côte d'Ivoire through Ghana, Togo, Benin, Nigeria, and Cameroon, this resilient climbing vine thrives in well-drained soils, yielding heavy subterranean storage tubers that can weigh anywhere from 5 to over 30 pounds.

Local communities revere the yam as the "King of Crops" because it serves far beyond everyday sustenance. While its dense, energy-rich flesh forms the foundation of celebrated dishes like pounded yam, porridges, and medicinal broths, the tuber historically functioned as currency, social capital, and the centerpiece of traditional agricultural cosmology. Meanwhile, the vine, peels, leaves, and wild varieties feature prominently in local ethnomedicine and soil regeneration.

This multifaceted role highlights the deep cultural and ecological heritage of African root systems. Here is our detailed guide to this iconic African staple, covering its botany, culinary behavior, indigenous storage engineering, cultural standing, and cultivation considerations.

What is the yam called across Africa?
This staple tuber is known by distinct names across various regional languages and cultural groups, reflecting its widespread domestic importance across the continent.

Region / Language	Common Name(s)
International	True Yam, White Guinea Yam, African Yam
Nigeria (Igbo)	Ji
Nigeria (Yoruba)	Isu
Nigeria (Hausa)	Doya
Ghana / Côte d'Ivoire (Akan / Twi)	Bayere (White Yam), Afase (Water Yam)
Ghana / Togo (Ewe)	Te
Cameroon	Yam, Koko-yam (vernacular distinctions)
Sierra Leone (Krio)	Yam
A Common Confusion: Not the American Sweet Potato
Despite American grocery stores labeling moist, orange-fleshed tubers as "yams," the African Yam (Dioscorea rotundata) is completely unrelated to the American sweet potato (Ipomoea batatas).

West African Yams: How They're Grown, Plus a Sautéed Yam Recipe goes further into how the yams are grown, plus a sautéed yam recipe.

Air Potato: West African Food, Florida Invasive looks at another Dioscorea from West Africa.

Feature	African True Yam (Dioscorea)	Sweet Potato / US "Yam" (Ipomoea)
Botanical Family	Dioscoreaceae (Monocot)	Convolvulaceae (Dicot / Morning Glory family)
Origin	Native to West & Central Africa	Native to the tropical Americas
Size & Shape	Large, cylindrical logs (often 2–10+ lbs, up to 5 ft)	Small to medium tapered roots (0.5–2 lbs)
Skin Texture	Rough, dark brown, bark-like, fibrous, hairy	Smooth, thin, orange, copper, or purplish skin
Flesh & Flavor	Dense, dry, starchy, ivory-white or pale yellow	Soft, moist, distinctly sweet, orange or reddish
Primary Culinary Use	Boiled & pounded into elastic dough; fried; roasted	Baked whole, candied, mashed in casseroles/pies
The bottom line: If you are looking at a small, smooth, reddish-orange tuber that bakes up syrupy-sweet, that is an American sweet potato. The true African Yam is a massive, bark-skinned, dense, and savory tuber—equally versatile, but fundamentally different in botany, texture, and taste.

What does African yam taste like?
The yam's culinary versatility comes from its neutral, satisfying starch profile and firm internal structure.

Aroma: When freshly cut, raw yam has a clean, faint, earth-and-rain aroma. Once boiled or steamed, it emits a comforting, warm, slightly sweet vapor akin to roasted chestnuts or boiled russet potatoes.
Flavor: Mild, savory, and nutty. It is far less sweet than a sweet potato and possesses an earthy, mineral depth that acts as a canvas for richly spiced broths, red palm oil, and leafy stews.
Texture: Dense and dry with a high amylose content. When boiled, it holds its structural integrity without disintegrating into mush. When sheared in a mortar, those starch polymers bind into a stretchy, cohesive, dough-like swallow (Iyan).
Why Does Tuber Size and Quality Vary?
Mounding and Soil Depth: Yam tubers expand straight down. In soft, loose, elevated earthen mounds (often 3 feet high), tubers grow long, straight, and unhindered. Heavy clay or rocky terrain causes stunted, bifurcated, or knobby roots.
Rainfall Timing: Ample moisture during the vegetative bulking phase creates massive tubers, while excessive water near maturity risks root rot and shortens post-harvest shelf life.
Cultural Significance & Context
The yam is woven into the spiritual, economic, and moral fabric of West African life.

The "King of Crops": In traditional agrarian communities, yam farming was historically an elite undertaking requiring physical strength, discipline, and land mastery. A man's wealth, work ethic, and ability to feed his lineage were measured directly by the size of his yam barn, earning distinguished social titles like Eze Ji (Yam King) in Igboland.
The New Yam Festival: Celebrated at the close of the rainy season (typically August to October) under names like Iri Ji (Igbo) or Te Za (Ewe). Custom strictly forbids eating the newly harvested tubers until the first fruits are consecrated to the earth deity (Ala) and the ancestors in gratitude for community survival and soil fertility.
Gender and Foodways Division: In traditional agrarian systems, yams stood as the primary prestige crop cultivated by men, while women intercropped and managed vital companion foods like cocoyam, cassava, peppers, leafy greens, and legumes—ensuring steady household nourishment during the lean "hunger months" before the yam harvest.
Material States with Cultural Annotation
Every stage of the yam tuber, from field curation to dry preservation, serves a deliberate domestic purpose.

Part of Plant	State / Preparation	Cultural / Practical Use
Head Sett (Apical portion)	Cut tuber top with sprout buds	Reserved as high-viability seed yam for planting next season's crop
Middle / Tail Flesh	Fresh, unblemished raw rounds	Boiled for pounding (Iyan), cubed for pottage (Asaro), or sliced for frying (Dundun)
Wounded / Bruised Tuber	Damaged during harvest excavation	Culled immediately for early home consumption to prevent rots in the storage barn
Tuber Slices (Gbodo)	Parboiled, steeped, and sun-dried	Milled into dark, fermented yam flour for making Amala Isu
Peels & Scrapings	Raw or dried thick rind	High-starch livestock feed for domestic goats and cattle; composted for organic mulch
Vine Shoots & Stems	Fast-climbing green foliage	Used in local ethnoveterinary remedies; ash used as a potassium-rich soil amendment
Processing Chain Details
The journey from underground tuber to stable staple relies on time-tested post-harvest engineering:

Harvesting: Excavation requires extreme care using wooden digging sticks or flat spade blades to uncover the tuber without nicking or bruising the skin, which invites soft-rot pathogens.
Curing: Freshly dug tubers are laid out in shaded, well-ventilated clearings for a few days to thicken their corky outer peel and suberize any minor surface scratches.
Barn Storage: Tubers are individually lashed with palm frond twine or raffia along vertical wooden poles in open-air barns beneath living shade trees. Suspending them off the ground provides 360-degree cross-ventilation, keeps them cool, prevents rodent damage, and isolates rotting tubers from their neighbors.
Value Addition & Flour Milling: Excess yams, or varieties that break dormancy early, are sliced thin, parboiled to stop enzyme activity, fermented lightly, and sun-dried on rock terraces or mats into brittle brown chips (gbodo), then ground into flour for long-term pantry storage.
Types of Cooking and Fresh Uses
The yam is one of the most culinary-adaptable tubers in the world, prepared through boiling, pounding, braising, roasting, and deep-frying:

Pounded Yam (Iyan / Utara Ji): The ultimate prestige dish. Boiled yam chunks are rhythmically sheared and compressed in a heavy wooden mortar until the starch cells fracture, tangling into a glossy, pillowy dough served with rich soups like Egusi, Ofe Nsala, or Efo Riro.
Amala Isu: A dark, savory swallow prepared by whisking sun-dried fermented yam flour into boiling water, prized across Yoruba culinary traditions for its light digestability and earthy profile.
Asaro (Yam Pottage): Yam cubes braised directly in red palm oil, peppers, onions, smoked dried fish, and leafy greens. As the yam simmers, its starches break down along the edges to naturally emulsify the broth into a rich gravy.
Dundun (Fried Yam): Thick sticks or rounds soaked briefly in salted water and deep-fried until the exterior forms a crisp, pale-golden shell enclosing a fluffy, steaming interior, sold ubiquitously as street food with fried pepper sauce (Ata Dindin).
Roasted Yam (Ji Ebe): Whole unpeeled chunks roasted over open wood embers until the outer bark is thoroughly charred, then scraped clean and dipped in raw, salted red palm oil stirred with native seasonings.

How do you choose a ripe African yam?
When shopping at African, Caribbean, or international markets, use these sensory checks to pick a prime tuber:

Firmness: Press firmly along the entire length of the tuber, especially around the tips. It should feel stone-hard. Any soft spots, spongy depressions, or "give" indicate internal rot.
Skin & Cut Ends: Look for unbroken, dry bark without weeping moisture, cracks, or white mold. If the vendor has sliced off an end, check that the exposed flesh is pure, moist, and chalky-white or pale cream—never grey, brown, or translucent.
Weight: A healthy, dormant yam feels heavy for its size. A tuber that feels hollow or featherlight has dried out or consumed its own starch reserves during prolonged storage.
Sprouting: Avoid tubers with long, active purple or green shoots emerging from the head. Sprouting signals that internal dormancy has broken, meaning the starches are turning into sugars and leaving the center woody and fibrous.
Regional Variations
Species Nuances: While White Yam (D. rotundata) dominates commercial markets for pounding, Water Yam (Dioscorea alata)—featuring squarish, winged vines—has a wetter, looser crumb ideal for frying into crispy grated fritters (Ojojo) or steaming into savory pudding (Ikokore).
Yellow Guinea Yam (D. cayenensis): Takes up to 12 months to mature, yielding yellow, vitamin-A-rich flesh that has a firmer, waxier consistency favored in certain traditional boil-and-dip recipes.
Bitter Yam (Dioscorea dumetorum): Grown in localized patches across West and Central Africa; highly nutritious with superior protein content, but requires thorough boiling and leaching to eliminate natural protective alkaloids before eating.
Contemporary Context
Today, the African yam is transitioning from a localized subsistence staple to a high-value commercial and scientific priority.

Commercial Export Markets: West African diasporic demand has created a thriving export corridor, with countries like Ghana and Nigeria shipping thousands of tons of vacuum-packed and fresh tubers annually to the United Kingdom, Europe, and North America.
Agronomic Innovation: Organizations like the International Institute of Tropical Agriculture (IITA) in Ibadan, Nigeria, are developing aeroponics and single-node vine cutting technologies to rapidly multiply clean, virus-free seed yams, addressing the historical hurdle of high seed cost.
Mechanization of Processing: Modern electric yam pounders and commercial milling factories now produce uniform yam flour, making everyday urban preparation accessible without manual mortar-and-pestle labor.
Practical Information
Growing Conditions: Yams demand loose, well-draining sandy loam rich in organic matter, warm tropical temperatures, and at least 6 to 8 months of frost-free growing conditions under full sun.
Propagation: Grown vegetatively from "seed yams" (small whole tubers) or "setts" (cut pieces of mature tubers weighing 200–500g). Setts are traditionally dusted with wood ash to dry cut surfaces and protect against fungal decay before planting.
Staking Requirements: As climbing vines, yams must be trained up tall wooden stakes or trellises (often 6 to 10 feet high). Staking lifts foliage into direct sunlight, dramatically boosting photosynthetic output and increasing final tuber yield.
Harvesting Season: The main harvest takes place at the onset of the dry season (typically October through December in West Africa) when the above-ground vines naturally turn yellow, dry out, and die back.
Safety: True yams should never be consumed raw. While cultivated white and yellow yams have low alkaloid levels, thorough cooking ensures complete starch gelatinization and neutralizes trace anti-nutritional compounds.
Can You Grow It in the United States? 
The African Guinea Yam (Dioscorea rotundata) is a strictly tropical, long-season crop. Growing it in the continental United States is limited to warm regions with an extended, frost-free calendar.

Feasibility: Where It Can Grow
Hardiness Zones: True African yams require conditions equivalent to USDA hardiness zones 9b through 12, demanding 200 to 270 continuous warm, sunny growing days to bulk underground tubers.
Suitable US States:
Florida (Central and South): Ideal conditions. Deep sandy soils, abundant summer rainfall, and subtropical heat mirror the West African coast.
Hawaii: Excellent year-round tropical environment.
Southern Texas (Gulf Coast / Lower Rio Grande Valley): Well-suited with supplemental irrigation during peak summer heat.
Gulf Coast portions of Louisiana, Mississippi, and Alabama: Feasible if tubers are started in containers early spring and planted after all danger of cool soil passes.
Temperature Sensitivity: Vines halt growth when temperatures dip below 60°F (15°C), and any ground frost will kill the foliage and rot developing tubers.
Trellising & Care: In warm US regions, give the vine substantial vertical support—such as a tall chain-link fence, heavy wooden arbor, or 8-foot bamboo teepee. Harvest carefully in late autumn once the entire vine canopy naturally withers to brown.
"""
# ==========================================

OUTPUT_FILE = "podcast.mp3"
VOICE = "en-US-AndrewNeural"  # US English male voice. Change to "en-US-AvaNeural" for female.

async def main():
    print(f"Generating audio using voice: {VOICE}")
    communicate = edge_tts.Communicate(ARTICLE_TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    
    # Simple check to ensure the file is not empty
    if os.path.exists(OUTPUT_FILE) and os.path.getsize(OUTPUT_FILE) > 1000:
        print(f"Success! Audio saved to {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)")
    else:
        print("Error: Audio file is missing or too small. Check the text or try again.")
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())
