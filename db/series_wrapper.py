import requests
import pandas as pd


genres_list = requests.get(
    'http://api.themoviedb.org/3/genre/tv/list?api_key=b33b8cf81183cc38fb69365485a59447').json()['genres']
genres_dic = dict()

for item in genres_list:
    genres_dic[item['id']] = item['name']

top_ids = set()

for page in range(1, 6):
    top_series = requests.get(
        f'https://api.themoviedb.org/3/tv/popular?language=pt-BR&page={page}&api_key=b33b8cf81183cc38fb69365485a59447').json()
    for series in top_series['results']:
        top_ids.add(int(series['id']))


# RECUPERANDO DATA FRAMES
works = pd.read_csv('works.csv', index_col=0)
genres_df = pd.read_csv('genres.csv', index_col=0)
creators_df = pd.read_csv('creators.csv', index_col=0)
work_genres = pd.read_csv('work_genres.csv', index_col=0)
work_creators = pd.read_csv('work_creators.csv', index_col=0)

print(works)

# ACHA OU ADICIONA O ID DOS GÊNEROS E CRIADORES


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


# ADICIONA CADA ANIME
for id in top_ids:
    series = requests.get(
        f'https://api.themoviedb.org/3/tv/{id}?language=pt-BR&api_key=b33b8cf81183cc38fb69365485a59447').json()
    try:
        # ANIMES PODEM NÃO TER TÍTULO EM EN
        title = series['name'] if series['name'] else series['original_name']
        genres = series['genres']
        producers = series['production_companies']
        overview = series['overview']
        released = series['first_air_date']
        if not released:
            continue
        img_url = 'https://image.tmdb.org/t/p/original' + \
            series['poster_path'] if series['poster_path'] else ''
        avg_rating = float(series['vote_average'])
        qtd_rating = int(series['vote_count'])
        a_series = pd.Series(
            [title, 'filme', '-', overview, released, img_url, avg_rating, qtd_rating], index=works.columns)
        works = works.append(a_series, ignore_index=True)
        filt_id = (works['name'] == title)
        movie_id = works.loc[filt_id].index[0]
        print("ID:", movie_id)
        print(title)
        for genre in genres:
            genre_id = find_genre(genres_dic[genre['id']])
            wg_series = pd.Series([movie_id, genre_id],
                                  index=work_genres.columns)
            work_genres = work_genres.append(wg_series, ignore_index=True)
        for producer in producers:
            producer_id = find_creator(producer['name'])
            wc_series = pd.Series([movie_id, producer_id],
                                  index=work_creators.columns)
            work_creators = work_creators.append(
                wc_series, ignore_index=True)
    except Exception as e:
        print(e)
        break


# Exportando
works.to_csv('works2.csv', encoding='utf-8')
genres_df.to_csv('genres2.csv', encoding='utf-8')
creators_df.to_csv('creators2.csv', encoding='utf-8')
work_genres.to_csv('work_genres2.csv', encoding='utf-8')
work_creators.to_csv('work_creators2.csv', encoding='utf-8')
