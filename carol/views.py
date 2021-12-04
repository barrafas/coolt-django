from django.shortcuts import render
from coolt_shelf.models import Work, Work_Creator, Work_Genre, Creator, Genre
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio


def carol(request):
    # db to dataset
    works = Work.objects.all()
    works = read_frame(works)
    works = works.loc[works['type'] == 'Livro'] #gets only books

    #publisher plot

    #groups by publisher and counts books, removes null publishers
    works_publisher = works.groupby(["publisher"],as_index=False).count()
    works_publisher = works_publisher.loc[works_publisher['publisher'] != '']
    
    #creates publisher vs quantity of books plot, removing publishers that only published 1 book
    fig = px.bar(works_publisher.loc[works_publisher['name'] > 1], x='publisher', y='name',hover_data=['name'],
    labels={"publisher": "Editora",
        "name": "Livros publicados",},
        color_discrete_sequence=['#A468D9'])
    # fig details
    fig.update_layout(
        bargap=0.1,
        margin=dict(l = 25, r = 25 , t = 50, b = 15),
        title="Publicações por editoras",
        title_font_color='#0d0221',
        title_font_size = 25
    )
    fig.update_xaxes(fixedrange=True, title='Editoras', showticklabels=False)
    fig.update_yaxes(fixedrange=True, title='Publicações')

    # morphs to html
    barplot = pio.to_html(fig, full_html=False, default_height=470, default_width=540)


    #rating plot
    works_rate = works.groupby("publisher",as_index=False)['qtd_rating'].mean() #gets the average grade per publisher
    works_rate['qtd_rating'] = works_rate['qtd_rating'].multiply(2) #turns max to 10
    works_rate = works_rate.loc[works_rate['publisher'] != ''] 

    #merges datasets, getting both avg scores by publisher and count of books in order to remove the ones that only got 1
    result = pd.merge(works_rate, works_publisher, on="publisher")

    #creates publishers vs rating plot
    fig1 = px.bar(result.loc[result['img_link'] > 1], x="publisher", y='qtd_rating_x',
    labels={"publisher": "Editora",
        "qtd_rating_x": "Média de leitores",},
        color_discrete_sequence=['#A468D9'])
    #details
    fig1.update_layout(
        bargap=0.1,
        margin=dict(l = 25, r = 25 , t = 50, b = 15),
        title="Média de leitores por editora",
        title_font_color='#0d0221',
        title_font_size = 25
    )

    fig1.update_xaxes(fixedrange=True, title='Editoras', showticklabels=False)
    fig1.update_yaxes(fixedrange=True, title='Média de leitores')

    #to html
    barplot2  = pio.to_html(fig1, full_html=False, default_height=470, default_width=540)

    #context 
    context = {
        "barplot" : barplot,
        "barplot2" : barplot2,
    }

    return render(request, 'carol.html', context)