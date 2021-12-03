from django.shortcuts import render
from coolt_shelf.models import Work, Work_Creator, Work_Genre, Creator, Genre
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio


def carol(request):
    works = Work.objects.all()
    works = read_frame(works)

    works_publisher = works.groupby(["publisher"],as_index=False).count()
    print(works_publisher)

    fig = px.bar(works_publisher, x='publisher', y='name')
    fig.update_layout(
        bargap=0.2,
        margin=dict(l = 5, r = 5, t = 55, b = 5),
        title="Histograma de suas notas dadas",
    )
    fig.update_xaxes(fixedrange=True, title=None)
    fig.update_yaxes(fixedrange=True, title=None)


    barplot = pio.to_html(fig, full_html=False, default_height=400, default_width=700)


    context = {
        "barplot" : barplot
    }

    return render(request, 'carol.html', context)