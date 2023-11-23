import pandas as pd

merged_data = pd.read_csv('./merged_data.csv')
df = pd.DataFrame(merged_data)

df.drop(columns=["luminosity", "Constellation", "Right ascension", "Declination", "App.mag.", "Spectraltype", "Discovery year", "Unnamed: 0"], inplace=True)
df2 = df.drop('id', axis=1)
df2.replace('?', pd.NA, inplace=True)

# Convert columns to numeric (if needed)
numeric_columns = df2.columns.difference(['star_names'])
df2[numeric_columns] = df2[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Filter out rows with 0 values in the "radius" or "mass" columns
filtered_df = df2[(df2['radius'] != 0) & (df2['mass'] != 0)]
filtered_df = filtered_df.drop_duplicates()

# Save the filtered DataFrame
print(filtered_df)
filtered_df.to_csv('final_Merged_data.csv', index=False)