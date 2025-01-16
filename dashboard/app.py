import dash
from dash import dcc, html
import requests

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Exemple de tableau de bord avec un graphique simple
app.layout = html.Div([
    html.H1("Données des Pandémies"),
    dcc.Graph(id="pandemic-graph"),
])

# Callback pour charger les données via l'API
@app.callback(
    dash.dependencies.Output("pandemic-graph", "figure"),
    [])
def update_graph():
    response = requests.get("http://localhost:8000/pandemics")
    data = response.json()

    figure = {
        "data": [
            {
                "x": [pandemic["name"] for pandemic in data],
                "y": [pandemic["mortality_rate"] for pandemic in data],
                "type": "bar",
            }
        ],
        "layout": {"title": "Mortalité des Pandémies"},
    }
    return figure

if __name__ == "__main__":
    app.run_server(debug=True)