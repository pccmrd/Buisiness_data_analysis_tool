import os
import pandas as pd

def load_and_save():
    file_path_read = os.path.join('..', 'data', 'feed-view.log')
    file_path_write = os.path.join('..', 'data', 'feed-views-semicolon.log')

    df = pd.read_csv(
        file_path_read,
        sep='\t',
        names=['datetime', 'user'],
        index_col='datetime',
        skiprows=[2, 3],
        skipfooter=2,
        engine='python'
    )

    df.index.name = 'date_time'

    df.to_csv(file_path_write, sep=';')
    
    return df

if __name__ == '__main__':
    df = load_and_save()
