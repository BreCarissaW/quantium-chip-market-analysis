from dash import html, dcc
import dash

dash.register_page(__name__, path='/rec_2', name="Brand Strategy")

layout = html.Div([
    html.H1("Recommendation 2: Brand Strategy - Hero Products"),
    html.Hr(),
    
    html.H3("Definition"),
    html.P("Maintain high visibility of Kettle brand chips with Doritos Corn Chips Supreme as a hero product, as they are top sellers across almost all lifestages."),
    
    html.Hr(),
    html.H3("Key Insights"),
    html.Ul([
        html.Li("Kettle brand chips are the highest selling brand across all lifestages."),
        html.Li("Doritos Corn Chips Supreme sell the most across all lifestages (except midage singles/couples → Smiths Crinkle Chips)."),
        html.Li("Kettle has the strongest product portfolio with multiple products in top 10 across lifestages."),
    ]),
    
    html.Hr(),
    html.H3("Top Kettle Products"),
    html.P("Run this code to see the top 5 selling Kettle products:"),
    html.Pre("""
top_kettle = data.groupby(['prod_brand', 'prod_name'])['tot_sales'].sum() \\
    .sort_values(ascending=False).reset_index()
top_kettle[top_kettle['prod_brand'] == 'Kettle'].head(5)
    """),
    
    html.Hr(),
    html.Div(id="rec2-chart-placeholder", children=[
        html.P("Brand and product comparison charts would be displayed here"),
    ])
])
