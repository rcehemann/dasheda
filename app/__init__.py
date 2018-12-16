"""
dasheda app assembly
"""
from dash import Dash
from dash_html_components import Div
from dash_bootstrap_components.themes import BOOTSTRAP as theme
from .layouts import header, body

app = Dash(__name__, external_stylesheets=[theme])
app.layout = Div([header, body], className='colspan-12', style={'background-color':'#white'})
