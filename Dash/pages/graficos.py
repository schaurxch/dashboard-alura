from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Carregando e preparando os dados
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0) * 1

# Criando os gráficos iniciais
figura_histograma = px.histogram(dados, x='age')
div_do_histograma = html.Div([
            html.H2('Histograma de idades'),
            dcc.Graph(figure=figura_histograma),
        ])

figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca')
div_do_boxplot = html.Div([
            html.H2('Distribuição das idades'),
            dcc.Graph(figure=figura_boxplot)
        ])

# Adicionando os novos gráficos
figura_boxplot_chol = px.box(dados, x='doenca', y='chol', color='doenca')
div_do_boxplot_chol = html.Div([
            html.H2('Colesterol Sérico'),
            dcc.Graph(figure=figura_boxplot_chol)
        ])

figura_boxplot_trestbps = px.box(dados, x='doenca', y='trestbps', color='doenca')
div_do_boxplot_trestbps = html.Div([
            html.H2('Pressão sanguínea em repouso'),
            dcc.Graph(figure=figura_boxplot_trestbps)
        ])

# Organizando o layout
layout = html.Div([
        html.H1('Análise de dados do UCI Repository Heart Disease', className='text-center mb-5'),
        dbc.Container([
            dbc.Row([
                dbc.Col([div_do_histograma, div_do_boxplot_chol], md=6),
                dbc.Col([div_do_boxplot, div_do_boxplot_trestbps], md=6)
            ], align="start")
        ])
    ])