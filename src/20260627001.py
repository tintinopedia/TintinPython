def bank():
    print("Welcome to the Bank!! ")
    name = str(input("Enter your name: "))
    extra_money = 6848
    left_money = 0
    print(f"Hello {name}!!")
    print(f"Your extra money is {extra_money}")
    print("Notice: \n \t")
    print("You can buy any thing from your money which is given to you. 💴")
    buy = str(input("What do you want to buy? (options: Tyres = 3415 New Car 🛻 = 6743)\n"))
    if buy == "Tyres":
        print("You chose tyres. 🛞")
        tyre = str(input("What kind of tyre do you want to buy? Soft = 4999,Medium = 3246 and Hard = 2186. \n"))
        if tyre == "Soft":
            print("You chose soft that is for 4999. \n")
            left_money = extra_money-4999
            print(f"You have {left_money} left. ")
        elif tyre == "Medium":
            print("You chose medium that is for 3246. \n")
            left_money = extra_money-3246
            print(f"You have {left_money} left. ")
        elif tyre == "Hard":
            print("You chose hard that is for 2186. \n")
            left_money = extra_money-2186
            print(f"You have {left_money} left. ")
        else:
            print("Only Soft,Medium and Hard tyres are available. ")


    elif left_money > extra_money:
        print("You have less money to buy. ")


    print("Welcome to the bissness section!! ")
    sell = str(input("What do you want to sell? "))
    price = int(input("How much do you want to sell it for?"))
    print(f"You sell {sell} for {price}")
    bank()