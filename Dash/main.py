from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pages
from app import app

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
        # dbc.DropdownMenu(
            #children=[
                # dbc.DropdownMenuItem("More pages", header=True),
                # dbc.DropdownMenuItem("Page 2", href="#"),
                # dbc.DropdownMenuItem("Page 3", href="#"),
            #],
            #nav=True,
            #in_navbar=True,
            #label="More",
        #),
    ],
    brand="Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True,
    className="mb-4",
)

app.layout = html.Div([
  dcc.Location(id='url', refresh=False),
  navegacao,
  html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
  if pathname == '/graficos':
    return pages.graficos.layout
  elif pathname == '/formulario':
    return pages.formulario.layout
  #else:
    

app.run(debug=True)