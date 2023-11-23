import plotly_express as pc
import csv
import pandas as pd
import matplotlib

dataFrame = pd.read_csv('gravity_conating_data.csv')
List = dataFrame.values.tolist()
 
filtered_stars = [ ]
print(List[10][2])

for i in range(len(List)): 
    if List[i][2] <100 or List[i][2] == 100 :
        if List[i][5] >150 and List[i][5] < 350:
         filtered_stars.append(List[i])
 
df_of_filtered_stars = pd.DataFrame(filtered_stars)
print(df_of_filtered_stars)

df_of_filtered_stars.to_csv('filtered_stars.csv')