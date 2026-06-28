def bank():
    print("Welcome to the Bank!! ")
    name = str(input("Enter your name: "))
    extra_money = 10000000
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
    elif buy == "New Car":
        print("You chose New Car. \n")
        Car = str(input("Which car do you want to buy?? options: (Ferrari 🏎️🏁🚥🏆💨 = 961410,Mercedes ℳℰℛℂℰⅅℰՏ = 599999 and Redbull = 600032)"))
        if Car == "Ferrari":
            print("You chose Ferrari that is for 961410. \n")
            left_money = extra_money-961410
            print(f"You have {left_money} left. ")
        elif Car == "Mercedes":
            print("You chose Mercedes that is for 599999. \n")
            left_money = extra_money-599999
            print(f"You have {left_money} left. ")
        elif Car == "Redbull":
            print("You chose Redbull that is for 600032. \n")
            left_money = extra_money-600032
            print(f"You have {left_money} left. ")
        else:
            print("Only Ferrari,Mercedes and Redbull is available. \n")


    elif left_money > extra_money:
        print("You have less money to buy. ")
    else:
        print("Invalid input!!")
bank()
def business():


    print("Welcome to the business section!! ")
    earned_money = 0
    sell = str(input("What do you want to sell? "))
    price = int(input("How much do you want to sell it for?"))
    qty = int(input("How many do you want to sell?"))
    total = qty*price
    print(f"You sold {sell} for {total}")
    earned_money = earned_money+total
    print(f"You have earned {earned_money}")
    sell_again = str(input("Do you want to sell something else as well? "))
    if sell_again == "yes":
        business()
    else:
        print("Thanks for doing business with us!! \n")
        print("Thank you for your interest. 👋")
business()