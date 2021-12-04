from django.shortcuts import render, redirect
from coolt_shelf.models import Work, Work_Creator, Work_Genre, Creator, Genre
from django_pandas.io import read_frame 
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def negocio(request):
    return render(request, 'negocio.html')