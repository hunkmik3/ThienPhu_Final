import os

# Helper function to generate bullet list HTML
def create_list_html(items):
    return "\n".join([f"                            <li><i class='tf-ion-ios-arrow-right mr-2 text-primary'></i>{item}</li>" for item in items])

# English Products List with Rich Content
products_data = [
    {
        "slug": "tempered-glass",
        "name": "Tempered Glass",
        "short_desc": "Tempered glass is a superior safety material solution created from a special thermal tempering process.",
        "img_file": "kinhcuongluc.jpg",
        "long_desc": "Tempered glass is a type of safety glass processed by controlled thermal or chemical treatments to increase its strength compared to normal glass. The glass is heated to approximately 700°C and then rapidly cooled. This process creates surface stress suitable for applications requiring superior strength. Outstanding for its load-bearing capacity, impact resistance, and thermal shock resistance 4-5 times greater than ordinary glass, it is the top choice for every project. The most valuable feature is its safe breakage mechanism—shattering into small, blunt granules instead of sharp shards, ensuring absolute safety for users.",
        "features": [
            "<strong>High Strength:</strong> 4 to 5 times stronger than standard float glass of the same thickness.",
            "<strong>Safety:</strong> If broken, it shatters into small, blunt granular chunks, minimizing injury risk.",
            "<strong>Thermal Resistance:</strong> Withstands temperatures up to 250°C and thermal shock up to 150°C.",
            "<strong>Durability:</strong> High resistance to impact and bending loads.",
            "<strong>Optical Clarity:</strong> Maintains the light transmission and clarity of the original glass."
        ],
        "applications": [
            "Frameless glass doors, sliding doors, shower enclosures.",
            "Glass balcony railings, staircases, fences.",
            "Building facades, storefronts, curtain walls.",
            "Tabletops, glass shelves, kitchen splashbacks.",
            "Partition walls in offices and homes."
        ]
    },
    {
        "slug": "laminated-glass",
        "name": "Laminated Glass",
        "short_desc": "Laminated safety glass is made of two or more layers of glass bonded together by a PVB interlayer.",
        "img_file": "kinh-cuong-luc-2-lop-3.jpg",
        "long_desc": "Laminated glass is a type of safety glass that holds together when shattered. It is manufactured by permanently bonding two or more lites of glass with a tough interlayer of Polyvinyl Butyral (PVB) or Ethylene-Vinyl Acetate (EVA), under heat and pressure. In the event of breaking, the interlayer holds the fragments together and keeps the glass sheet largely intact. This prevents large sharp shards from falling and causing injury, while also providing a barrier against forced entry.",
        "features": [
            "<strong>Safety & Security:</strong> Resists penetration; glass shards adhere to the interlayer if broken.",
            "<strong>Sound Insulation:</strong> The interlayer dampens sound, providing excellent noise reduction.",
            "<strong>UV Protection:</strong> Blocks up to 99% of harmful UV rays, protecting interiors from fading.",
            "<strong>Storm & Impact Resistance:</strong> Remains intact even under heavy impact or strong winds.",
            "<strong>Design Flexibility:</strong> Can incorporate colored interlayers for aesthetic effects."
        ],
        "applications": [
            "Skylights, glass roofs, canopies (overhead glazing).",
            "Glass floors, stair treads.",
            "High-security windows and doors for banks, jewelry stores.",
            "Automotive windshields.",
            "Windows in hurricane-prone areas."
        ]
    },
    {
        "slug": "insulated-glass",
        "name": "Insulated Glass (IGU)",
        "short_desc": "Insulated glass is the leading solution for energy saving and soundproofing for modern buildings.",
        "img_file": "kinh-hop-an-toan.jpg",
        "long_desc": "Insulating Glass Units (IGUs), commonly known as double glazing, consist of two or more glass window panes separated by a vacuum or gas-filled space (argon or krypton) to reduce heat transfer across a part of the building envelope. The edges are sealed with a primary and secondary sealant to ensure structural integrity and prevent moisture penetration. IGUs are the standard for energy-efficient construction.",
        "features": [
            "<strong>Thermal Insulation:</strong> Significantly reduces heat loss in winter and heat gain in summer.",
            "<strong>Energy Efficiency:</strong> Lowers energy costs for heating and cooling by 30-50%.",
            "<strong>Soundproofing:</strong> Provides superior acoustic insulation compared to single glazing.",
            "<strong>Condensation Control:</strong> Minimizes moisture buildup on window surfaces.",
            "<strong>Versatility:</strong> Can combine with Low-E, reflective, or tinted glass for enhanced performance."
        ],
        "applications": [
            "Exterior facades of office buildings, hotels, and high-rises.",
            "Windows and doors for residential homes.",
            "Glass curtain walls.",
            "Refrigeration units and commercial freezers.",
            "Partition walls in recording studios or meeting rooms."
        ]
    },
    {
        "slug": "curved-glass",
        "name": "Curved Glass",
        "short_desc": "Curved glass is produced using specialized thermal bending technology, creating unique aesthetic highlights.",
        "img_file": "kinhuongcong.jpg",
        "long_desc": "Curved glass (or bent glass) is processed by heating the glass to its softening point and then molding it into a curved shape using gravity or mechanical forces. It can be further treated to be annealed, tempered, or laminated. Curved glass introduces flowing lines and organic shapes to architecture, breaking the monotony of straight lines and offering a modern, sophisticated look.",
        "features": [
            "<strong>Aesthetic Appeal:</strong> Adds elegance and fluidity to architectural designs.",
            "<strong>Customization:</strong> Available in various radii and shapes (cylindrical, spherical).",
            "<strong>Strength:</strong> Curved tempered glass retains high structural strength.",
            "<strong>Panoramic Views:</strong> Offers uninterrupted, wider viewing angles.",
            "<strong>Versatility:</strong> Can be combined with other glass technologies (IGU, laminated)."
        ],
        "applications": [
            "Curved facades, spiral staircases, glass elevators.",
            "Revolving doors, rounded corners in buildings.",
            "Shower enclosures, curved partitions.",
            "Display counters, aquarium tanks.",
            "Automotive glass."
        ]
    },
    {
        "slug": "acid-etched-glass",
        "name": "Acid Etched Glass",
        "short_desc": "Acid etched glass is treated with hydrofluoric acid to create a beautiful, smooth, and uniform matte surface.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Acid etched glass is float glass that has been treated with hydrofluoric acid to permanently etch one or both surfaces. This process creates a smooth, satin-like matte finish that diffuses light while reducing transparency. Unlike sandblasting, acid etching produces a smoother, easier-to-clean surface that does not show fingerprints or retain dirt as easily.",
        "features": [
            "<strong>Smooth Finish:</strong> Satiny, soft touch surface that resists fingerprints.",
            "<strong>Uniformity:</strong> Consistent frosted appearance without the blotchiness of sandblasting.",
            "<strong>Durability:</strong> The finish is permanent and will not peel or wear off.",
            "<strong>Light Diffusion:</strong> Softens and spreads light evenly, reducing glare.",
            "<strong>Privacy:</strong> Obscures visibility while allowing natural light to enter."
        ],
        "applications": [
            "Interior partitions, office dividers.",
            "Shower doors, bathroom windows.",
            "Furniture components (tabletops, cabinet doors).",
            "Balustrades, railings.",
            "Signage and decorative features."
        ]
    },
    {
        "slug": "sandblasted-glass",
        "name": "Sandblasted Glass",
        "short_desc": "Sandblasted glass is treated with high-pressure sandblasting technology to create patterns and logos.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Sandblasted glass is produced by blasting silica sand or other abrasive materials at high pressure onto the surface of the glass. This erodes the surface, creating a rough, frosted look. Sandblasting allows for high precision and is ideal for creating intricate designs, detailed geometric patterns, corporate logos, or artistic murals on glass.",
        "features": [
            "<strong>Design Flexibility:</strong> Capable of creating complex, custom patterns and gradients.",
            "<strong>Privacy Control:</strong> Varying degrees of opacity can be achieved.",
            "<strong>Durability:</strong> The design is physically etched into the glass.",
            "<strong>Cost-Effective:</strong> economical method for custom decorative glass.",
            "<strong>Lighting Effects:</strong> Can be edge-lit to make the etched design glow."
        ],
        "applications": [
            "Corporate logo branding on glass doors.",
            "Decorative partitions in restaurants and hotels.",
            "Privacy bands on office glazing.",
            "Artistic glass panels.",
            "Signage and wayfinding."
        ]
    },
    {
        "slug": "ceramic-fritted-glass",
        "name": "Ceramic Fritted Glass",
        "short_desc": "Ceramic fritted glass is printed directly onto the glass surface with ceramic ink, then fired at high temperatures.",
        "img_file": "kinh-in-men.jpg",
        "long_desc": "Ceramic fritted glass (also known as silk-screened or ceramic printed glass) involves applying ceramic frit (paint) to the glass surface through a screen or digital printer containing a specific design. The glass is then fired in a tempering furnace, fusing the frit to the glass surface. The result is a highly durable, scratch-resistant, and decorative glass product.",
        "features": [
            "<strong>Exemplary Permanence:</strong> The ceramic ink becomes part of the glass; it will not scratch, fade, or peel.",
            "<strong>Color Variety:</strong> Available in a wide range of colors and opacities.",
            "<strong>Solar Control:</strong> Reduces glare and solar heat gain depending on the pattern density.",
            "<strong>Safety:</strong> Is typically tempered or heat-strengthened.",
            "<strong>Eco-Friendly:</strong> Ceramic inks are free of lead and harmful heavy metals."
        ],
        "applications": [
            "Exterior building facades (spandrel glass).",
            "Curtain walls, overhead glazing.",
            "Interior wall cladding, kitchen backsplashes.",
            "Decorative Balustrades.",
            "Public art installations."
        ]
    },
    {
        "slug": "nano-coated-glass",
        "name": "Nano Coated Glass",
        "short_desc": "Nano coated glass has a self-cleaning surface that repels water and dust.",
        "img_file": "kinh-phu-nano.jpg",
        "long_desc": "Nano coated glass features an ultra-thin, transparent coating of nano-particles that provides hydrophobic (water-repellent) and oleophobic (oil-repellent) properties. When water hits the surface, it beads up and rolls off, taking dirt and grime with it (lotus effect). This significantly reduces mineral deposits (like limestone), soap scum, and water spots, keeping the glass cleaner for longer.",
        "features": [
            "<strong>Easy Cleaning:</strong> Reduces cleaning time and frequency by up to 90%.",
            "<strong>Water Repellent:</strong> improved visibility in wet conditions.",
            "<strong>Anti-Corrosion:</strong> Protects glass from etching by hard water, salt spray, and pollutants.",
            "<strong>Durability:</strong> Resistant to UV rays, abrasion, and temperature extremes.",
            "<strong>Eco-Friendly:</strong> Reduces the need for harsh chemical cleaners."
        ],
        "applications": [
            "Shower cabins and glass bathroom enclosures.",
            "Exterior windows and facades in high-rise buildings.",
            "Marine glass (boats, yachts).",
            "Solar panels (to maintain efficiency).",
            "Automotive windshields and mirrors."
        ]
    },
    {
        "slug": "patterned-glass",
        "name": "Patterned Glass",
        "short_desc": "Patterned glass creates decorative patterns and textures, providing privacy and aesthetics.",
        "img_file": "kinh-in-hoa-van-mo-3.jpg",
        "long_desc": "Patterned glass, also known as textured or rolled glass, is made by passing molten glass between rollers, one of which carries a pattern. This imprints a distinct texture onto one or both sides of the glass. The texture diffuses light and obscures detailed vision, offering a balance between transparency, privacy, and decorative appeal.",
        "features": [
            "<strong>Decorative:</strong> Adds visual interest and vintage or modern style to interiors.",
            "<strong>Privacy:</strong> Distorts the view while still allowing light transmission.",
            "<strong>Variety:</strong> Available in many classic and contemporary textures (reeded, fluted, rain, hammered).",
            "<strong>Processable:</strong> Can be toughened/tempered for safety applications.",
            "<strong>Light Diffusion:</strong> Softens harsh sunlight."
        ],
        "applications": [
            "Cabinet doors, kitchen cupboards.",
            "Interior doors and partitions.",
            "Shower screens.",
            "Lighting fixtures.",
            "Office dividers and meeting rooms."
        ]
    },
     {
        "slug": "ultra-clear-glass",
        "name": "Ultra Clear Glass",
        "short_desc": "Ultra clear glass (Low-Iron) offers maximum transparency and true color transmission.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Ultra Clear Glass, or Low-Iron Glass, is manufactured with a reduced iron content compared to standard clear float glass. This elimination of iron removes the characteristic greenish tint seen in standard glass, especially at the edges. The result is a crystal-clear glass with exceptional clarity and high light transmission, allowing the true colors of objects behind or coated on the glass to shine through.",
        "features": [
            "<strong>Exceptional Clarity:</strong> Virtually colorless with high light transmission (>91%).",
            "<strong>True Color Rendering:</strong> Does not distort colors; ideal for displays and color-critical applications.",
            "<strong>Premium Aesthetic:</strong> Provides a clean, invisible, and high-end look.",
            "<strong>Bright Edges:</strong> Edges appear ice-blue or clear instead of dark green.",
            "<strong>Versatile:</strong> Can be laminated, tempered, or painted."
        ],
        "applications": [
            "Museum display cases and jewelry counters.",
            "High-end retail storefronts.",
            "Aquariums and terrariums.",
            "Back-painted glass (ensures true color match).",
            "Solar energy collectors."
        ]
    },
    {
        "slug": "reflective-glass",
        "name": "Reflective Glass",
        "short_desc": "Reflective glass is coated with a metal oxide layer that reflects light, reducing heat and glare.",
        "img_file": "kinh-phan-quang.jpg",
        "long_desc": "Reflective glass is created by applying a metallic reflective coating during the float glass manufacturing process. This coating gives the glass a mirror-like appearance from the outside, reflecting a significant portion of incoming solar radiation. It provides excellent solar control and glare reduction while offering a one-way mirror effect for privacy during daylight hours.",
        "features": [
            "<strong>Solar Control:</strong> Reflects heat, reducing cooling loads in buildings.",
            "<strong>Glare Reduction:</strong> Improves visual comfort for occupants.",
            "<strong>Daytime Privacy:</strong> Prevents outsiders from seeing in during the day.",
            "<strong>Aesthetics:</strong> Available in various colors (bronze, grey, green, blue) for striking exterior designs.",
            "<strong>UV Filtering:</strong> Reduces transmission of harmful UV rays."
        ],
        "applications": [
            "Skyscrapers and office building facades.",
            "Curtain walls.",
            "Windows exposed to intense direct sunlight.",
            "Roof glazing and atriums."
        ]
    },
    {
        "slug": "low-e-glass",
        "name": "Low-E Glass",
        "short_desc": "Low-E glass minimizes UV and infrared light while maintaining brightness, saving energy.",
        "img_file": "kinh-low-e.jpg",
        "long_desc": "Low Emissivity (Low-E) glass has a microscopically thin, transparent coating that reflects long-wave infrared heat. In winter, it reflects internal heat back into the room, keeping it warm. In summer, it reflects external solar heat away, keeping interiors cool. It does this while still letting in visible light, making it the standard for energy-efficient modern architecture.",
        "features": [
            "<strong>Thermal Insulation:</strong> Drastically improves the U-value of windows.",
            "<strong>Energy Savings:</strong> Reduces dependence on HVAC systems year-round.",
            "<strong>Comfort:</strong> Eliminates cold spots near windows and drafts.",
            "<strong>Fade Protection:</strong> Blocks UV radiation to protect furniture and carpets.",
            "<strong>High Light Transmission:</strong> Keeps interiors bright and airy."
        ],
        "applications": [
            "Residential windows and doors.",
            "Commercial office buildings.",
            "Schools and hospitals.",
            "Garden rooms and conservatories."
        ]
    },
    {
        "slug": "solar-control-glass",
        "name": "Solar Control Glass",
        "short_desc": "Optimal solar energy control glass, reducing air conditioning costs.",
        "img_file": "kinh-hop-solar.png",
        "long_desc": "Solar Control glass is designed to allow sunlight to pass through a window or facade while radiating and reflecting away a large degree of the sun's heat. It typically uses advanced soft-coat or hard-coat technologies. Unlike standard Low-E glass which focuses on thermal insulation, Solar Control glass is specifically optimized to block solar heat gain (g-value), making it ideal for hot climates or large glazed areas.",
        "features": [
            "<strong>Heat Rejection:</strong> Blocks up to 70% of solar heat gain.",
            "<strong>Cost Efficiency:</strong> Significantly lowers air conditioning usage.",
            "<strong>Visual Comfort:</strong> Reduces eye strain by controlling glare.",
            "<strong>Appearance:</strong> Available in neutral tints or reflective finishes.",
            "<strong>Performance:</strong> Can be used in single glazing or IGU configurations."
        ],
        "applications": [
            "Large glazed facades and curtain walls.",
            "Atriums and skylights.",
            "Conservatories and sunrooms.",
            "Commercial buildings in hot climates."
        ]
    },
    {
        "slug": "tinted-glass",
        "name": "Tinted Glass",
        "short_desc": "Tinted glass is colored during production, absorbing heat and offering visual appeal.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Tinted glass (body-tinted glass) is produced by adding small amounts of metal oxides to the glass composition during the melting process. This gives the glass a uniform color throughout its thickness. Tinted glass absorbs a significant amount of solar energy, reducing heat transmission, and also cuts down on glare. Common colors include grey, bronze, green, and blue.",
        "features": [
            "<strong>Solar Absorption:</strong> Absorbs 30-50% of solar heat, reducing internal temperatures.",
            "<strong>Glare Control:</strong> Softens harsh bright light for a more comfortable interior environment.",
            "<strong>Privacy:</strong> darker tints provide increased privacy.",
            "<strong>Aesthetics:</strong> Adds color and character to the building exterior.",
            "<strong>UV Protection:</strong> Filters out UV radiation."
        ],
        "applications": [
            "Windows and doors in residential and commercial buildings.",
            "Automotive windows.",
            "Tabletops and furniture.",
            "Internal partitions.",
            "Decorative facades."
        ]
    },
    {
        "slug": "mirror-glass",
        "name": "Mirror Glass",
        "short_desc": "High-quality silver-coated glass for sharp reflection and interior expansion.",
        "img_file": "kinh-guong.jpg",
        "long_desc": "Mirror glass is produced by coating a silver layer, a copper layer, and waterproof paint on the back of float glass. This process creates a highly reflective surface. Quality mirrors use high-grade float glass to ensure a distortion-free reflection. Mirrors are an essential element in interior design, used not just for grooming but to create the illusion of space and reflect light.",
        "features": [
            "<strong>High Reflectivity:</strong> Clear, bright, and distortion-free images.",
            "<strong>Durability:</strong> Multi-layer coating protects against corrosion and moisture (especially in bathrooms).",
            "<strong>Space Enhancement:</strong> Makes small rooms appear larger and brighter.",
            "<strong>Variety:</strong> Available in silver, bronze, grey, antique, and tinted finishes.",
            "<strong>Safety Options:</strong> Can be backed with safety film to hold fragments if broken."
        ],
        "applications": [
            "Bathrooms and dressing rooms.",
            "Wall cladding in gyms, dance studios, and lobbies.",
            "Wardrobe doors.",
            "Decorative furniture overlays.",
            "Retail fitting rooms."
        ]
    },
    {
        "slug": "smart-film-glass",
        "name": "Smart Film Glass",
        "short_desc": "Smart glass switches between transparent and opaque states using electric current.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Smart Film Glass (Switchable Privacy Glass) utilizes Polymer Dispersed Liquid Crystal (PDLC) technology. When electricity is applied, the liquid crystals align, and the glass becomes transparent. When the power is off, the crystals scatter, creating an opaque, frosted privacy barrier. This allows for instant privacy control at the flick of a switch, eliminating the need for blinds or curtains.",
        "features": [
            "<strong>Instant Privacy:</strong> Switch from clear to frosted in milliseconds.",
            "<strong>Modern Aesthetic:</strong> minimalist, high-tech look without bulky window treatments.",
            "<strong>Projection Screen:</strong> Can be used as a high-definition rear projection screen when opaque.",
            "<strong>Sound & Heat Insulation:</strong> Offers benefits similar to laminated glass.",
            "<strong>Control Options:</strong> Can be operated via wall switch, remote, app, or voice control."
        ],
        "applications": [
            "Conference room partitions.",
            "Hospital privacy screens (ICU, ER).",
            "Luxury hotel bathroom pods.",
            "Residential windows and skylights.",
            "Retail display cases."
        ]
    },
    {
        "slug": "fabric-laminated-glass",
        "name": "Fabric Laminated Glass",
        "short_desc": "A sophisticated combination of safety glass and art fabric layers for unique interiors.",
        "img_file": "kinh-ghep-vai.jpg",
        "long_desc": "Fabric laminated glass encapsulates varied fabrics, metallic meshes, or textiles between layers of glass and protective interlayers. This process preserves the delicate beauty and texture of the fabric while transforming it into a durable, easy-to-clean surfacing material. It offers endless design possibilities by combining the safety of laminated glass with the richness of textiles.",
        "features": [
            "<strong>Unique Design:</strong> Limitless variety of fabric colors, textures, and patterns.",
            "<strong>Protection:</strong> Keeps the fabric clean, dry, and protected from UV fading.",
            "<strong>Safety:</strong> Structural integrity of laminated glass.",
            "<strong>Versatility:</strong> Can be used for varying levels of transparency and privacy.",
            "<strong>Hygiene:</strong> Easy to clean surface compared to exposed fabric."
        ],
        "applications": [
            "Feature walls and partitions.",
            "Elevator interiors.",
            "Furniture cladding / Table tops.",
            "Doors and sliding panels.",
            "Backlit architectural features."
        ]
    }
]

