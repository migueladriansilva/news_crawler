import pandas as pd


def filter_results(df):
    df['Words count'] = df['Title'].str.split(' ').str.len()
    g5 = df[df['Words count'] > 5].sort_values(by='Amount of comments', ascending=False)
    l5 = df[df['Words count'] <= 5].sort_values(by='Points', ascending=False)
    filtered_df = pd.concat([g5, l5]).drop('Words count', axis=1)
    return filtered_df
