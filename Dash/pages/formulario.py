from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np
from app import app

modelo = joblib.load('modelo_xgboost.pkl')

medianas = joblib.load('medianas.pkl')

formulario = dbc.Container([
    html.P('Preencha os dados abaixo para que o modelo possa fazer a predição.', className="text-center mb-5"),
    dbc.Row([
      dbc.Col([
        # idade
        dbc.CardGroup([
        dbc.Label('Idade'),
        dbc.Input(id='idade', type='number', placeholder='Digite a Idade')
        ], className="mb-3"),
        # sexo biológico
        dbc.CardGroup([
          dbc.Label('Sexo Biológico'),
          dbc.Select(id='sexo', options=[
              {'label': 'Masculino', 'value': '1'},
              {'label': 'Feminino', 'value': '0'}]),
        ], className="mb-3"),
        # tipo de dor no peito
        dbc.CardGroup([
          dbc.Label('Tipo de Dor no Peito'),
          dbc.Select(id='cp', options=[
              {'label': 'Angina Típica', 'value': '1'},
              {'label': 'Angina Atípica', 'value': '2'},
              {'label': 'Não Angina', 'value': '3'},
              {'label': 'Angina Assintomática', 'value': '4'}]),
        ], className="mb-3"),
        # trestbps
        dbc.CardGroup([
          dbc.Label('Pressão Arterial em Repouso'),
          dbc.Input(id='trestbps', type='number', placeholder='Digite a Pressão Arterial em Repouso')
        ], className="mb-3"),
        # chol
        dbc.CardGroup([
          dbc.Label('Colesterol Sérico'),
          dbc.Input(id='chol', type='number', placeholder='Digite o Colesterol Sérico')
        ], className="mb-3"),
        # fbs
        dbc.CardGroup([
          dbc.Label('Glicemia em Jejum > 120 mg/dl'),
          dbc.Select(id='fbs', options=[
              {'label': 'Sim', 'value': '1'},
              {'label': 'Não', 'value': '0'}]),
        ], className="mb-3"),
        # restecg
        dbc.CardGroup([
          dbc.Label('Resultados Eletrocardiográficos em Repouso'),
          dbc.Select(id='restecg', options=[
              {'label': 'Normal', 'value': '0'},
              {'label': 'Anormalidade de Ondas ST-T', 'value': '1'},
              {'label': 'Hipertrofia Ventricular Esquerda', 'value': '2'}]),
        ], className="mb-3"),
      ]),
      dbc.Col([
        # thalach
        dbc.CardGroup([
          dbc.Label('Frequência Cardíaca Máxima Alcançada'),
          dbc.Input(id='thalach', type='number', placeholder='Digite a Frequência Cardíaca Máxima Alcançada')
        ], className="mb-3"),
        # exang
        dbc.CardGroup([
          dbc.Label('Angina Induzida por Exercício'),
          dbc.Select(id='exang', options=[
              {'label': 'Sim', 'value': '1'},
              {'label': 'Não', 'value': '0'}]),
        ], className="mb-3"),
        # oldpeak
        dbc.CardGroup([
          dbc.Label('Depressão do Segmento ST Induzida por Exercício em Relação ao Repouso'),
          dbc.Input(id='oldpeak', type='number', placeholder='Digite a Depressão do Segmento ST')
        ], className="mb-3"),
        # slope
        dbc.CardGroup([
          dbc.Label('Inclinação do Segmento ST'),
          dbc.Select(id='slope', options=[
              {'label': 'Inclinação Positiva', 'value': '1'},
              {'label': 'Plano', 'value': '2'},
              {'label': 'Inclinação Negativa', 'value': '3'}]),
        ], className="mb-3"),
        # ca
        dbc.CardGroup([
          dbc.Label('Número de Vasos Principais Coloridos por Fluoroscopia'),
          dbc.Select(id='ca', options=[
              {'label': '0', 'value': '0'},
              {'label': '1', 'value': '1'},
              {'label': '2', 'value': '2'},
              {'label': '3', 'value': '3'}]),
        ], className="mb-3"),
        # thal, cintilografia do miocardio
        dbc.CardGroup([
          dbc.Label('Talassemia'),
          dbc.Select(id='thal', options=[
              {'label': 'Normal', 'value': '3'},
              {'label': 'Defeito Fixo', 'value': '6'},
              {'label': 'Defeito Reversível', 'value': '7'}]),
        ], className="mb-3"),
        # botão enviar
          dbc.CardGroup([
            dbc.Label('Enviar Dados para Predição'),
              dbc.Button(
                  'Enviar',
                  id='botao-enviar',
                  n_clicks=0,
                  color="primary",
                  className="w-100 py-2"  # largura total e altura parecida
              ),
          ], className="mb-3"),
      ])
    ])
  ], fluid=True)

layout = html.Div([
  html.Header([
    html.H1('Formulário de Dados para Predição de Doença Cardíaca', className="text-center"),
  ], className="mb-4"),
  formulario,
  html.Div(id='previsao', className="pd-3")
])


@app.callback(
    Output('previsao', 'children'),
    Input('botao-enviar', 'n_clicks'),
    State('idade','value'),
    State('sexo','value'),
    State('cp','value'),
    State('trestbps','value'),
    State('chol','value'),
    State('fbs','value'),
    State('restecg','value'),
    State('thalach','value'),
    State('exang','value'),
    State('oldpeak','value'),
    State('slope','value'),
    State('ca','value'),
    State('thal','value'),
)
def prever_doenca(n_clicks, idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
  if n_clicks == 0:
    return ""

  entradas_user = pd.DataFrame(
    data = [[idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
  )

  # preencher valores nulos com as medianas
  entradas_user.fillna(medianas, inplace=True)
  # oldpeak para float
  entradas_user['oldpeak'] = entradas_user['oldpeak'].astype(float)
  # o restante para int
  for col in entradas_user.columns:
    if col != 'oldpeak':
      entradas_user[col] = entradas_user[col].astype(int)

  previsao = modelo.predict(entradas_user)[0]
  if previsao == 0:
    return dbc.Alert("O modelo previu que você NÃO TEM doença cardíaca.", color="success", class_name="m-5 text-center")
  else:
    return dbc.Alert("O modelo previu que você TEM doença cardíaca.", color="danger", class_name="m-5 text-center")

