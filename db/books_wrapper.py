import pandas as pd

works = pd.read_csv('works.csv', index_col=0)
genres_df = pd.read_csv('genres.csv', index_col=0)
creators_df = pd.read_csv('creators.csv', index_col=0)
work_genres = pd.read_csv('work_genres.csv', index_col=0)
work_creators = pd.read_csv('work_creators.csv', index_col=0)

books = pd.read_csv('external/books.csv', encoding='ISO-8859-1')


def find_creator(name):
    global creators_df
    filt = (creators_df['creator'] == name)
    record = creators_df.loc[filt].index.to_list()
    if not record:
        c_series = pd.Series(
            [name], index=creators_df.columns)
        creators_df = creators_df.append(c_series, ignore_index=True)
        filt_id = (creators_df['creator'] == name)
        record = creators_df.loc[filt_id].index.to_list()
    return record[0]


def find_genre(name):
    global genres_df
    filt = (genres_df['genre'] == name)
    record = genres_df.loc[filt].index.to_list()
    if not record:
        g_series = pd.Series(
            [name], index=genres_df.columns)
        genres_df = genres_df.append(g_series, ignore_index=True)
        filt_id = (genres_df['genre'] == name)
        record = genres_df.loc[filt_id].index.to_list()
    return record[0]


for index, row in books.iterrows():
    try:
        genres = row['genres'].split(", ")
        a_series = pd.Series(
            [row['title'], 'livro', row['publisher'],
             row['description'], row['firstPublishYear'],
             row['coverImg'], row['rating'],
             row['numRatings']], index=works.columns)
        works = works.append(a_series, ignore_index=True)
        filt_id = (works['name'] == row['title'])
        book_id = works.loc[filt_id].index[0]
        print("ID:", book_id)
        print(row['title'])
        for genre in genres:
            genre_id = find_genre(genre)
            wg_series = pd.Series([book_id, genre_id],
                                  index=work_genres.columns)
            work_genres = work_genres.append(wg_series, ignore_index=True)
        producer_id = find_creator(row['author'])
        wc_series = pd.Series([book_id, producer_id],
                              index=work_creators.columns)
        work_creators = work_creators.append(
            wc_series, ignore_index=True)
    except Exception as e:
        print(e)
        break

# Exportando
works.to_csv('works.csv', encoding='utf-8')
genres_df.to_csv('genres.csv', encoding='utf-8')
creators_df.to_csv('creators.csv', encoding='utf-8')
work_genres.to_csv('work_genres.csv', encoding='utf-8')
work_creators.to_csv('work_creators.csv', encoding='utf-8')
