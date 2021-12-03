from django.shortcuts import render, redirect
from coolt_shelf.models import Work, Work_Creator, Work_Genre, Creator, Genre
from django_pandas.io import read_frame 
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Create your views here.

def dashboard(request, usertag, work_type):
    if work_type.lower() not in ["anime"]:
        return redirect('404')

    work_type = work_type.capitalize()

    def get_dataframe(model):
        model_qs = model.objects.all() # Pega todos os itens de um modelo
        model_df = read_frame(model_qs) # Converte o QuerySet para DataFrame pandas
        return model_df

    works_df = get_dataframe(Work) 
    work_genres_df = get_dataframe(Work_Genre)
    genres_df = get_dataframe(Genre)


    random_amount = np.random.randint(30, 51) # Seleciona uma quantia aleatória de obras para serem pegas
    filtered = works_df[works_df["type"] == work_type].sample(random_amount) # Coleta essa quantia
    filtered.reset_index(inplace=True, drop=True) 

    # Manipulação do numpy para gerar dados próximos de listas reais encontradas em sites similares
    # (maior concentração de 4/5s,)
    user_scores = np.random.normal(5, 2, size=random_amount) 
    user_scores[(user_scores > 4) & (user_scores < 6)] = 4
    user_scores[user_scores >= 6] = 5
    user_scores[(user_scores < 2)] = 1
    user_scores[0] = 1 # Garante que há ao menos uma nota 1
    user_scores = pd.DataFrame(user_scores, columns=["score"])
    scores_floor = pd.DataFrame(np.floor(user_scores), columns=["score"])

    filtered_scores = pd.concat([filtered, user_scores],  axis=1) # Concatena notas aleatorias às obras

    favorites = filtered_scores[filtered_scores["score"] == 5] # Coleta as obras mais gostadas
    favorite = favorites.sample().squeeze() # Escolhe uma obra aleatória para ser a favorita

    filter = (work_genres_df["work_id"] == favorite["name"]) & (work_genres_df["genre_id"].astype(str).ne('None'))
    favorite_genres = work_genres_df.loc[filter, "genre_id"].values # Pega os gêneros da obra favorita

    filter = (work_genres_df["work_id"].isin(favorites["name"].values) & (work_genres_df["genre_id"].astype(str).ne('None')))
    favorites_genres = work_genres_df.loc[filter, "genre_id"].value_counts(sort=True) # Pega os gêneros das obras favoritas


    # -------------------- Começo do histograma ---------------------
    simple_white = pio.templates["simple_white"]
    simple_white.layout.font.color = "#FFFFFF"
    simple_white.layout.plot_bgcolor = 'rgba(0, 0, 0, 0)'
    simple_white.layout.paper_bgcolor = 'rgba(0, 0, 0, 0)'
    simple_white.layout.xaxis.linecolor = '#FFFFFF'
    simple_white.layout.xaxis.tickcolor = '#FFFFFF'
    simple_white.layout.yaxis.linecolor = 'rgba(0, 0, 0, 0)'
    simple_white.layout.yaxis.showticklabels = False
    simple_white.layout.yaxis.tickcolor = 'rgba(0, 0, 0, 0)'      

    fig = px.histogram(scores_floor, x="score", category_orders=dict(score=[1, 2, 3, 4, 5]), 
                       template=simple_white, color_discrete_sequence=["#0d0221"])
    fig.update_layout(
        bargap=0.2,
        margin=dict(l = 5, r = 5, t = 55, b = 5),
        title="Histograma de suas notas dadas",
    )
    fig.update_xaxes(fixedrange=True, title=None)
    fig.update_yaxes(fixedrange=True, title=None)


    hist = pio.to_html(fig, full_html=False, default_height=500, default_width=700) # Converter figura para codigo html
    # ---------------------- Fim do histograma ----------------------

    labels = favorites_genres.index.tolist()
    values = favorites_genres.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(template=simple_white)
    donut = pio.to_html(fig, full_html=False, default_height=500, default_width=700)


    context = {
        "usertag": usertag,
        "works_df": works_df,
        "hist": hist,
        "work_type": work_type,
        "favorite": favorite,
        "favorite_genres": favorite_genres,
        "favorites_genres": favorites_genres,
        "donut": donut,
        "favorites": favorites.loc[favorites["name"].ne(favorite["name"]), "img_link"].values,
    }
    return render(request, 'tiago_analysis.html', context)

