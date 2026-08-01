import csv

# Expanded Global Brands and Models (Over 35+ brands and 280+ models)
global_brands_and_models = {
    # United States
    "Ford": ["F-150", "Mustang", "Explorer", "Escape", "Bronco", "Mach-E", "Maverick", "Ranger", "Edge", "Expedition", "Transit"],
    "Chevrolet": ["Silverado", "Corvette", "Equinox", "Tahoe", "Suburban", "Trax", "Blazer EV", "Colorado", "Malibu", "Traverse"],
    "Tesla": ["Model 3", "Model Y", "Model S", "Model X", "Cybertruck"],
    "Jeep": ["Wrangler", "Grand Cherokee", "Compass", "Gladiator", "Renegade", "Wagoneer"],
    "Cadillac": ["CT4", "CT5", "XT4", "XT5", "Escalade", "Lyriq", "Optiq", "Vistiq", "Celestiq"],
    "GMC": ["Sierra 1500", "Canyon", "Yukon", "Terrain", "Hummer EV"],
    "RAM": ["1500", "2500", "3500", "ProMaster"],
    "Dodge": ["Hornet", "Durango", "Charger Daytona"],
    "Lincoln": ["Corsair", "Nautilus", "Aviator", "Navigator"],
    "Buick": ["Encore GX", "Envista", "Envision", "Enclave"],

    # Japan
    "Toyota": ["Corolla", "Camry", "RAV4", "Highlander", "Tacoma", "Prius", "Land Cruiser", "bZ4X", "4Runner", "Crown", "Sequoia", "Tundra", "GR Supra", "GR86"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "HR-V", "Prologue", "Passport", "Ridgeline", "Odyssey"],
    "Nissan": ["Altima", "Sentra", "Rogue", "Z", "Ariya", "Pathfinder", "Frontier", "Armada", "Versa", "Kicks", "Murano"],
    "Subaru": ["Outback", "Forester", "Crosstrek", "WRX", "Solterra", "Legacy", "Ascent", "BRZ"],
    "Lexus": ["IS", "ES", "RX", "GX", "NX", "RZ", "LS", "LX", "TX", "LC"],
    "Mazda": ["Mazda3", "Mazda6", "CX-30", "CX-5", "CX-50", "CX-70", "CX-90", "MX-5 Miata"],
    "Mitsubishi": ["Outlander", "Outlander Sport", "Eclipse Cross", "Mirage"],
    "Acura": ["Integra", "TLX", "RDX", "MDX", "ZDX"],
    "Infiniti": ["Q50", "QX50", "QX55", "QX60", "QX80"],
    "Suzuki": ["Swift", "Jimny", "Vitara", "Brezza", "Ertiga", "Fronx", "Grand Vitara"],

    # Germany & Europe
    "BMW": ["3 Series", "5 Series", "7 Series", "X1", "X3", "X5", "X7", "i4", "iX", "i7", "Z4", "M3", "M5"],
    "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLA", "GLC", "GLE", "GLS", "EQE", "EQS", "G-Class", "AMG GT"],
    "Audi": ["A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "e-tron GT", "Q4 e-tron"],
    "Volkswagen": ["Golf", "Jetta", "Tiguan", "Atlas", "ID.4", "Taos", "Passat", "ID. Buzz"],
    "Volvo": ["XC40", "XC60", "XC90", "EX30", "EX90", "S60", "S90", "V60"],
    "Porsche": ["911", "718 Cayman", "Panamera", "Macan", "Cayenne", "Taycan"],
    "Jaguar": ["F-TYPE", "F-PACE", "E-PACE", "I-PACE"],
    "Land Rover": ["Defender", "Discovery", "Range Rover", "Range Rover Sport", "Range Rover Evoque", "Velar"],
    "Alfa Romeo": ["Giulia", "Stelvio", "Tonale"],
    "Fiat": ["500e", "500X", "Panda", "Pulse", "Fastback"],
    "Peugeot": ["208", "308", "2008", "3008", "5008"],
    "Renault": ["Clio", "Megane E-Tech", "Captur", "Austral", "Koleos", "Duster"],
    "Mini": ["Cooper", "Countryman", "Aceman"],

    # South Korea
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe", "Palisade", "Ioniq 5", "Ioniq 6", "Kona", "Venue", "Santa Cruz"],
    "Kia": ["Forte", "K5", "Sportage", "Telluride", "EV6", "EV9", "Seltos", "Sorento", "Soul", "Carnival"],
    "Genesis": ["G70", "G80", "G90", "GV70", "GV80", "GV60"],

    # China
    "BYD": ["Atto 3", "Seal", "Dolphin", "Han", "Tang", "Seagull", "Song Plus", "Yuan Plus"],
    "NIO": ["ET5", "ET7", "ES6", "ES8", "EC6", "EC7", "ET9"],
    "XPeng": ["P7", "G6", "G9", "P5", "X9"],
    "Geely": ["Coolray", "Monjaro", "Geometry C", "Tugella"],
    "MG": ["MG4 EV", "MG ZS", "MG5", "MG HS", "Cyberster"],
    "Zeekr": ["001", "007", "009", "X"],

    # India
    "Tata Motors": ["Nexon", "Harrier", "Safari", "Punch", "Curvv", "Tiago", "Tigor", "Altroz"],
    "Mahindra": ["Thar", "Scorpio-N", "XUV700", "XUV300", "Bolero"],
    "Maruti Suzuki": ["Brezza", "Baleno", "Swift", "Ertiga", "Dzire", "Fronx", "Grand Vitara"]
}

