import pandas as pd
import numpy as np
import plotly.express as px

 

final_csv = pd.read_csv('./final_merged_data.csv')

df = pd.DataFrame(final_csv)

 

radius =  df["radius"].to_list()
mass=   df["mass"].to_list()
 
final_gravity = []
names = df["star_names"].to_list()
print(df.head(1100))

for index, name in enumerate(names):
      
      
      if radius[index] != 0.0 or radius[index] != str:
       gravity =  6.674e-11 * (float(mass[index]) * 1.989e+30) / (float(radius[index]) * 6.957e+8)**2
       print(gravity)

      else:
       gravity = 0
      print(gravity)
      final_gravity.append(gravity)

   
  
   
 

 
df["gravity"] =  final_gravity
df.to_csv('gravity_conating_data.csv')
 


 