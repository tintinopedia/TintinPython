def bank():
    print("Welcome to the Bank!! ")
    name = str(input("Enter your name: "))
    extra_money = 6848
    pay = extra_money
    print(f"Hello {name}!!")
    print(f"Your extra money is {extra_money}")
    print("Notice: \n \t")
    print("You can buy any thing from your money which is given to you. 💴")
    buy = str(input("What do you want to buy? (options: Tyres = 3415 New Car 🛻 = 6743)\n"))
    if buy == "Tyres":
        print("You chose tyres. 🛞")
        tyre = str(input("What kind of tyre do you want to buy? Soft = 4999,Medium = 3246 and Hard = 2186. \n"))
        if tyre == "Soft":
            print("You chose soft.")
            pay = pay-extra_money
            print(f"You have {extra_money} left. ")
        elif tyre == "Medium":

        elif pay > extra_money:
            print("You have less money to buy. ")
        elif tyre == "Hard":
            print("You chose hard.")
    print("Welcome to the bissness section!! ")
    sell = str(input("What do you want to sell? "))
    price = int(input("How much do you want to sell it for?"))
    print(f"You sell {sell} for {price}")