# Regional Configurations
fuel_types = ["Petrol", "Diesel", "Hybrid", "EV"]
transmissions = ["Manual", "Automatic", "Dual-Clutch (DCT)"]
trim_levels = ["Base", "Mid / Sport", "Top / Limited", "Performance / Luxury"]

# Model Base Anchor Prices (USD)
base_prices_usd = {
    # Budget / City Cars
    "Seagull": 10300, "Punch": 7300, "Dolphin": 16500, "Nexon": 9800, "Corolla": 22050,
    "Civic": 24200, "Elantra": 22500, "Forte": 20000, "Trax": 20500, "Sentra": 21000,
    "Versa": 16500, "Kicks": 21000, "Venue": 19800, "Soul": 20100, "Swift": 14000,
    "Tiago": 7000, "Baleno": 8500, "Dzire": 8000, "Mirage": 16800,

    # Compact & Mid-Size SUVs / Sedans
    "RAV4": 28600, "CR-V": 30100, "Tucson": 27500, "Sportage": 27000, "CX-5": 29300,
    "Camry": 28400, "Accord": 27800, "Sonata": 27500, "Thar": 15500, "XUV700": 19500,
    "Maverick": 24000, "Mustang": 30920, "Outback": 28800, "Forester": 29700, "Crosstrek": 25100,
    "HR-V": 24600, "Rogue": 28300, "CX-30": 24900, "Seltos": 24400, "Compass": 25900,

    # Premium & Luxury
    "Model 3": 38990, "Model Y": 44990, "3 Series": 45500, "C-Class": 47000, "A4": 44100,
    "IS": 41200, "ES": 43200, "RX": 49900, "G70": 41500, "XC60": 46900, "TLX": 45000,
    "CT4": 35000, "CT5": 38500, "Q5": 45300, "X3": 46900, "GLC": 47500,

    # Trucks / Large SUVs / Executive
    "F-150": 37000, "Silverado": 38000, "Tacoma": 36200, "Wrangler": 32500, "Bronco": 39600,
    "5 Series": 58200, "E-Class": 62500, "X5": 65700, "GLE": 62650, "G80": 54400,
    "Telluride": 36000, "Palisade": 36500, "Tahoe": 56200, "Land Cruiser": 56000,
    "Escalade": 82000, "Yukon": 58000, "Range Rover": 107400, "Defender": 56400,

    # High Luxury / Supercars / EV Flags
    "S-Class": 117300, "7 Series": 96400, "Corvette": 68300, "Model S": 74990, "Model X": 79990,
    "Cybertruck": 79990, "Ioniq 5": 41800, "EV6": 48700, "Atto 3": 19800, "Seal": 31000,
    "911": 114400, "Taycan": 99400, "Hummer EV": 98800, "Celestiq": 340000, "AMG GT": 134900
}

