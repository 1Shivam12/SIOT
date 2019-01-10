# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 08:11:28 2019

@author: Shivam Bhatnagar
"""

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div(children=[html.H1('Example Graph'),
                                dcc.Graph(id='Example',
                                          figure ={
                                                  'data':[{'x':[1,2,3,4,5], 'y':[5,6,7,2,1],'type':'line', 'name':'boats'},
                                                          {'x':[1,2,3,4,5], 'y':[1,12,12,45,12],'type':'bar', 'name':'cars'},
                                                          ],
                                                  'layout':{
                                                          'title':'Basic Dash Example'                                                
                                                                                                                   
                                                          }
                                                  
                                                  })
                                
                                ])

if __name__ == '__main__':
    app.run_server(debug=True)