import requests
import pandas as pd
from bs4 import BeautifulSoup

# Set para os top 100 ID
top_ids = set()

# Scraping dos top 100 ID
for limit in (0, 50):
    html_text = requests.get(
        f'https://myanimelist.net/topanime.php?limit={limit}').text

    soup = BeautifulSoup(html_text, 'lxml')
    anime_elements = soup.find_all(
        'a', href=lambda x: x and x.startswith('https://myanimelist.net/anime/'), id=lambda x: x and x.startswith('#area'))
    for element in anime_elements:
        id = element['id'].strip('#area')
        top_ids.add(id)

# Criando dataframes
works = pd.DataFrame(columns=['name', 'type', 'publisher',
                     'synopsis', 'released', 'img_link', 'avg_rating', 'qtd_rating'])
genres_df = pd.DataFrame(columns=['genre'])
creators_df = pd.DataFrame(columns=['creator'])
work_genres = pd.DataFrame(columns=['work_id', 'genre_id'])
work_creators = pd.DataFrame(columns=['work_id', 'creator_id'])


# Acha ou adiciona o id do criador
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


# Acha ou adiciona o id do gênero
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


# Itera sobre cada id e captura/adiciona os dados do anime ao df
for id in top_ids:
    anime = requests.get(f'https://api.jikan.moe/v3/anime/{id}/').json()
    try:
        # Animes podem não ter título em inglês
        title = anime['title_english'] if anime['title_english'] else anime['title']
        genres = anime['genres']
        producers = anime['producers']
        overview = anime['synopsis']

        ####

        # Animes podem não ter estudio
        if anime['studios'][0]['name']:
            publisher = anime['studios'][0]['name']
        else:
            publisher = ''

        # Remove o horário
        released = anime['aired']['from'].strip(
            'T00:00:00+00:00')

        img_url = anime['image_url']

        # Pula iteração caso não tiver score
        if not (anime['score'] or anime['scored_by']):
            continue

        avg_rating = float(anime['score'])
        qtd_rating = int(anime['scored_by'])

        # Adiciona ao dataframe
        a_series = pd.Series(
            [title, 'anime', publisher, overview, released, img_url, avg_rating, qtd_rating], index=works.columns)
        works = works.append(a_series, ignore_index=True)

        # Encontra o id do work
        filt_id = (works['name'] == title)
        anime_id = works.loc[filt_id].index[0]
        print("ID:", anime_id)
        print(title)

        # Adiciona os gêneros e os produtores em suas devidas tabelas/relações.
        for genre in genres:
            genre_id = find_genre(genre['name'])
            wg_series = pd.Series([anime_id, genre_id],
                                  index=work_genres.columns)
            work_genres = work_genres.append(wg_series, ignore_index=True)
        for producer in producers:
            producer_id = find_creator(producer['name'])
            wc_series = pd.Series([anime_id, producer_id],
                                  index=work_creators.columns)
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
