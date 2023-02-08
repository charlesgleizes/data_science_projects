
import plotly.express as px
import pandas as pd

from sklearn.metrics import roc_curve, auc

from utils.get_color import *
import plotly.graph_objects as go

"""
    roc_curve_plot(lat, lon): 
        Usecase:Computes AUC curve
        Input:  y (numerical array): Actual labels
                y_score (numerical array): Predicted labels
        Output: Plotly graph object that depicts the ROC curve
"""

def roc_curve_plot(y, y_score):
    fpr, tpr, thresholds = roc_curve(y, y_score)
    # Evaluating model performance at various thresholds
    df = pd.DataFrame({
        'False Positive Rate': fpr,
        'True Positive Rate': tpr
    }, index=thresholds)
    df.index.name = "Thresholds"
    df.columns.name = "Rate"

    fig_thresh = px.line(
        df, title='TPR and FPR at every threshold',
        width=1000, height=500
    )

    fig_thresh.update_yaxes(scaleanchor="x", scaleratio=1)
    fig_thresh.update_xaxes(range=[0, 1], constrain='domain')
    # fig_thresh.update_traces(line_color=primaryColor(), line_width=5)
    return fig_thresh
