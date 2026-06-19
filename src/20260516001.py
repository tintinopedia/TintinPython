# HW 1
def even_odd_num():
    num = int(input("Enter a number: "))
    for i in range(1,num+1):
        if i % 2== 0:
            print("Even number ",i)
        else:
            print("Odd number ",i)
even_odd_num()

# HW 2
def magic_num():
    for i in range(1,21):
        if i > 10 and i % 2 == 0:
            print("MAGIC NUMBER 🪄 ",i)
        else:
            print("NOT A MAGIC NUMBER ❌ ",i)
magic_num()