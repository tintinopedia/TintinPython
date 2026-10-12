from dataclasses import dataclass

print("Welcome to the Luxury car manegment! \n")
garage = {
    "BMW": {"price": 6500000, "qty": 3},
    "Audi": {"price": 5500000, "qty": 2},
    "Tesla": {"price": 7200000, "qty": 5}
}

def display_cars():
    print("__________________________AVAILABLE CARS_________________________________")
    for key,value in garage.items():
        print(key, ":", value)

def search_car():
    car = input("Enter car name: \n")

    details = garage.get(car)

    if details:
        print("car found")
        print("Price: ", details["price"])
        print("Quantity: ", details["qty"])
    else:
        print("car not found")
def add_car():
    car = input("Enter car name: \n")

    if car in garage:
        new_price = int(input("Enter New Price : "))
        garage[car].update({"price": new_price})
        print("Price updated")
    else:
        car_input = input("Enter car name: ")
        car_price = int(input("Enter New Price : "))
        car_qty = int(input("Enter Quantity : "))
        garage[car_input] = {"price": car_price, "qty": car_qty}
def update_price():
    car = input("Enter Car Name : ")

    if car in garage:
        new_price = int(input("Enter New Price : "))

        garage[car].update({
            "price": new_price
        })

        print("✅ Price Updated")
    else:
        print("❌ Car Not Found")
def sell_car():
    car = input("Enter car name: \n")
    if car in garage:
        qty = int(input("Enter Quantity to buy: "))
        if garage[car]["qty"] >= qty:
            total = garage[car]["price"] * qty
            garage[car] ["qty"] = garage[car]["qty"] - qty
            print("\nCar Sold Successfully")
            print("Total Price =", total)
            print("Remaining Quantity =", garage[car]["qty"])

            if garage[car]["qty"] == 0:
                print("⚠ Out of Stock")
            else:
                print("✅ Available")

        else:
            print("Not Enough Stock")

    else:
        print("Car Not Found")
def delete_car():
    car = input("Enter Car Name : ")

    if car in garage:

        choice = input("Use pop() or del ? (pop/del) : ")

        if choice.lower() == "pop":
            garage.pop(car)
            print("Car Deleted using pop()")

        else:
            del garage[car]
            print("Car Deleted using del")

    else:
        print("Car Not Found")
def dictionary_methods():
    print("Keys")
    print(garage.keys())

    print("\nValues")
    print(garage.values())

    print("\nItems")
    print(garage.items())
def garage_statistics():
    total_qty = 0
    total_value = 0

    expensive_car = ""
    cheap_car = ""

    max_price = -1
    min_price = 999999999999

    for car, details in garage.items():
        total_qty = total_qty + details["qty"]
        total_value = total_value + details["price"] * details["qty"]
        if details["price"] > max_price:
            max_price = details["price"]
            expensive_car = car

        if details["price"] < min_price:
            min_price = details["price"]
            cheap_car = car

    print("\n========== GARAGE STATISTICS ==========")

    print("Total Quantity =", total_qty)

    print("\nMost Expensive Car")
    print(expensive_car)
    print(max_price)
    print("\nCheapest Car")
    print(cheap_car)
    print(min_price)

    print("\nTotal Garage Value =", total_value)
def search_budget():
    budget = int(input("Enter budget : "))
    found = False
    print("Cars Under Budget")
    for car, details in garage.items():
        if details["price"] <= budget:
            print(car,"-",details["qty"])
            found = True
    if not found:
        print("No cars found")
def Discount_Calculator():
    car = input("Enter car name: \n")
    if car in garage:
        discount = float(input("Enter Discount % : \n"))
        original = garage[car]["price"]
        discount_amount = original * discount / 100
        final_price = original - discount_amount
        print("\nOriginal Price =", original)
        print("Discount Amount =", discount_amount)
        print("Final Price =", final_price)

    else:
        print("Car Not Found")
while True:
    print("\n===================================")
    print("🏎️ LUXURY CAR GARAGE")
    print("===================================")
    print("1. Display All Cars")
    print("2. Search Car")
    print("3. Add New Car")
    print("4. Update Car Price")
    print("5. Sell Car")
    print("6. Delete Car")
    print("7. Show Dictionary Methods")
    print("8. Garage Statistics")
    print("9. Search By Budget")
    print("10. Discount Calculator")
    print("11. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        display_cars()

    elif choice == 2:
        search_car()

    elif choice == 3:
        add_car()

    elif choice == 4:
        update_price()

    elif choice == 5:
        sell_car()

    elif choice == 6:
        delete_car()

    elif choice == 7:
        dictionary_methods()

    elif choice == 8:
        garage_statistics()

    elif choice == 9:
        search_budget()

    elif choice == 10:
       Discount_Calculator()

    elif choice == 11:
        print("🙏 Thank You for Using Luxury Car Garage System!")
        break

    else:
        print("❌ Invalid Choice")