import pandas as pd
import plotly.express as px

final_csv_data = pd.read_csv('./gravity_conating_data.csv')
df = pd.DataFrame(final_csv_data)
filtered_df = df.dropna()
print(filtered_df.head(80))
fig = px.scatter(filtered_df,x="radius", y= "mass", size="gravity", hover_data=["star_names"])
fig.show()


