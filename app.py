
from dash import Dash,  html, dash_table
from src.service.vendasService import VendasService
from src.components.chart_component import ChartComponent
from src.components.table_component import TableComponent
import pandas as pd
import dash_bootstrap_components as dbc


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

    ChartComponent.render(df_modelos),

    html.Div([
        ChartComponent.carrosPais(df_pais),
        ChartComponent.timeVendas(df_vendas)
    ], style={'display':'Flex',
              'gap': '20px'})
    
    

])

if __name__ == "__main__":
    app.run(debug=False)

