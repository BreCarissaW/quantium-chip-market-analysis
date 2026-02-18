from dash import html, dcc
import dash

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1("Quantium Chip Market Analysis"),
    html.Hr(),
    
    html.H2("Executive Summary"),
    html.Ul([
        html.Li("Focus promotional strategies on 150-190g packets priced $3-$3.99"),
        html.Li("Maintain high visibility of Kettle brand & Doritos Corn Chips Supreme"),
        html.Li("Target older segments (older singles/couples, retirees, older families) - make up 50%+ of sales"),
    ]),
    
    html.Hr(),
    html.H3("Navigate to a recommendation:"),
    html.Ul([
        html.Li(dcc.Link("📦 Recommendation 1: Product Strategy (Size & Price)", href="/rec_1")),
        html.Li(dcc.Link("🏷️ Recommendation 2: Brand Strategy (Kettle & Doritos)", href="/rec_2")),
        html.Li(dcc.Link("👥 Recommendation 3: Customer Targeting (Lifestages)", href="/rec_3")),
    ])
])
