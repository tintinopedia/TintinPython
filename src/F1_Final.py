print("Welcome to the f1 cars game!!! 🎮🕹️ Race with Ferrari 🏎️🏁🚥🏆💨,Mercedes ℳℰℛℂℰⅅℰՏ and Redbull!! ")
player_1 = str(input("enter player name: \n \t Example: abcd ")).title()
player_2 = str(input("enter player 2: \n \t Example: abcd ")).title()
print(f"Hello {player_1}{player_2}!! This is the best Formula 1 car game!! \n")
def game():
    shell_fuel = 60.00
    km = 800
    laps = 15
    name = player_1
    top_speed = 458.6
    end_line = laps
    finish = str(input("Have you reached the end line?? 🔚 (Yes or No?)"))
    speed = str(input("Did you hit the top speed?? Yes or No?"))
    if finish == "Yes":
        speed1 = int(input(f"{player_1} Tell your current speed: \n"))
        speed2 = int(input(f"{player_2} Tell your current speed: \n"))
        if speed1 == speed2:
            print("It's a tie. \n")
            print("You are suppose to play a new game. \n")
            game()
        elif speed1 > speed2:
            print(f"{player_1} wins 🏆 \n")
        elif speed1 < speed2:
            print(f"{player_2} wins🏆 \n")
        else:
            print("Invalid input Try again. \n")

        print("You won the game!! 🏆")
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
        if finish == "Yes":
            print("Things to do: \n")
            print(f"Try to hit the top speed🏎️!! \n \t {top_speed} \n")
    elif finish == "No":
        name1 = str(input(f"Are you {player_1} or {player_2}? \n"))
        if name1 == player_1:
            print(f"{player_1} You have not reached the end line! \n")
        elif name1 == player_2:
            print(f"{player_2} You have not reached the end line! \n")
        location = str(input(f"{name1} Tell me what can you see nearby!! Indications(Trees,mountain,road,nearby lake) \n")).lower()
        if location == "trees":
            print("You have chosen Trees. \n")
            print("If the trees are on the left ⬅️ side move right ➡️ If the trees are on your right ➡️ move left ⬅️")
            shell_fuel = 60.00-20
            km = 800-3
            laps = laps-km
            print(f"You have {shell_fuel} left.")
            fuel = str(input("Do you want refuel your F1 car. \n"))
            if fuel == "Yes":
                shell_fuel = 60.00+20
                print(f"You have {shell_fuel} left.")
            elif fuel == "No":
                print("You have not refueled your F1 car.")
        elif location == "mountain":
            print("You have chosen mountain. \n")
            print("If the mountain is on the left ⬅️ side move right ➡️ If the mountain is on your right ➡️ move left ⬅️")
            shell_fuel = 60.00-30
            km = 800-5
            laps = laps-km
            print(f"You have {shell_fuel} left.")
            fuel = str(input("Do you want refuel your F1 car. \n"))
            if fuel == "Yes":
                shell_fuel = 60.00+20
            print(f"You have {shell_fuel} left.")
        elif location == "road":
            print("Go straight. \n")
            shell_fuel = 60.00-10
            km = 800-2
        elif location == "nearby lake":
            print("You have chosen lake. \n")
            print("If the lake is on the left ⬅️ side move right ➡️ If the lake is on your right ➡️ move left ⬅️")
            shell_fuel = 60.00-40
            km = 800-7
            laps = laps-km
            print(f"You have {shell_fuel} left.")
            fuel = str(input("Do you want refuel your F1 car. \n"))
            if fuel == "Yes":
                shell_fuel = 60.00+20
                print(f"You have {shell_fuel} left.")
            elif fuel == "No":
                print("You have not refueled your F1 car.")
    else:
        print("Invalid input!!")
    def status():
        print("Things to do: \n")
        print(f"Try to hit the top speed 🏎️!! \n \t {top_speed} \n")
        print("km = ",km)
        print("Try to save shell⛽️!! \n")
        print("shell_fuel = ",shell_fuel)
        print("Try to reach as early as you can!! \n to win the trophy🏆!! \n")
    status()
    restart = str(input("Do you want to restart the game?? Yes or No? \n"))
    if restart == "Yes":
        game()
    elif restart == "No":
        print("Thank you for playing!!")
    else:
        print("Invalid input!!")
game()