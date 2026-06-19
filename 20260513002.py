# Section B: AND OR Practice
# If number is greater than 0 and less than 10 → print Small Number
marks = int(input("Enter marks: "))
if marks > 0 and marks < 10:
    print(f"Small number \n")


# If a number is divisible by 2 or divisible by 5 → print Special Number
number = int(input("Enter number: "))
if number % 2 == 0 or number % 5 == 0:
    print(f"Special Number \n")


# If marks > 50 and attendance > 75 → print Pass else print Fail
number = int(input("Enter number: "))
if number > 50 and attendance > 75:
    print(f"Pass \n")
else:
    print(f"Fail \n")
