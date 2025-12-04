import pandas as pd


def read_json_to_df(file):
    df = pd.read_json(file)
    return df