import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('filtered_stars.csv')
star_names = df['1'] 
distance = df['2'] 
mass = df['3'] 
radius = df['4'] 
gravity = df['5'] 
headings = ["Name","Distance","Mass","Radius","Gravity"]
fig = plt.figure(figsize = (1000, 5))
plt.bar(star_names, mass, color ='black', 
        width = 0.5)
plt.xlabel("Star Names")
plt.ylabel("Mass")
plt.title("Masses of the planets")
plt.show()

plt.bar(star_names, gravity, color ='blue', 
        width = 0.5)

plt.xlabel("Star Names")
plt.ylabel("Gravity")
plt.title("Gravity of the planets")
plt.show()

plt.bar(star_names, radius, color ='red', 
        width = 0.5)

plt.xlabel("Star Names")
plt.ylabel("Radius")
plt.title("Radius of the planets")
plt.show()

plt.bar(star_names, distance, color ='green', 
        width = 0.5)

plt.xlabel("Star Names")
plt.ylabel("Distance")
plt.title("Distance of the planets from earth")
plt.show()