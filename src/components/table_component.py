from dash import dash_table, html
import pandas as pd
from dash.development.base_component import Component

class TableComponent:

    @staticmethod
    def render_vendas_table(df: pd.DataFrame) -> Component:


        return html.Div([
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df.columns],
                page_size=10,
                style_table={'overflowX':'auto'},
                style_cell={
                    'textAlign':'left',  
                    'padding': '10px',
                    'fontFamily':'sans-serif'
                },
                style_header = { 
                    'backgroundColor':'rgb(230,230,230)',
                    'fontWeight':'bold'
                },
            )
        ], style = {'padding' : '20px'})
        
