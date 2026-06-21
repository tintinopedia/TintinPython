print("Welcome to the f1 cars game!!! 🎮🕹️ Race with Ferrari 🏎️🏁🚥🏆💨,Mercedes ℳℰℛℂℰⅅℰՏ and Redbull!! ")
player_name = str(input("enter player name: \n \t Example: abcd ")).title()
print(f"Hello {player_name}!! This is the best Formula 1 car game!! \n")
def game():
    shell_fuel = 60.00
    km = 800
    laps = 15
    name = player_name
    top_speed = 458.6
    end_line = laps
    finish = str(input("Have you reached the end line?? 🔚 (yes\no)"))
    speed = str(input("Did you hit the top speed?? yes\no"))
    if finish == "yes":
        print("You won the game!! 🏆")
        if finish == "yes":
            print("Things to do: \n")
            print(f"Try to hit the top speed🏎️!! \n \t {top_speed} \n")
    elif finish == "no":
        print("You have not reached the end line! \n")
        location = str(input("Tell me what can you see nearby!! Indications(Trees,mountain,road,nearby lake) \n")).lower()
        if location == "trees":
            print("You have chosen Trees. \n")
            print("If the trees are on the left ⬅️ side move right ➡️ If the trees are on your right ➡️ move left ⬅️")
            shell_fuel = 60.00-20
            km = 800-3
            laps = laps-km
            print(f"You have {shell_fuel} left.")
            fuel = str(input("Do you want refuel your F1 car. \n"))
            if fuel == "yes":
                shell_fuel = 60.00+20
                print(f"You have {shell_fuel} left.")
            elif fuel == "no":
                print("You have not refueled your F1 car.")
        elif location == "mountain":
            print("You have chosen mountain. \n")
            print("If the mountain is on the left ⬅️ side move right ➡️ If the mountain is on your right ➡️ move left ⬅️")
            shell_fuel = 60.00-30
            km = 800-5
            laps = laps-km
            print(f"You have {shell_fuel} left.")
            fuel = str(input("Do you want refuel your F1 car. \n"))
            if fuel == "yes":
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
            if fuel == "yes":
                shell_fuel = 60.00+20
                print(f"You have {shell_fuel} left.")
            elif fuel == "no":
                print("You have not refueled your F1 car.")
    else:
        print("Invalid input!!")
    def status():
        print("Things to do: \n")
        print(f"Try to hit the top speed🏎️!! \n \t {top_speed} \n")
        print("km = ",km)
        print("Try to save shell⛽️!! \n")
        print("shell_fuel = ",shell_fuel)
        print("Try to reach as early as you can!! \n to win the trophy🏆!! \n")
    status()
    restart = str(input("Do you want to restart the game?? yes/no \n"))
    if restart == "yes":
        game()
    elif restart == "no":
        print("Thank you for playing!!")
    else:
        print("Invalid input!!")
game()