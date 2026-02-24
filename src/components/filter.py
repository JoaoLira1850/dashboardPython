import pandas as pd
from dash import dcc, html
from dash.development.base_component import Component

class Filter_pais :



    @staticmethod
    def dropdown_pais(df: pd.DataFrame) -> Component:
            
        paises = sorted(df['pais'].dropna().unique().tolist()) 
        
        return html.Div([
            html.Label("Filtrar por pais", style={"marginBottom": "6px", "display":"block"}),
            dcc.Dropdown(
                id="filtro-pais",
                options=[{"label": "Todos", "value": "__ALL__"}] + [{"label": p , "value": p} for p in paises],
                value="__ALL__",
                clearable=False
            )
        ],style={
            "maxWidth":"420px",
            "margin":"0 auto 18px auto",
        })


