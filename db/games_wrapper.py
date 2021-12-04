import pandas as pd

works = pd.read_csv('works.csv', index_col=0)
genres_df = pd.read_csv('genres.csv', index_col=0)
creators_df = pd.read_csv('creators.csv', index_col=0)
work_genres = pd.read_csv('work_genres.csv', index_col=0)
work_creators = pd.read_csv('work_creators.csv', index_col=0)

# Limpando games_info
games_info = pd.read_csv('external/steam.csv.zip', compression='zip').head(100)
games_info = games_info.drop(columns=['english', 'platforms', 'required_age', 'categories', 'steamspy_tags',
                                      'achievements', 'median_playtime', 'average_playtime', 'owners', 'price'])

games_info['qtd_rating'] = games_info['positive_ratings'] + \
    games_info['negative_ratings']
games_info['avg_rating'] = games_info['positive_ratings'] * \
    10/games_info['qtd_rating']

games_info = games_info.drop(columns=['positive_ratings', 'negative_ratings'])
games_info = games_info.rename(columns={'appid': 'steam_appid'})

######

games_desc = pd.read_csv(
    'external/steam_description_data.csv.zip', compression='zip').head(100)
games_desc = games_desc.drop(
    columns=['detailed_description', 'about_the_game'])

games_media = pd.read_csv('external/steam_media_data.csv.zip',
                          compression='zip').head(100)
games_media = games_media.drop(columns=['screenshots', 'background', 'movies'])

games_info = pd.merge(games_info, games_desc, how='inner', on='steam_appid')
games_info = pd.merge(games_info, games_media, how='inner', on='steam_appid')

games_info = games_info.drop(columns=['steam_appid'])
games = games_info.rename(columns={'release_date': 'released'})

#####


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


for index, row in games.iterrows():
    try:
        genres = row['genres'].split(";")
        a_series = pd.Series(
            [row['name'], 'jogo', row['publisher'],
             row['short_description'], row['released'],
             row['header_image'], row['avg_rating'],
             row['qtd_rating']], index=works.columns)
        works = works.append(a_series, ignore_index=True)
        filt_id = (works['name'] == row['name'])
        game_id = works.loc[filt_id].index[0]
        print("ID:", game_id)
        print(row['name'])
        for genre in genres:
            genre_id = find_genre(genre)
            wg_series = pd.Series([game_id, genre_id],
                                  index=work_genres.columns)
            work_genres = work_genres.append(wg_series, ignore_index=True)
        producer_id = find_creator(row['developer'])
        wc_series = pd.Series([game_id, producer_id],
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