if not os.path.exists("source/en/products"):
    os.makedirs("source/en/products")

for product in products_data:
    filename = f"source/en/products/{product['slug']}.html"
    
    features_html = create_list_html(product['features'])
    applications_html = create_list_html(product['applications'])
    
    content = f"""@@include('header-product-en.htm')

@@include('blocks/navigation-product-en.htm')

<section class="page-title bg-1">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="block text-center">
          <span class="text-white">Product Details</span>
          <h1 class="text-capitalize mb-4 text-lg">{product['name']}</h1>
          <ul class="list-inline">
            <li class="list-inline-item"><a href="../index.html" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="../products.html" class="text-white">Products</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">{product['name']}</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section blog-details">
    <div class="container">
        <div class="row">
            <div class="col-lg-10 offset-lg-1">
                <article class="post">
                    <div class="post-image mb-5 text-center">
                        <img loading="lazy" class="img-fluid" style="max-height: 500px; width: auto;" src="../../images/products/{product['img_file']}" alt="{product['name']}">
                    </div>
                    <div class="post-content">
                        <h3 class="mb-3">{product['name']}</h3>
                        
                        <div class="mb-5 text-justify" style="font-size: 1.1rem; color: #555;">
                            {product['long_desc']}
                        </div>

                        <div class="row mb-5 w-100 mx-0">
                            <div class="col-12 col-md-6 mb-4 mb-md-0">
                                <div class="p-4 bg-light rounded border">
                                    <h4 class="mb-4 text-dark"><i class="tf-ion-ios-star mr-2 text-warning"></i>Key Features</h4>
                                    <ul class="list-unstyled">
                                        {features_html}
                                    </ul>
                                </div>
                            </div>
                            <div class="col-12 col-md-6">
                                <div class="p-4 bg-light rounded border">
                                    <h4 class="mb-4 text-dark"><i class="tf-ion-ios-lightbulb mr-2 text-warning"></i>Applications</h4>
                                    <ul class="list-unstyled">
                                        {applications_html}
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div class="alert alert-success mt-4" role="alert">
                           <h5 class="alert-heading mb-2"><i class="tf-ion-ios-telephone mr-2"></i>Contact for Quote</h5>
                           <p class="mb-0">Interested in <strong>{product['name']}</strong>? Please contact our Hotline directly for expert consultation on dimensions, specifications, and the best pricing.</p>
                        </div>
                        
                        <div class="mt-4 text-center">
                             <a href="../contact.html" class="btn btn-main">Request Quote</a>
                             <a href="tel:+84837923996" class="btn btn-solid-border ml-2">Call Now: (+84) 83 792 3996</a>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        
        <div class="row mt-5">
            <div class="col-12">
                <div class="title text-center">
                    <h2>Other Products</h2>
                    <div class="border"></div>
                </div>
            </div>
            
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../../images/products/kinhcuongluc.jpg" alt="Tempered Glass">
                        <div class="overlay">
                            <a href="tempered-glass.html" class="btn-view">View Details</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="tempered-glass.html">Tempered Glass</a></h4>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../../images/products/kinh-cuong-luc-2-lop-3.jpg" alt="Laminated Glass">
                        <div class="overlay">
                            <a href="laminated-glass.html" class="btn-view">View Details</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="laminated-glass.html">Laminated Glass</a></h4>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../../images/products/kinh-hop-an-toan.jpg" alt="Insulated Glass">
                        <div class="overlay">
                            <a href="insulated-glass.html" class="btn-view">View Details</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="insulated-glass.html">Insulated Glass</a></h4>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

@@include('en/blocks/footer-product.htm')
@@include('footer-scripts-product-en.htm')
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Created English product pages with Full Content.")
