cars = ["Alto K10", "Wagon R", "Celerio", "Swift", "Baleno",
        "Dzire", "Ciaz", "S-Presso", "Brezza", "Fronx",
        "Grand Vitara", "Jimny", "Ertiga", "XL6", "Eeco",
        "Alto 800", "Maruti 800", "Zen", "Zen Estilo", "Estime",
        "Gypsy", "Omni", "Ritz", "SX4", "A-Star", "Kizashi",
        "Grand Vitara XL7", "S-Cross", "Ignis", "eVitara",

        # --- TATA MOTORS (Current, EVs & Heritage) ---
        "Tiago", "Altroz", "Tigor", "Punch", "Nexon",
        "Curvv", "Harrier", "Safari", "Sierra EV", "Avinya",
        "Tiago EV", "Punch EV", "Nexon EV", "Tigor EV",
        "Indica", "Indigo", "Indigo Manza", "Nano", "Sumo",
        "Safari DICOR", "Safari Storme", "Aria", "Hexa",
        "Zest", "Bolt",

        # --- MAHINDRA & MAHINDRA ---
        "Thar", "Thar Roxx", "Scorpio Classic", "Scorpio-N",
        "Bolero", "Bolero Neo", "XUV3XO", "XUV700", "XUV400",
        "XEV 9e", "BE.05", "Thar e", "XUV500", "XUV300",
        "TUV300", "KUV100 NXT", "Marazzo", "Verito", "Quanto",
        "Scorpio Getaway", "Mahindra Classic", "Commander",

        # --- HYUNDAI INDIA ---
        "Grand i10 Nios", "i20", "i20 N-Line", "Aura", "Verna",
        "Exter", "Venue", "Creta", "Alcazar", "Tucson", "Ioniq 5",
        "Ioniq 6", "Bayon", "Santro", "Getz", "Accent",
        "Elantra", "Sonata", "Santa Fe", "Eon", "Creta EV",

        # --- KIA INDIA ---
        "Sonet", "Seltos", "Carens", "Carnival", "EV6", "EV9",
        "Syros", "Syros EV", "Sorento", "EV4",

        # --- TOYOTA KIRLOSKAR MOTOR ---
        "Glanza", "Camry", "Urban Cruiser Hyryder", "Taisor",
        "Fortuner", "Legender", "Hilux", "Rumion", "Innova Crysta",
        "Innova Hycross", "Vellfire", "Qualis", "Etios",
        "Etios Liva", "Corolla Altis", "Prius", "Land Cruiser",

        # --- HONDA CARS INDIA ---
        "Amaze", "City", "City e:HEV", "Elevate", "Elevate EV",
        "Brio", "Jazz", "Mobilio", "BR-V", "CR-V",
        "Civic", "Accord",

        # --- VOLKSWAGEN & SKODA ---
        "Virtus", "Taigun", "Tiguan", "Tayron", "Tera",
        "Slavia", "Kylaq", "Kushaq", "Kodiaq", "Kodiaq RS",
        "Polo", "Vento", "Jetta", "Passat", "Phaeton",
        "Fabia", "Rapid", "Laura", "Octavia", "Superb", "Yeti",

        # --- MG MOTOR & BYD ---
        "Comet EV", "Windsor EV", "Astor", "Hector", "Hector Plus",
        "Gloster", "ZS EV", "Atto 3", "E6", "Seal", "Seagull",

        # --- RENAULT, NISSAN & CITROËN ---
        "Kwid", "Triber", "Kiger", "Duster", "Arkana",
        "Magnite", "Tekton", "Terrano", "Sunny", "Micra",
        "Patrol", "Teana", "Kicks", "C3", "ë-C3", "C3 Aircross",
        "C5 Aircross", "Basalt",

        # --- FORD & CHEVROLET (Memorable Exits) ---
        "Ikon", "Fiesta", "Figo", "Aspire", "Fusion",
        "EcoSport", "Endeavour", "Mondeo", "Mustang",
        "Optra", "Aveo", "Spark", "Beat", "Cruze",
        "Tavera", "Captiva", "Trailblazer",

        # --- HISTORIC INDIAN ICONS ---
        "Hindustan Ambassador", "Hindustan Contessa",
        "Premier Padmini", "Premier 118NE", "Standard Herald",
        "Sipani Badal", "San Storm",

        # --- FORCE MOTORS & ISUZU ---
        "Gurkha 3-Door", "Gurkha 5-Door", "Force One",
        "D-Max V-Cross", "MU-X",

        # --- LUXURY SEGMENT (Audi, BMW, Mercedes, Volvo, Jaguar, Land Rover) ---
        "A-Class", "C-Class", "E-Class", "S-Class", "GLA", "GLC", "GLE", "GLS", "G-Class", "AMG E 53",
        "2 Series", "3 Series Gran Limousine", "5 Series", "7 Series", "X1", "X3", "X5", "X7", "M2",
        "A4", "A6", "A8 L", "Q3", "Q5", "Q7", "Q8", "e-tron", "Q6 E-Tron",
        "XC40 Recharge", "XC60", "XC90", "EX60", "EX90", "ES90",
        "XE", "XF", "XJ", "E-Pace", "F-Pace", "F-Type", "I-Pace",
        "Evoque", "Discovery Sport", "Discovery", "Defender", "Range Rover Velar", "Range Rover Sport", "Range Rover",

        # --- EXOTIC SUPERCAR & ULTRA-LUXURY BRANDS ---
        "Panamera", "Macan", "Cayenne", "Taycan", "718 Cayman", "718 Boxster", "911 Carrera",
        "Urus", "Huracan", "Revuelto", "Temerario",
        "Roma", "296 GTB", "SF90 Stradale", "Purosangue", "12Cilindri",
        "Vantage", "DBX", "DBS",
        "Ghost", "Phantom", "Cullinan", "Spectre",
        "Flying Spur", "Continental GT", "Bentayga"]
def game_day():
        print("Welcome to the showroom!")
        buyer_money = 900007
        print(f"Buyer money is {buyer_money}")
        choice = str(input("Would you like to buy cars? (y/n): "))
        if choice == "y":
                print("you chose to buy a car. \n")
                fuel_types = str(input("Which type of fuel do you want for your car? choose from these \t \n (Petrol,Diesel,CNG and Electric): \n"))
                if fuel_types == "Petrol":
                        print("you chose to buy a car with fuel == petrol. \n")
                options = str(input(""))

        elif choice == "n":
                print("Bye Bye come again later to buy cars. \n")

