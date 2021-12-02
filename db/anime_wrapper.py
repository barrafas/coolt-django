import requests
import pandas as pd
from bs4 import BeautifulSoup

# SET PARA O TOP 100 ID
top_ids = set()

# SCRAPING DOS TOP 100 ID
for limit in (0,):
    html_text = requests.get(
        f'https://myanimelist.net/topanime.php?limit={limit}').text

    soup = BeautifulSoup(html_text, 'lxml')
    anime_elements = soup.find_all(
        'a', href=lambda x: x and x.startswith('https://myanimelist.net/anime/'), id=lambda x: x and x.startswith('#area'))
    for element in anime_elements:
        id = element['id'].strip('#area')
        top_ids.add(id)

# CRIANDO DATA FRAMES
works = pd.DataFrame([],
                     columns=['name', 'type', 'publisher', 'synopsis', 'released', 'img_link'])
genres_df = pd.DataFrame(columns=['genre'])
creators_df = pd.DataFrame(columns=['creator'])
work_genres = pd.DataFrame(columns=['work_id', 'genre_id'])
work_creators = pd.DataFrame(columns=['work_id', 'creator_id'])
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
    anime = requests.get(f'https://api.jikan.moe/v3/anime/{id}/').json()
    try:
        # ANIMES PODEM NÃO TER TÍTULO EM EN
        title = anime['title_english'] if anime['title_english'] else anime['title']
        genres = anime['genres']
        producers = anime['producers']
        overview = anime['synopsis']
        if anime['studios'][0]['name']:  # ANIMES PODEM NÃO TER STUDIO
            publisher = anime['studios'][0]['name']
        else:
            publisher = ''
        released = anime['aired']['from'].strip(
            'T00:00:00+00:00')  # REMOVE O HORÁRIO
        img_url = anime['image_url']
        a_series = pd.Series(
            [title, 'anime', publisher, overview, released, img_url], index=works.columns)
        works = works.append(a_series, ignore_index=True)
        filt_id = (works['name'] == title)
        anime_id = works.loc[filt_id].index[0]
        print("ID:", anime_id)
        print(title)
        for genre in genres:
            genre_id = find_genre(genre['name'])
            wg_series = pd.Series([anime_id, genre_id],
                                  index=work_genres.columns)
            work_genres = work_genres.append(wg_series, ignore_index=True)
        for producer in producers:
            producer_id = find_creator(producer['name'])
            wc_series = pd.Series([anime_id, producer_id],
                                  index=work_genres.columns)
            work_creators = work_creators.append(wc_series, ignore_index=True)

    except Exception as e:
        print(e)
        break


# Exportando
works.to_csv('works.csv', encoding='utf-8')
genres_df.to_csv('genres.csv', encoding='utf-8')
creators_df.to_csv('creators.csv', encoding='utf-8')
work_genres.to_csv('work_genres.csv', encoding='utf-8')
work_creators.to_csv('work_creators.csv', encoding='utf-8')
