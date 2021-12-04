from django.shortcuts import render, redirect
from coolt_shelf.models import Work, Work_Creator, Work_Genre, Creator, Genre
from django_pandas.io import read_frame
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def negocio(request):
    # Coleta as informações e transforma em um dataFrame
    works = Work.objects.all()
    works = read_frame(works)
    # Ajusta a data para indicar apenas o ano e limita ele para menor de 2016
    works['released'] = pd.to_datetime(works['released'])
    works['released'] = works['released'].dt.year
    works = works[works['released'] < 2016]
    # Cria dataFrames únicos para cada tipo
    animes = works.loc[works["type"] == 'Anime']
    livros = works.loc[works["type"] == 'Livro']
    filmes = works.loc[works["type"] == 'Filme']
    jogos = works.loc[works["type"] == 'Jogo']
    series = works.loc[works["type"] == 'Série']
    # Padroniza as notas de livro e coloca limite mínimo de ano
    livros['avg_rating'] = livros['avg_rating'].multiply(2)
    livros = livros.loc[livros['released'] >= 1979]

    # Criação do boxplot de anime
    fig1 = px.box(animes, x='released', y='avg_rating',
                  color_discrete_sequence=['GoldenRod'], range_x=[2000, 2016])
    fig1.update_layout(
        title="Boxplot de nota pelos anos (Anime)",
        paper_bgcolor='rgba(194,187,215,1)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="DarkGoldenRod"
        )
    )
    fig1.update_xaxes(fixedrange=True, title='Ano de lançamento')
    fig1.update_yaxes(fixedrange=True, title='Notas')

    animebox = pio.to_html(fig1, full_html=False,
                           default_height=400, default_width=800)

    # Criação do boxplot de livro
    fig2 = px.box(livros, x='released', y='avg_rating',
                  color_discrete_sequence=['DarkOrange'], range_x=[2000, 2016])
    fig2.update_layout(
        title="Boxplot de nota pelos anos (Livro)",
        paper_bgcolor='rgba(194,187,215,1)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="Sienna"
        )
    )
    fig2.update_xaxes(fixedrange=True, title='Ano de lançamento')
    fig2.update_yaxes(fixedrange=True, title='Notas')

    livrobox = pio.to_html(fig2, full_html=False,
                           default_height=400, default_width=800)

    # Criação do boxplot de filme
    fig3 = px.box(filmes, x='released', y='avg_rating',
                  color_discrete_sequence=['LimeGreen'], range_x=[2000, 2016])
    fig3.update_layout(
        title="Boxplot de nota pelos anos (Filme)",
        paper_bgcolor='rgba(194,187,215,1)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="DarkGreen"
        )
    )
    fig3.update_xaxes(fixedrange=True, title='Ano de lançamento')
    fig3.update_yaxes(fixedrange=True, title='Notas')

    filmebox = pio.to_html(fig3, full_html=False,
                           default_height=400, default_width=800)

    # Criação do boxplot de jogo
    fig4 = px.box(jogos, x='released', y='avg_rating',
                  color_discrete_sequence=['RoyalBlue'], range_x=[2000, 2016])
    fig4.update_layout(
        title="Boxplot de nota pelos anos (Jogo)",
        paper_bgcolor='rgba(194,187,215,1)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="Navy"
        )
    )
    fig4.update_xaxes(fixedrange=True, title='Ano de lançamento')
    fig4.update_yaxes(fixedrange=True, title='Notas')

    jogobox = pio.to_html(fig4, full_html=False,
                          default_height=400, default_width=800)

    # Criação do boxplot de série
    fig5 = px.box(series, x='released', y='avg_rating',
                  color_discrete_sequence=['crimson'], range_x=[2000, 2016])
    fig5.update_layout(
        title="Boxplot de nota pelos anos (Série)",
        paper_bgcolor='rgba(194,187,215,1)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="DarkRed"
        )
    )
    fig5.update_xaxes(fixedrange=True, title='Ano de lançamento')
    fig5.update_yaxes(fixedrange=True, title='Notas')

    seriebox = pio.to_html(fig5, full_html=False,
                           default_height=400, default_width=800)

    # Cria os contextos de acordo com a forma em html dos boxplots
    context = {
        "anime": animebox,
        "livro": livrobox,
        "filme": filmebox,
        "jogo": jogobox,
        "serie": seriebox,
    }

    return render(request, 'negocio.html', context)