global_cars_db = []

for brand, models in global_brands_and_models.items():
    for model in models:
        # Fetch base anchor price (Default to $35,000 for unspecified models)
        anchor_price = base_prices_usd.get(model, 35000)

        for fuel in fuel_types:
            # Rule: Dedicated EVs must only produce EV fuel entries
            is_pure_ev_badge = (
                    "EV" in model or brand in ["Tesla", "NIO", "XPeng", "Zeekr"] or
                    model in [
                        "Mach-E", "Ioniq 5", "Ioniq 6", "EV6", "EV9", "ID.4", "ID. Buzz",
                        "EX30", "EX90", "bZ4X", "Solterra", "Ariya", "Atto 3", "Seal",
                        "Dolphin", "Seagull", "Prologue", "e-tron GT", "Q4 e-tron",
                        "Lyriq", "Optiq", "Vistiq", "Celestiq", "Hummer EV", "Taycan",
                        "I-PACE", "500e", "Megane E-Tech", "MG4 EV", "Aceman", "Cyberster"
                    ]
            )

            if is_pure_ev_badge and fuel != "EV":
                continue

            for tx in transmissions:
                # Rule: EVs use single-speed automatics (no Manual or DCT)
                if fuel == "EV" and tx in ["Manual", "Dual-Clutch (DCT)"]:
                    continue

                for trim in trim_levels:
                    # Dynamic Pricing Logic Algorithm
                    calculated_price = anchor_price

                    # 1. Powertrain adjustment
                    if fuel == "Hybrid":
                        calculated_price += 2200
                    elif fuel == "EV" and not is_pure_ev_badge:
                        calculated_price += 6500

                    # 2. Gearbox adjustment (skip automatic markup on pure single-speed EVs)
                    if fuel != "EV":
                        if tx == "Automatic":
                            calculated_price += 1400
                        elif tx == "Dual-Clutch (DCT)":
                            calculated_price += 2200

                    # 3. Trim level adjustment
                    if trim == "Mid / Sport":
                        calculated_price += 3200
                    elif trim == "Top / Limited":
                        calculated_price += 7500
                    elif trim == "Performance / Luxury":
                        calculated_price += 14000

                    # Record formatting
                    full_name = f"{brand} {model} {fuel} {tx} ({trim})"
                    record = {
                        "Brand": brand,
                        "Model": model,
                        "Fuel Type": fuel,
                        "Transmission": tx,
                        "Trim Level": trim,
                        "Full Car Name": full_name,
                        "Est. MSRP (USD)": f"${calculated_price:,}"
                    }
                    global_cars_db.append(record)

print(f"Successfully generated {len(global_cars_db):,} unique car configurations with pricing data!\n")

# Helper function to print records cleanly in terminal without pandas
def print_sample_table(records):
    header = f"{'Full Car Name':<55} | {'Est. MSRP (USD)':<15}"
    print(header)
    print("-" * len(header))
    for row in records:
        print(f"{row['Full Car Name']:<55} | {row['Est. MSRP (USD)']:<15}")

# Display representative samples from the dataset
print("=== Head Sample (Budget / Compacts) ===")
print_sample_table(global_cars_db[:5])

print("\n=== Mid-Range Sample (SUVs / Luxury) ===")
print_sample_table(global_cars_db[5000:5005])

print("\n=== Tail Sample (Supercars / EVs) ===")
print_sample_table(global_cars_db[-5:])

# Save to CSV using Python's built-in csv module
csv_filename = "global_cars_with_pricings.csv"
fieldnames = ["Brand", "Model", "Fuel Type", "Transmission", "Trim Level", "Full Car Name", "Est. MSRP (USD)"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(global_cars_db)

print(f"\nSaved enlarged dataset to '{csv_filename}'")