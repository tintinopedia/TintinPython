accounts = {"Ahaan":
                {"pin":8146,"age":23,"balance":3635,"transactions":["Account Created:₹3635"]
                },
            "Rahul":
                {"pin":1729,"age":27,"balance":1623,"transactions":["Account Created:₹1623"]},
            "Ahaana":
                {"pin":6344,"age":24,"balance":2411,"transactions":["Account Created:₹2411"]},
            }

def create_account():
    name = str(input("Enter your name: \n"))
    if name in accounts:
        print("Account already exists! \n")
        return
    age = int(input("Enter your age: \n"))
    if age < 18:
        print("Sorry You cannot create account. \n")
        return
    pin = int(input("Enter your 4-digit pin: \n"))
    if pin < 1000 or pin > 9999:
        print("Your pin must bhe only 4-digit. \n")
        return
    deposit = float(input("Enter your deposit amount: \n"))
    if deposit < 0:
        print("Sorry You cannot deposit negative amount. \n")
        return

    accounts[name] = {"pin":pin,"age":age,"balance":deposit,"transactions":[f"Account Created with ₹{deposit}"]}

    print("Acccount Created Succesfully! 💰")
    print(f"Welcome to Bank Of Baroda(Gujarat),{name}! \n")

def login():
    username = input("Enter your username: \n")

    if username not in accounts:
        print("Account not found! \n")
        return None

    attempts = 3
    while attempts > 0:
        PIN = int(input("Enter you PIN: \n"))
        if PIN == accounts[username]["pin"]:
            print("Congratulations! 🎉🎊🥳 You have successfully logged in! \n")
            return username
        attempts -= 1
        print(f"Wrong 😑Pin! Try again! attemts = {attempts} \n")
    print("Account locked! 🔒\n")
    return None
def check_balance(username):

    balance = accounts[username]["balance"]
    print(f"Your  balance is = {balance}💲! \n")
def deposit(username):
    amount = float(input("Enter your deposit amount: \n"))

    if amount < 0:
        print("Deposit amount should be greater then 0. \n")
        return
    accounts[username]["balance"] += amount
    accounts[username]["transactions"].append(f"Deposited amount is: 💲{amount}")
    print(f"{amount} has been deposited successfully! \n")
    print(f"The new balance is = {accounts[username]["balance"]} \n")
def withdrawing_money(username):
    amount = float(input("Enter your withdraw amount: \n"))
    balance = accounts[username]["balance"]
    if amount <= 0:
        print("Withdraw amount should be greater then 0. \n")
        return
    if amount > balance:
        print("Insufficient balance! \n")