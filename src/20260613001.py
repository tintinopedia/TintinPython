customer_name = str(input("Enter your name: "))
money = float(input("Enter pocket money 💴 "))
def show_menu():
    print("Toy menu")
    print("1.Teddy bear = 120 💴")
    print("2.Toy car = 80 💴")
    print("3.Ball = 50 💴")
    print("4.Exit")
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You have chosen teddy bears.🧸 ")
        qty = int(input("Enter how many teddy bears you want?? 🧸"))
        bill = 120 * qty
        if money >= bill:
            money = money - bill
            print("Now your new available balance is ",money)
        else:
            print("Insufficient balance")
    elif choice == 2:
        print("You have chosen toy cars.🚘")
        qty = int(input("Enter how many cars you want?? 🚘"))
        bill = 80 * qty
        if money >= bill:
            money = money - bill
            print("Your new available balance is ",money)
        else:
            print("Insufficient balance")
    elif choice == 3:
        print("You have chosen balls.🥎")
        qty = int(input("Enter how many balls you want??"))
        bill = 50 * qty
        if money >= bill:
            money = money - bill
            print("Your new balance is ",money)
        else:
            print(f"insufficient money. ")
    elif choice == 4:
        print(f"Bye bye 👋 {customer_name}!!! Have a nice day 😊")
        break
    else:
        print("Invalid choice.please try again.")