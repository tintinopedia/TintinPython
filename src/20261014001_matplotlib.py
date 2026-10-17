'''
Make a line chart to show the amount of rainfall (in mm) for each month 
from January to June.
'''

import matplotlib.pyplot as plt

Months = ["Jan","Feb","Mar","Apr","May","Jun"]
rainfall = [30,50,20,70,90,60]

plt.figure(figsize=(7,10))
plt.plot(Months,rainfall,color  = "#C9B6FC")
plt.xlabel("Months")
plt.ylabel("Rainfall(mm)")
plt.title("Monthly Rainfall")
plt.show()


                                                                                                     