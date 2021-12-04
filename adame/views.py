from django.shortcuts import render
from coolt_shelf.models import Work, Work_Genre
from django_pandas.io import read_frame
import pandas as pd
import plotly.express as px
import plotly.io as pio


def index(request):
    # Adquirindo todas as entradas da tabela Work e transformando em df
    works_data = Work.objects.all()
    works = read_frame(works_data)[['name', 'type']]

    # Adquirindo todas as entradas da tabela Work_Genre e transformando em df
    work_genres_data = Work_Genre.objects.all()
    work_genres = read_frame(work_genres_data)

    # Fazendo merge pelo nome do work para ter a coluna type em cada relação.
    genres_types = pd.merge(
        works, work_genres, left_on='name', right_on='work_id')

    # Removendo colunas desnecessárias
    genres_types = genres_types.drop(columns=['name', 'id', 'work_id'])

    # Adquirindo a quantidade de cada gênero por tipo (como index).
    size_genres = genres_types.groupby(
        ['type', 'genre_id']).size()

    # Tipos para iteração
    TYPES = ('Anime', 'Filme', 'Série', 'Livro', 'Jogo')

    # Dicionário a ser exportado pelo context
    plots = dict()

    for type in TYPES:
        # Nome para utilizar nas fstrings
        name = (type + 's').lower()

        # Criando plot
        fig = px.bar(size_genres[type].sort_values(ascending=False).head(15),
                     template='plotly_dark',
                     labels={
            "genre_id": "Gênero",
            "value": "Quantidade"
        }
        )
        fig.update_layout(
            bargap=0.2,
            margin=dict(l=5, r=5, t=55, b=5),
            title=f"Gêneros mais comuns dentre {name} de nosso banco.",
            showlegend=False
        )
        fig.update_xaxes(fixedrange=True, title=None)
        fig.update_yaxes(fixedrange=True, title=None)

        # Salvando na variável a exportar
        plots[name.title()] = pio.to_html(fig, full_html=False,
                                          default_height=400, default_width=700)

    context = {'plots': plots}

    return render(request, 'adame.html', context)
