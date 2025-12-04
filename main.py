from utils import *

file = "orders_simple.json"
df = read_json_to_df(file)
df = change_to_proper_float(df, "total_amount")
df = change_to_int(df, "shipping_days")
df = change_to_int(df, "customer_age")
df = change_to_float(df, "rating")
df = change_to_datetime(df, "order_date")
df = removes_tags(df, "items_html")
print(df.coupon_used[df.coupon_used == np.nan])
df = set_nan(df, "coupon_used")
df = add_order_month_column(df)
df = add_high_value_order_column(df)
df = sort_table(df)
df = rating_of_country_column(df)
df = delete_rows_by_condition(df)
df = add_delivery_status_column(df)
save_csv(df)