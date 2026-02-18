from dash import html, dcc, callback, Input, Output
import dash
import pandas as pd
import plotly.express as px

# Load data (you'll need to import from your notebook)
# For now, placeholder - you'll update this
dash.register_page(__name__, path='/rec_1', name="Product Strategy")

layout = html.Div([
    html.H1("Recommendation 1: Product Strategy - Size & Price"),
    html.Hr(),
    
    html.H3("Definition"),
    html.P("Focus promotional and shelf space strategies on 150-190g chip packets priced between $3.00-$3.99, as they have the highest total sales for all customer segments."),
    
    html.Hr(),
    html.H3("Key Insights"),
    html.Ul([
        html.Li("Products between 150-190 grams have the highest total sales for all customer segments."),
        html.Li("Products between $3 and $3.99 have the highest total sales across all lifestages."),
        html.Li("There is a moderate positive correlation (r=0.43) between price and sales."),
    ]),
    
    html.Hr(),
    html.H3("Products Matching This Criteria"),
    html.P("Run this code to see the 25 products between 150-190g and $3.00-$3.99:"),
    html.Pre("""
recommended_products = (data['prod_size_grams'] >= 150) & \\
                       (data['prod_size_grams'] <= 190) & \\
                       (data['prod_price'] >= 3.00) & \\
                       (data['prod_price'] <= 3.99)
data[recommended_products]['prod_name'].unique()
    """),
    
    html.Hr(),
    html.Div(id="rec1-chart-placeholder", children=[
        html.P("Charts would be displayed here once connected to your data"),
    ])
])
