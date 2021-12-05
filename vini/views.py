from math import remainder
from django.shortcuts import render
from django.views.generic import TemplateView
from coolt_shelf.models import Work
from django_pandas.io import read_frame
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Create your views here.

def to_decade(year:int):
    quo = year//10
    dif = year-10*quo
    if dif>5:
        return 10*quo
    else:
        return 10*quo+10


class Vini(TemplateView):
    template_name = "vini.html"

    def __init__(self):
        self.extra_context = {}
        df = self.load_df()
        figs = self.create_figs(df)
        extra_context = {"insights":self.get_insights(), "titles":self.get_titles(), "range5":[0,1,2,3,4]}
        self.to_context(**figs,**extra_context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for k in self.extra_context:
            context[k] = self.extra_context[k]
        return context

    def load_df(self):
        works_django = Work.objects.all()
        columns = ["type","released","qtd_rating"]
        df = read_frame(works_django)[columns].sort_values("released")
        return df

    def create_figs(self, df):
        figs = {}

        types = pd.unique(df["type"])
        # Popularity:
        df_pop = df.copy()
        df_pop["released"] = df_pop["released"].apply(lambda x: x.year)
        df_pop = df_pop.groupby(by=["type","released"], axis=0).sum("qtd_rating").reset_index()
        popularity = px.scatter(df_pop, x="released", y="qtd_rating", color="type", trendline="rolling", trendline_options={"window":2}, opacity=0, labels={"type":"Tipo"})
        popularity.update_xaxes(fixedrange=True, title="Década", range=[1987,2022])
        popularity.update_yaxes(fixedrange=True, title="Quantidade de Avaliações", range=[-1000000,8000000])
        popularity = pio.to_html(popularity, full_html=True, default_height=400, default_width=600)


        ind_pop = []
        for i in range(len(types)):
            t = types[i]
            df_t = df[ df["type"]==t ]
            i_p = px.scatter(df_t, y="qtd_rating", x="released", color="type", labels={"type":"Tipo"}, opacity=.7)
            i_p.update_xaxes(fixedrange=True, title="Década")
            i_p.update_yaxes(fixedrange=True, title="Quantidade de Avaliações")
            i_p = pio.to_html(i_p, full_html=True, default_height=400, default_width=600)
            ind_pop.append(i_p)


        figs["popularity"] = popularity
        figs["ind_pop"] = ind_pop

        return figs
    
    def figs_to_html(self, figs):
        html_figs = {}
        for k in figs:
            html_figs[k] = pio.to_html(figs[k], full_html=True, default_height=400, default_width=600)
        return html_figs

    def get_insights(self):
        
        i0 = "Como podemos ver, os livros são as obras mais atemporais, com algumas ocorrências muito antigas e de \
            alta relevância. Isto se deve à natureza desta mídia que é totalmente voltada ao conteúdo, e não à forma. \
            É interessante notar como todas as obras antigas são de alta relevância, porque as que não era foram perdidas\
            , enquanto há obras recentes com poucas avaliações que estão na base de dados simplesmente por serem recentes."
        i1 = "Seguidos dos livros possuímos as séries. Vale notar como há mais séries sendo produzidas hoje, com um maior \
            número de séries com várias avaliações mas também de séries com quase nenhuma avaliação"
        i2 = "Com os animes vemos algo interessante; a quantidade de animes com 0 avaliações é pequeno em comparação às \
            outras mídias. Também há um momento marcante entorno dos anos 2000, onde alguns animes possuem uma quantidade \
            elevada de avaliações. Provavelmente são animes muito bons ou que marcaram alguma geração (ou os dois)."
        i3 = "O que pode ser visto dos jogos é muito muito claro: poucos jogos se destacam, mas os que se destacam são \
            verdadeiros outliers. Isto pode ser devido à capacidade de um jogo produzir outras formas de entretenimento, \
            como competições, vídeos, streaming, o que faz com que caso um jogo faça muito sucesso, o faça em diversas \
            frentes e chame muita atenção para então ser avaliado. É interessante olhar o boom de jogos em torno de 2006-2007"
        i4 = "O caso dos filmes também é claro: ao longo do tempo algumas obras foram sendo esquecidas e outras foram se \
            consagrando como obras primas, chamando a atenção e avaliações de pessoas mesmo que muito tempo depois. Ainda assim \
            a quantidade de avaliações é reduzida."
        
        insights = [i0,i1,i2,i3,i4]

        return insights

    def get_titles(self):
        
        t0 = "Livro"
        t1 = "Série"
        t2 = "Anime"
        t3 = "Jogo"
        t4 = "Filme"
        
        titles = [t0,t1,t2,t3,t4]

        return titles


    def to_context(self, **kwargs):
        for k in kwargs:
            self.extra_context[k] = kwargs[k]
    

                
