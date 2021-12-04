import pandas as pd

works = pd.read_csv('../csv/works.csv', index_col=0)

# Transforma yyyy em yyyy-mm-dd
works['released'] = pd.to_datetime(works.released)

works.to_csv('../csv/works.csv')
