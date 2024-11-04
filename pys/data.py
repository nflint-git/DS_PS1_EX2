import pandas as pd
from pandas import DataFrame


def round_to_nearest_billion(x: float) -> int:
    return round(x / 1e9)


def load_dataset(data: str) -> DataFrame:
    """
    load the dataset from a CSV

    """
    df = pd.read_csv(data)
    country = ['United Kingdom', 'Japan', 'China', 'Germany', 'Switzerland']
    years = [str(year) for year in range(2000, 2023)]
    filtered_df = df[df['Country'].isin(country)]
    filtered_df = filtered_df[['Country'] + years]
    filtered_df.set_index('Country', inplace=True, drop=True)
    filtered_df = filtered_df.applymap(round_to_nearest_billion)

    return filtered_df
