from dash import Dash, html, dcc, callback, Output, Input, State
import pickle
import pandas as pd

external_stylesheets = [
    'https://unpkg.com/simpledotcss/simple.min.css',
]

with open("scaler.pkl","rb") as f:
    scaler = pickle.load(f)
with open("model.pkl","rb") as f:
    model = pickle.load(f)


app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='AI Stock Recommendation'),
    html.H3(children='Choose parameters to see if your stock is a Buy, Hold or Sell'),
    html.P(children='Buy, Hold or Sell?'),
    html.Br(),
    dcc.Dropdown(
        ["Mic Cap","Sm Cap", "Mid Cap", "Lg Cap", "Mg Cap"],
        id='dropdown-Market Cap',
        placeholder="Choose the Market Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi","Med","Lo"],
        id='dropdown-For P/E Cat',
        placeholder="Choose the Forward P/E category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-Dividend',
        placeholder="Choose if you would like dividend",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-EPS growth this year(%) Cat',
        placeholder="Choose if the stock has EPS growth this year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-EPS growth next year(%) Cat',
        placeholder="Choose if the stock will EPS growth next year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-EPS growth past 5 years (%) Cat',
        placeholder="Choose if the stock has had EPS growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-EPS growth next 5 years (%) Cat',
        placeholder="Choose if the stock will have EPS growth in the next 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Yes","No"],
        id='dropdown-Sales growth past 5 years (%) Cat',
        placeholder="Choose if the stock has had Sales growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi","Med","Lo"],
        id='dropdown-Sales Cat',
        placeholder="Choose the Sales category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi","Med","Lo"],
        id='dropdown-Float Short (%) Cat',
        placeholder="Choose the short percentage of float category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Pos", "Neg"],
        id='dropdown-Profit Margin (%) Cat',
        placeholder="Choose the Profit Margin category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Up", "Down"],
        id='dropdown-Performance (Year) (%) Cat',
        placeholder="Choose the Performance direction for the past year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi", "Med", "Lo"],
        id='dropdown-Employees Cat',
        placeholder="Choose the category for the number of Employees",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Buy", "Hold"],
        id='dropdown-Analyst Rec Cat',
        placeholder="Choose the Analyst Recommendation",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi","Med","Lo"],
        id='dropdown-Risk',
        placeholder="Choose the Risk level",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Hi","Med","Lo"],
        id='dropdown-Volume Cat',
        placeholder="Choose the Volume category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["Pos","Neg"],
        id='dropdown-Var % Cat',
        placeholder="Choose the Variance between the stock target price and the current price",
        style= {
            "width": "30em"
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
    State('dropdown-Market Cap', 'value'),
    State('dropdown-For P/E Cat', 'value'),
    State('dropdown-Dividend', 'value'),
    State('dropdown-EPS growth this year(%) Cat', 'value'),
    State('dropdown-EPS growth next year(%) Cat', 'value'),
    State('dropdown-EPS growth past 5 years (%) Cat', 'value'),
    State('dropdown-EPS growth next 5 years (%) Cat', 'value'),
    State('dropdown-Sales growth past 5 years (%) Cat', 'value'),
    State('dropdown-Sales Cat', 'value'),
    State('dropdown-Float Short (%) Cat', 'value'),
    State('dropdown-Profit Margin (%) Cat', 'value'),
    State('dropdown-Performance (Year) (%) Cat', 'value'),
    State('dropdown-Employees Cat', 'value'),
    State('dropdown-Analyst Rec Cat', 'value'),
    State('dropdown-Risk', 'value'),
    State('dropdown-Volume Cat', 'value'),
    State('dropdown-Var % Cat', 'value'),
    prevent_initial_call=True
)
def update_result(clicks, MarketCap, For_PE, Dividend, EPS_growth_thisyr, EPS_growth_nextyr, 
                  EPS_growth_past5, EPS_growth_next5, Sales_growth_past5, Sales, Float_Short, ProfitMargin,
                  Performance, Employees, Analyst_Rec, Risk, Volume, Var
                  ):
    info_for_prediction = {
        # "MarketCap": 1 if MarketCap=="Mic Cap" else 0,
        # "MarketCap": 1 if MarketCap=="Sm Cap" else 0,
        # "MarketCap": 1 if MarketCap=="Mid Cap" else 0,
        # "MarketCap": 1 if MarketCap=="Lg Cap" else 0,
        # "MarketCap": 1 if MarketCap=="Mg Cap" else 0,
        "MarketCap": str(MarketCap),
        "For_PE": str(For_PE),
        "Dividend": str(Dividend),
        "EPS_growth_thisyr": str(EPS_growth_thisyr),
        "EPS_growth_nextyr": str(EPS_growth_nextyr),
        "EPS_growth_past5": str(EPS_growth_past5),
        "EPS_growth_next5": str(EPS_growth_next5),
        "Sales_growth_past5": str(Sales_growth_past5),
        "Sales": str(Sales),
        "Float_Short": str(Float_Short),
        "ProfitMargin": str(ProfitMargin),
        "Performance": str(Performance),
        "Employees": str(Employees),
        "Analyst_Rec": str(Analyst_Rec),
        "Risk": str(Risk),
        "Volume": str(Volume),
        "Var": str(Var)
        }
    df_predict = pd.DataFrame(info_for_prediction,index=[0])
    df_predict = scaler.transform(df_predict)
    answer = model.predict(df_predict)
    if answer == 0:
        result = "HOLD!"
    else:
        result = "BUY!"
    return result

if __name__ == '__main__':
    app.run(debug=True)