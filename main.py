from utils import read_json_to_df

file = "orders_simple.json"
df = read_json_to_df(file)
print(df.head())