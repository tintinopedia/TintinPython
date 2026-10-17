'''
Make a bar chart to show your favourite subjects and how many votes each 
subject got.
'''
import matplotlib.pyplot as plt

Favourite_subject = ["Maths","English","Science"]
votes = [99,83,96]

plt.figure(figsize=(10,10))
plt.bar(Favourite_subject,votes,color=["#70FFFD","#D6F527","#F527F2"])
plt.xlabel("number of votes")
plt.ylabel("Subjects")
plt.title("Favourite Subject")
plt.show()
'''
import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "Art"]
votes = [8, 6, 9, 4]
plt.bar(subjects,votes,color=["#B6FBFC","#FCB6EE","#FCF6B6","#5C80EB"])
plt.title("Favorite Subjects")
plt.xlabel("Subjects")
plt.ylabel("Number of Votes")
plt.ylim(0, 10)
plt.show()
'''