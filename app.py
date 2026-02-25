
from dash import Dash,  html, dash_table,dcc
from src.service.vendasService import VendasService
from src.components.chart_component import ChartComponent
from src.components.table_component import TableComponent
from src.components.filter import Filter_pais
import pandas as pd
import dash_bootstrap_components as dbc
from src.callbacks.vendas_callbacks import register_callbacks


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY]
    )

server = app.server

venda_service: VendasService = VendasService()

df_vendas:pd.DataFrame = venda_service.listarVendasParaTabela()

df_pais: pd.DataFrame = venda_service.listarVendasPais()

df_modelos: pd.DataFrame = venda_service.listarModelos()


app.layout = html.Div([


    html.H1("Dashborad de Vendas de Carros" , style={'textAlign': 'center'}),


    html.Div(

        Filter_pais.dropdown_pais(df_vendas),
        style = {
            "display":"flex",
            "justifyContent":"flex-end",
            "paddingRight":"20px"
        }
    ),
    




    html.Div([
        dcc.Graph(id="graf-modelos"),

    ], style = {"padding": "20px 20px"}),

    html.Div([
        html.Div(
            [dcc.Graph(id="graf-carros-pais")],
            style={"width": "50%", "minWidth": 0}
        ),
        html.Div(
            [dcc.Graph(id="graf-time-vendas")],
            style={"width": "50%", "minWidth": 0}
        ),
    ], style={
        'display': 'flex',
        'gap': '20px',
        "padding": "20px"
    })
        

])

register_callbacks(app, df_vendas)

if __name__ == "__main__":
    app.run(debug=False)

