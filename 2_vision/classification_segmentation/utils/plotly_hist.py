import plotly.express as px
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification
from utils.get_color import *
import plotly.graph_objects as go

"""
    plotly_hist(lat, lon): 
        Usecase:Computes AUC curve
        Input:  X
                    - array for no-silo values (0)
                y
                    - array for silo values (1)
                name_X
                    - nave variable X
                name_y
                    - nave variable y
                title
                    - title of the plot
                x_axis
                    - x_axis title of the plot
                y_axis
                    - y_axis title of the plot
        Output: Plotly graph object that depicts a Hist
"""

# The histogram of scores compared to true labels
def plotly_hist(X, y, name_X, name_y, title, x_axis, y_axis):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=X,
        histnorm='percent',
        name=name_X, # name used in legend and hover labels
        marker_color= primaryColor(),
        opacity=0.75,
    ))
    fig.add_trace(go.Histogram(
        x=y,
        histnorm='percent',
        name=name_y,
        marker_color= secondaryColor(),
        opacity=0.75
    ))  

    fig.update_layout(
        title_text=title, # title of plot
        xaxis_title_text=x_axis, # xaxis label
        yaxis_title_text=y_axis, # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1 # gap between bars of the same location coordinates
    )

    return fig