

from dash import Input, Output
import pandas as pd
from src.components.chart_component import ChartComponent


def register_callbacks(app, df_vendas):

    def filtrar_paises(df: pd.DataFrame, pais: str):

        if pais is None or pais == "__ALL__":
            return df
        return df[df["pais"] == pais].copy()
    
    @app.callback(

        Output("graf-modelos", "figure"),
        Output("graf-carros-pais", "figure"),
        Output("graf-time-vendas", "figure"),
        Input("filtro-pais", "value"),
    )

    def atulizar_graficos(pais):

        df_filtrado = filtrar_paises(df_vendas, pais)

        df_modelos = (
            df_filtrado
            .groupby(["pais","carro"])["preco"]
            .sum()
            .reset_index()
        )

        df_pais = (
            df_filtrado
            .groupby("pais")["preco"]
            .sum()
            .reset_index()
        )

        fig1 = ChartComponent.render(df_modelos)
        fig2 = ChartComponent.carrosPais(df_pais)
        fig3 = ChartComponent.timeVendas(df_filtrado)

        return fig1, fig2, fig3
        
