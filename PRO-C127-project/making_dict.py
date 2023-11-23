import pandas as pd 

df = pd.read_csv('gravity_conating_data.csv')
df = df.dropna()
List = df.values.tolist()
 
 
final_list = []
for i in range(len(List)):
    a = List[i]
     
    temp_dict = {
        'Name':a[1],
        'Distance':a[2],
        'mass':a[3],
        'radius':a[4],
        'gravity':a[5]
    }
     
    final_list.append(temp_dict)
print(final_list)
