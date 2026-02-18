from dash import html, dcc
import dash

dash.register_page(__name__, path='/rec_3', name="Customer Targeting")

layout = html.Div([
    html.H1("Recommendation 3: Customer Targeting - Lifestage Focus"),
    html.Hr(),
    
    html.H3("Definition"),
    html.P("Focus marketing efforts on older singles/couples, retirees, and older families as they make up over 50% of total sales, indicating that they are key customer segments for chips."),
    
    html.Hr(),
    html.H3("Sales by Lifestage"),
    html.Ul([
        html.Li(html.Strong("Older Singles/Couples: ") + "Largest segment + highest premium customer spend"),
        html.Li(html.Strong("Retirees: ") + "Second largest segment"),
        html.Li(html.Strong("Older Families: ") + "Third largest + most transactions + largest budget customers"),
        html.Li(html.Strong("Other segments: ") + "Make up <50% of total sales"),
    ]),
    
    html.Hr(),
    html.H3("Customer Segment Profiles"),
    html.Div([
        html.H4("Older Families"),
        html.Ul([
            html.Li("Make the most chip transactions"),
            html.Li("Largest Budget customer segment in total sales"),
        ]),
        
        html.H4("Older Singles/Couples"),
        html.Ul([
            html.Li("Spend the most money on chips overall"),
            html.Li("Largest Premium customer segment"),
        ]),
    ]),
    
    html.Hr(),
    html.Div(id="rec3-chart-placeholder", children=[
        html.P("Lifestage breakdown and demographic charts would be displayed here"),
    ])
])
