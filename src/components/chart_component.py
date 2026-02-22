import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash.development.base_component import Component


class ChartComponent:

    DARK_BG: any = "#121212"   


    @staticmethod
    def render(df: pd.DataFrame) -> Component:

        fig = px.bar(df, x='carro', y='preco', color='pais', text_auto='.2s')

        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor=ChartComponent.DARK_BG,
            plot_bgcolor=ChartComponent.DARK_BG,
            font=dict(color='#EAEAEA'),
            legend=dict(bgcolor='rgba(0,0,0,0)')
        )

        return html.Div(
            [dcc.Graph(figure=fig)],
            style={
                'padding': '20px',
                'border': '1px solid rgba(255,255,255,0.08)',
                'borderRadius': '25px',
                'boxShadow': '0px 4px 15px rgba(0,0,0,0.5)',
                'backgroundColor': ChartComponent.DARK_BG
            }
        )


    @staticmethod
    def carrosPais(df: pd.DataFrame) -> Component:
        fig = px.bar(
            df,
            x='preco',
            y='pais',
            orientation='h',
            color='pais',
            text_auto='.2s'
        )

        fig.update_layout(
            height=380,
            width=600,
            template='plotly_dark',
            paper_bgcolor=ChartComponent.DARK_BG,
            plot_bgcolor=ChartComponent.DARK_BG,
            font=dict(color='#EAEAEA'),
            legend=dict(bgcolor='rgba(0,0,0,0)')
        )

        fig.update_xaxes(gridcolor="rgba(255,255,255,0.08)")
        fig.update_yaxes(gridcolor="rgba(255,255,255,0.08)")

        return html.Div(
            [dcc.Graph(figure=fig)],
            style={
                'padding': '20px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'border': '1px solid rgba(255,255,255,0.08)',
                'borderRadius': '25px',
                'boxShadow': '0px 4px 15px rgba(0,0,0,0.5)',  # corrigido
                'backgroundColor': ChartComponent.DARK_BG,
                'width': '50%',
                'height': 410
            }
        )


    @staticmethod
    def timeVendas(df: pd.DataFrame) -> Component:

        fig = px.line(df, x='datavenda', y='preco')

        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor=ChartComponent.DARK_BG,
            plot_bgcolor=ChartComponent.DARK_BG,
            height=380,
            width=600,
            font=dict(color='#EAEAEA')
        )

        fig.update_yaxes(range=[10000, 850000])

        fig.update_traces(
            fill="tozeroy",
            fillcolor="rgba(99,110,250,0.2)"
        )

        return html.Div(
            [dcc.Graph(figure=fig)],
            style={
                'padding': '20px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'border': '1px solid rgba(255,255,255,0.08)',
                'borderRadius': '25px',
                'boxShadow': '0px 4px 15px rgba(0,0,0,0.5)',
                'backgroundColor': ChartComponent.DARK_BG,
                'width': '50%',
                'height': 410
            }
        )