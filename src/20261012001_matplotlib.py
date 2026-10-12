import matplotlib.pyplot as plt
cities = ["Mumbai","Delhi","Haryana","Kolkata"]
temperature_Celsius = [31,34,36,34]
plt.figure(figsize=(7,4))
plt.bar(cities,temperature_Celsius,color=["#57FCFF","#87FAF4","#87C2FA","#0B024F"])
plt.xlabel("Cities")
plt.ylabel("temperature")
plt.title("temperature in Cities")
plt.show()
plt.figure(figsize=(7,4))
plt.plot(cities,temperature_Celsius,color="#E7FA9D")
plt.xlabel("Cities")
plt.ylabel("temperature")
plt.title("temperature in Cities")
plt.show()