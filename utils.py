import pandas as pd
import numpy as np


def read_json_to_df(file):
    df = pd.read_json(file)
    return df


def change_to_proper_float(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: float(str(x)[:-1])) 
    return df


def change_to_float(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: float(x))
    return df


def change_to_int(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: int(x))
    return df

def change_to_datetime(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: pd.to_datetime(x))
    return df

def removes_tags(df, column_name):
    df[column_name] = df[column_name].str.replace(r'<[^<>]*>', '', regex=True)
    return df


def set_nan(df, column_name):
    df[column_name] = df[column_name].replace(np.nan, "no coupon")
    return df

def add_order_month_column(df):
    df['order_month'] = pd.to_datetime(df['order_date']).dt.month
    return df


def add_high_value_order_column(df):
    df["high_value_order"] = df.total_amount > df.total_amount.mean()
    return df


def sort_table(df):
    df = df.sort_values("total_amount", ascending=False)
    return df


def rating_of_country_column(df):
    country_avarage_rating = df.groupby("country")["rating"].transform("mean")
    df["country_avarage_rating"] = country_avarage_rating
    return df


def delete_rows_by_condition(df):
    df = df[(df.total_amount > 1000) & (df.rating > 4.5)]
    return df


def add_delivery_status_column(df):
    df["delivery_status"] = df.apply(check_value_total, axis=1)
    return df

def check_value_total(row):
    if row["shipping_days"] > 7:
        val = "delayed"
    else:
        val = "on_time"
    return val

def save_csv(df):
    return df.to_csv("clean_orders_[ID_NUMBER].csv", "\t")
    