# Section D: IF ELIF ELSE Practice
# Marks ≥ 80 → Excellent, Marks ≥ 50 → Good, else → Try Again
marks = int(input("Enter your marks:"))
if marks > 80:
    print("Excellent ⭐⭐⭐️")
elif marks > 50:
    print("Good ⭐⭐")
else:
    print("Try Again")


# If number > 0 → Positive, number < 0 → Negative, else → Zero
num = int(input("Enter a number: Negative/Positive:"))
if num > 0:
    print("Positive(+)")
elif num < 0:
    print("Negative(-)")
else:
    print("Zero")