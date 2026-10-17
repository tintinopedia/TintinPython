'''
Make a pie chart to show the percentage of students who like different animals.
'''

import matplotlib.pyplot as plt

animals = ["Tiger", "Lion", "Jaguar", "Elephant"]
num = [68,52,24,19]
plt.pie(num,labels=animals, autopct="%1.1f%%")
plt.title("Favourite Animals")
plt.show()


