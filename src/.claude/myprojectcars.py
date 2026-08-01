brands_and_models = {
    "Maruti Suzuki": [
        "Alto K10", "Wagon R", "Celerio", "Swift", "Baleno", "Dzire", "Ciaz",
        "S-Presso", "Brezza", "Fronx", "Grand Vitara", "Jimny", "Ertiga",
        "XL6", "Ignis", "S-Cross", "Ritz", "Zen", "SX4", "A-Star", "Estilo"
    ],
    "Tata Motors": [
        "Tiago", "Altroz", "Tigor", "Punch", "Nexon", "Curvv", "Harrier",
        "Safari", "Indica", "Indigo", "Hexa", "Aria", "Zest", "Bolt", "Nano"
    ],
    "Mahindra": [
        "Thar", "Thar Roxx", "Scorpio-N", "Scorpio Classic", "XUV700", "XUV3XO",
        "XUV400", "Bolero", "Bolero Neo", "XUV500", "XUV300", "TUV300", "Marazzo"
    ],
    "Hyundai": [
        "Grand i10 Nios", "i20", "Aura", "Verna", "Exter", "Venue", "Creta",
        "Alcazar", "Tucson", "Ioniq 5", "Santro", "Eon", "Getz", "Elantra", "Sonata"
    ],
    "Kia": [
        "Sonet", "Seltos", "Carens", "Carnival", "EV6", "EV9", "Syros"
    ],
    "Toyota": [
        "Glanza", "Taisor", "Urban Cruiser Hyryder", "Rumion", "Innova Crysta",
        "Innova Hycross", "Fortuner", "Legender", "Hilux", "Camry", "Vellfire", "Etios"
    ],
    "Honda": [
        "Amaze", "City", "Elevate", "Brio", "Jazz", "Civic", "Accord", "CR-V"
    ],
    "Volkswagen": [
        "Virtus", "Taigun", "Tiguan", "Polo", "Vento", "Jetta", "Passat", "Tayron"
    ],
    "Skoda": [
        "Slavia", "Kushaq", "Kylaq", "Kodiaq", "Rapid", "Octavia", "Superb", "Yeti"
    ],
    "MG Motor": [
        "Comet EV", "Windsor EV", "Astor", "Hector", "Hector Plus", "Gloster", "ZS EV"
    ]
}
# The unique configuration matrices that expand these into distinct car names
fuel_types = ["Petrol", "Diesel", "CNG", "EV"]
transmissions = ["MT", "AMT", "AT", "DCT"]
variants = ["Base", "Mid", "Top", "Luxury"]

# The list container
thousand_indian_cars = []

# Programmatic Expansion Loop
for brand, models in brands_and_models.items():
    for model in models:
        for fuel in fuel_types:
            # Prevent illogical pairings (e.g., historical cars or specific builds without EV/CNG variants)
            if "EV" in model and fuel != "EV":
                continue
            if fuel == "EV" and "EV" not in model and model not in ["Nexon", "Punch", "Tiago", "ZS", "Curvv", "XUV400"]:
                continue
            if fuel == "CNG" and brand not in ["Maruti Suzuki", "Tata Motors", "Hyundai", "Toyota"]:
                continue

            for tx in transmissions:
                # EVs generally don't use Manual or DCT transmissions
                if fuel == "EV" and tx in ["MT", "DCT"]:
                    continue
                # Budget models rarely use high-end DCTs
                if model in ["Alto K10", "Wagon R", "S-Presso", "Kwid", "Nano"] and tx == "DCT":
                    continue

                for var in variants:
                    # Constructing a completely distinct unique model name string
                    full_car_name = f"{brand} {model} {fuel} {tx} ({var} Variant)"
                    thousand_indian_cars.append(full_car_name)

# Slice cleanly to ensure we present exact counts if needed, but the loop builds roughly 1000+
print(f"Successfully generated a unique database array of {len(thousand_indian_cars)} Indian car configurations!")

# Let's inspect a quick sample batch from across the list layout
print("\nFirst 5 entries:")
for car in thousand_indian_cars[:5]:
    print(f"- {car}")

print("\nMiddle 5 entries:")
for car in thousand_indian_cars[500:505]:
    print(f"- {car}")

print("\nLast 5 entries:")
for car in thousand_indian_cars[-5:]:
    print(f"- {car}")
