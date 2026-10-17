'''
Make a pie chart to show the percentage of students who like different animals.
'''

import matplotlib.pyplot as plt

animals = ["Tiger", "Lion", "Jaguar", "Elephant"]

plt.pie(animals, autopct="%1.1f%%")
plt.title("Favourite Animals")
plt.show()
