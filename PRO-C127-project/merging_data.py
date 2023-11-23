import pandas as pd

brown_dwarfs = pd.read_csv('./new_scraped_data.csv')
stars = pd.read_csv('./scraped_data.csv')
df1= pd.DataFrame(stars)
df = pd.DataFrame(brown_dwarfs)
df.rename(columns={'Radius': 'radius','Mass':'mass','Brown dwarf':'star_names','Distance':'distance'}, inplace=True)
nan_removed = df.fillna(0)
nan_removed["radius"] =  nan_removed["radius"].astype(float)
nan_removed["mass"] =  nan_removed["mass"].astype(float)
nan_removed["radius"] =  nan_removed["radius"]*0.102763
nan_removed["mass"] =  nan_removed["mass"]*0.000954588
nan_removed.drop_duplicates(keep='first')
merged_data = pd.concat([df1,nan_removed],axis=0 )
merged_data.to_csv('merged_data.csv')