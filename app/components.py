""" larger component classes """

import dash_bootstrap_components as dbc
import dash_html_components as html
# helper functions

def dict_default_args(func):
  names = func.__doc__.split('Returns')[0]
  names = ' '.join(names.split("Parameters")[-1].split('-')[1::]).split('\n\n')
  names = [x.split(' : ')[0].strip() for x in names]
  return dict(zip(names, func.__defaults__))

def inputs_from_dict(dictionary, id_prefix=''):
  return [dbc.InputGroup([
    dbc.InputGroupAddon(key, addon_type="prepend"),
    dbc.Input(placeholder=value, id=id_prefix+key)
  ]) for key,value in dictionary.items()]

# classes

class BaseComponent():
  def __init__(self):
    self._defaults = []
    self._html = []
    self._function = None
    return None

  def __repr__(self):
    return self.__class__.__name__ + "(function=" + str(self._function) + ")"

  @property
  def function(self):
    return self._function

  @property
  def html(self):
    return self._html

  def get_kwargs(self):
    return {}

  def buttonPushed(self):
    return self.function(
      **self.get_kwargs()
    )

class FunctionInputCardWithButton(BaseComponent):
  def __init__(self,
               function=lambda x: None,
               button_text='Button',
               button_color='primary',
               button_class='mr-1',
               button_id=None,
               description='FunctionInputCardWithButton'):

    self._defaults = dict_default_args(function)
    self._function = function
    self._html = dbc.Card([
      dbc.CardHeader(description),
      dbc.CardBody([
        dbc.CardText(html.Div(inputs_from_dict(self._defaults, id_prefix=str(self))))
      ]),
      dbc.CardFooter(dbc.Button(button_text,
                                color=button_color,
                                className=button_class,
                                id=button_id))
    ])
