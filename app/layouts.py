""" app layout """

from .components import FunctionInputCardWithButton
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from sklearn.datasets import make_classification

header = html.Header("dashEDA",
                     className='title text-center',
                     style={'font-size':42, 'color':'#004ead'})

make_data_card = FunctionInputCardWithButton(
  function=make_classification,
  button_text='Make Data',
  button_color='success',
  button_id='make_classification_button',
  description='Make a classification problem'
)

body = dbc.Container([
  dbc.Row([
    dbc.Col([
      make_data_card.html
    ]),
    dbc.Col([
      dcc.Graph(
        figure=go.Scatter(x=[1,2,3], y=[2,1,3], mode='markers')
      )
    ])
  ])
])
