#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:12:07 2018

@author: Manita
"""
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
plotly.tools.set_credentials_file(username='m20180054', api_key='1LD0VLp4rF02lKfRqxa2')
import io
import plotly.graph_objs as go 
from plotly.offline import plot

import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


#Opens up a map in PLOTLY.api

    # 'agg_clustered': table
    # 'CODE': variable to geo
    # 'clusters': to differentiate countries

data = [ dict(
        type = 'choropleth',
        locations = agg_clustered['CODE'],
        z = agg_clustered['clusters'],
        scope = "Europe",
        text = agg_clustered['country'],
        colorscale = [[0,"rgb(250,128,114)"],[0.35,"rgb(175,89,79)"],[0.5,"rgb(70,35,31)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"52.9, 80.8, 92.2"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(0,0,0)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = 'c',
            title = 'Clusters'),
      ) ]

layout = dict(
    title = 'Clusters in the World',
    geo = dict(
        showframe = True,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
        )
    )
)
fig = dict( data=data, layout=layout )


plot(fig, validate=False, filename='CLUSTERS MAP')

# to save as png
# plot(fig, validate=False, filename='d3-world-map.html', image='png')









































