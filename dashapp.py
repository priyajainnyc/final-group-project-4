from dash import Dash, html, dcc, callback, Output, Input, State
import pickle
import pandas as pd

external_stylesheets = [
    'https://unpkg.com/simpledotcss/simple.min.css',
]

with open("classifier.pkl","rb") as f:
    classifier = pickle.load(f)
with open("classifier1.pkl","rb") as f:
    classifier1 = pickle.load(f)

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='AI Stock Recommendation'),
    html.H3(children='Choose parameters to see if your stock is a BUY or HOLD'),
    html.P(children='BUY or HOLD?'),
    html.Br(),
    dcc.Dropdown(
        ["BUY","HOLD"],
        id='dropdown-recommendation',
        placeholder="Choose the analyst recommemdation",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Technology","Consumer Cyclical", "Communication Services", "Energy", "Healthcare", "Financial", "Consumer Defensive", "Industrials"],
        id='dropdown-sector',
        placeholder="Which sector are you interested in",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-dividend',
        placeholder="Does the stock payout dividend",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Input(
        id='input-marketcap',
        type='number',
        placeholder="Choose the market cap",
        style= {
            "width": "150em"
        },
    ),
    html.Br(),
    dcc.Input(
        id='input-sales',
        type='number',
        placeholder="Choose the sales amount",
        style= {
            "width": "150em"
        },
    ),
    html.Br(),
    dcc.Input(
        id='input-profitmargin',
        type='number',
        placeholder="Choose profit margin ratio",
        style= {
            "width": "150em"
        },
    ),
    html.Br(),
    dcc.Input(
        id='input-multiple',
        type='number',
        placeholder="Currently trading at this P/E multiple",
        style= {
            "width": "150em"
        },
    ),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Br(),
    html.H3(children="Results"),
    html.P(children="", id="p-result")
])

@callback(
    Output('p-result', 'children'),
    Input('submit-val', "n_clicks"),
    State('dropdown-recommendation', 'value'),
    State('dropdown-sector', 'value'),
    State('dropdown-dividend', 'value'),
    State('input-marketcap', 'value'),
    State('input-sales', 'value'),
    State('input-profitmargin', 'value'),
    State('input-multiple', 'value'),
    prevent_initial_call=True
)
def update_result(clicks, recommendation, sector, dividend, amount_marketcap, amount_sales, 
                  amount_profitmargin, count_multiple,
                  ):
    info_for_prediction = {
        "Recommendation": 0 if recommendation=="HOLD" else 1,
        "Sector": 0 if sector=="Technology" else 1,
        "Sector": 0 if recommendation=="Consumer Cyclical" else 1,
        "Sector": 0 if recommendation=="Communication Services" else 1,
        "Sector": 0 if recommendation=="Energy" else 1,
        "Sector": 0 if recommendation=="Healthcare" else 1,
        "Sector": 0 if recommendation=="Financial" else 1,
        "Sector": 0 if recommendation=="Consumer Defensive" else 1,
        "Sector": 0 if recommendation=="Industrials" else 1,
        "Dividend": 0 if dividend=="No" else 1,
        "Market Cap": float(amount_marketcap),
        "Sales": float(amount_sales),
        "Profit Margin": float(amount_profitmargin),
        "Forward P/E": float(count_multiple),
        }
    df_predict = pd.DataFrame(info_for_prediction,index=[0])
    df_predict = classifier.transform(df_predict)
    answer = classifier1.predict(df_predict)
    if answer == 0:
        result = "HOLD!"
    else:
        result = "BUY!"
    return result

if __name__ == '__main__':
    app.run(debug=True)