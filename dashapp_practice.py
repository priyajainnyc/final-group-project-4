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
        ["0", "1"],
        id='dropdown-Mkt Cap Cat_Mic Cap',
        placeholder="Choose the Market Cap_Mic Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Mkt Cap Cat_Sm Cap',
        placeholder="Choose the Market Cap_Sm Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Mkt Cap Cat_Mid Cap',
        placeholder="Choose the Market Cap_Mid Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Mkt Cap Cat_Lg Cap',
        placeholder="Choose the Market Cap_Lg Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Mkt Cap Cat_Mg Cap',
        placeholder="Choose the Market Cap_Mg Cap",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-For P/E Cat_Hi',
        placeholder="Choose the Forward P/E category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-For P/E Cat_Med',
        placeholder="Choose the Forward P/E category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-For P/E Cat_Lo',
        placeholder="Choose the Forward P/E category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Dividend_Yes',
        placeholder="Choose if you would like dividend",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Dividend_No',
        placeholder="Choose if you would like dividend",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth this year(%) Cat_Yes',
        placeholder="Choose if the stock has EPS growth this year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
     dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth this year(%) Cat_No',
        placeholder="Choose if the stock has EPS growth this year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth next year(%) Cat_Yes',
        placeholder="Choose if the stock will EPS growth next year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth next year(%) Cat_No',
        placeholder="Choose if the stock will EPS growth next year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth past 5 years (%) Cat_Yes',
        placeholder="Choose if the stock has had EPS growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth past 5 years (%) Cat_No',
        placeholder="Choose if the stock has had EPS growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth next 5 years (%) Cat_Yes',
        placeholder="Choose if the stock will have EPS growth in the next 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-EPS growth next 5 years (%) Cat_No',
        placeholder="Choose if the stock will have EPS growth in the next 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Sales growth past 5 years (%) Cat_Yes',
        placeholder="Choose if the stock has had Sales growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Sales growth past 5 years (%) Cat_No',
        placeholder="Choose if the stock has had Sales growth in the past 5 years",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Sales Cat_Hi',
        placeholder="Choose the Sales category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Sales Cat_Med',
        placeholder="Choose the Sales category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Sales Cat_Lo',
        placeholder="Choose the Sales category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Float Short (%) Cat_Hi',
        placeholder="Choose the short percentage of float category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Float Short (%) Cat_Med',
        placeholder="Choose the short percentage of float category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Float Short (%) Cat_Lo',
        placeholder="Choose the short percentage of float category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Profit Margin (%) Cat_Pos',
        placeholder="Choose the Profit Margin category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
     dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Profit Margin (%) Cat_Neg',
        placeholder="Choose the Profit Margin category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Performance (Year) (%) Cat_Up',
        placeholder="Choose the Performance direction for the past year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Performance (Year) (%) Cat_Down',
        placeholder="Choose the Performance direction for the past year",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Employees Cat_Hi',
        placeholder="Choose the category for the number of Employees",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Employees Cat_Med',
        placeholder="Choose the category for the number of Employees",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Employees Cat_Lo',
        placeholder="Choose the category for the number of Employees",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Analyst Rec Cat_Buy',
        placeholder="Choose the Analyst Recommendation",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Analyst Rec Cat_Hold',
        placeholder="Choose the Analyst Recommendation",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Risk_Hi',
        placeholder="Choose the Risk level_Hi",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Risk_Med',
        placeholder="Choose the Risk level_Med",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Risk_Lo',
        placeholder="Choose the Risk level_Lo",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Volume Cat_Hi',
        placeholder="Choose the Volume category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Volume Cat_Med',
        placeholder="Choose the Volume category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Volume Cat_Lo',
        placeholder="Choose the Volume category",
        style= {
            "width": "30em"
        },
    ),
    html.Br(),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Var % Cat_Pos',
        placeholder="Choose the Variance between the stock target price and the current price",
        style= {
            "width": "30em"
        },
    ),
    dcc.Dropdown(
        ["0", "1"],
        id='dropdown-Var % Cat_Neg',
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
    State('dropdown-Market Cap_Mic Cap', 'value'),
    State('dropdown-Market Cap_Sm Cap', 'value'),
    State('dropdown-Market Cap_Mid Cap', 'value'),
    State('dropdown-Market Cap_Lg Cap', 'value'),
    State('dropdown-Market Cap_Mg Cap', 'value'),
    State('dropdown-For P/E Cat_Hi', 'value'),
    State('dropdown-For P/E Cat_Med', 'value'),
    State('dropdown-For P/E Cat_Lo', 'value'),
    State('dropdown-Dividend_Yes', 'value'),
    State('dropdown-Dividend_No', 'value'),
    State('dropdown-EPS growth this year(%) Cat_Yes', 'value'),
    State('dropdown-EPS growth this year(%) Cat_No', 'value'),
    State('dropdown-EPS growth next year(%) Cat_Yes', 'value'),
    State('dropdown-EPS growth next year(%) Cat_No', 'value'),
    State('dropdown-EPS growth past 5 years (%) Cat_Yes', 'value'),
    State('dropdown-EPS growth past 5 years (%) Cat_No', 'value'),
    State('dropdown-EPS growth next 5 years (%) Cat_Yes', 'value'),
    State('dropdown-EPS growth next 5 years (%) Cat_No', 'value'),
    State('dropdown-Sales growth past 5 years (%) Cat_Yes', 'value'),
    State('dropdown-Sales growth past 5 years (%) Cat_No', 'value'),
    State('dropdown-Sales Cat_Hi', 'value'),
    State('dropdown-Sales Cat_Med', 'value'),
    State('dropdown-Sales Cat_Lo', 'value'),
    State('dropdown-Float Short (%) Cat_Hi', 'value'),
    State('dropdown-Float Short (%) Cat_Med', 'value'),
    State('dropdown-Float Short (%) Cat_Lo', 'value'),
    State('dropdown-Profit Margin (%) Cat_Pos', 'value'),
    State('dropdown-Profit Margin (%) Cat_Neg', 'value'),
    State('dropdown-Performance (Year) (%) Cat_Up', 'value'),
    State('dropdown-Performance (Year) (%) Cat_Down', 'value'),
    State('dropdown-Employees Cat_Hi', 'value'),
    State('dropdown-Employees Cat_Med', 'value'),
    State('dropdown-Employees Cat_Lo', 'value'),
    State('dropdown-Analyst Rec Cat_Buy', 'value'),
    State('dropdown-Analyst Rec Cat_Hold', 'value'),
    State('dropdown-Risk_Hi', 'value'),
    State('dropdown-Risk_Med', 'value'),
    State('dropdown-Risk_Lo', 'value'),
    State('dropdown-Volume Cat_Hi', 'value'),
    State('dropdown-Volume Cat_Med', 'value'),
    State('dropdown-Volume Cat_Lo', 'value'),
    State('dropdown-Var % Cat_Pos', 'value'),
    State('dropdown-Var % Cat_Neg', 'value'),
    prevent_initial_call=True
)
def update_result(clicks, MarketCap_Mic, MarketCap_Sm, MarketCap_Mid, MarketCap_Lg, MarketCap_Mg,
                  For_PE_Hi, For_PE_Med, For_PE_Lo,
                  Dividend_Yes, Dividend_No,
                  EPS_growth_thisyr_Yes, EPS_growth_thisyr_No,
                  EPS_growth_nextyr_Yes, EPS_growth_nextyr_No, 
                  EPS_growth_past5_Yes, EPS_growth_past5_No, 
                  EPS_growth_next5_Yes, EPS_growth_next5_No,
                  Sales_growth_past5_Yes, Sales_growth_past5_No,
                  Sales_Hi, Sales_Med, Sales_Lo,
                  Float_Short_Hi, Float_Short_Med, Float_Short_Lo,
                  ProfitMargin_Pos, ProfitMargin_Neg,
                  Performance_Up, Performance_Down,
                  Employees_Hi, Employees_Med, Employees_Lo,
                  Analyst_Rec_Buy, Analyst_Rec_Hold,
                  Risk_Hi, Risk_Med, Risk_Lo,
                  Volume_Hi, Volume_Med, Volume_Lo, 
                  Var_Pos, Var_Neg
                  ):
    info_for_prediction = {
        "MarketCap_Mic": 0 if MarketCap_Mic=="No" else 1,
        "MarketCap_Sm": 0 if MarketCap_Sm=="No" else 1,
        "MarketCap_Mid": 0 if MarketCap_Mid=="No" else 1,
        "MarketCap_Lg": 0 if MarketCap_Lg=="No" else 1,
        "MarketCap_Mg": 0 if MarketCap_Mg=="No" else 1,
        "For_PE_Hi": 0  if For_PE_Hi=="No" else 1,
        "For_PE_Med": 0  if For_PE_Med=="No" else 1,
        "For_PE_Lo": 0  if For_PE_Lo=="No" else 1,
        "Dividend_Yes": 0 if Dividend_Yes=="No" else 1,
        "Dividend_No": 0 if Dividend_No=="No" else 1,
        "EPS_growth_thisyr_Yes": 0 if EPS_growth_thisyr_Yes=="No" else 1,
        "EPS_growth_thisyr_No": 0 if EPS_growth_thisyr_No=="No" else 1,
        "EPS_growth_nextyr_Yes": 0 if EPS_growth_nextyr_Yes=="No" else 1,
        "EPS_growth_nextyr_No": 0 if EPS_growth_nextyr_No=="No" else 1,
        "EPS_growth_past5_Yes": 0 if EPS_growth_past5_Yes=="No" else 1,
        "EPS_growth_past5_No": 0 if EPS_growth_past5_No=="No" else 1,
        "EPS_growth_next5_Yes": 0 if EPS_growth_next5_Yes=="No" else 1,
        "EPS_growth_next5_No": 0 if EPS_growth_next5_No=="No" else 1,
        "Sales_growth_past5_Yes": 0 if Sales_growth_past5_Yes=="No" else 1,
        "Sales_growth_past5_No": 0 if Sales_growth_past5_No=="No" else 1,
        "Sales_Hi": 0  if Sales_Hi=="No" else 1,
        "Sales_Med": 0  if Sales_Med=="No" else 1,
        "Sales_Lo": 0  if Sales_Lo=="No" else 1,
        "Float_Short_Hi": 0  if Float_Short_Hi=="No" else 1,
        "Float_Short_Med": 0  if Float_Short_Med=="No" else 1,
        "Float_Short_Lo": 0  if Float_Short_Lo=="No" else 1,
        "ProfitMargin_Pos": 0  if ProfitMargin_Pos=="No" else 1,
        "ProfitMargin_Neg": 0  if ProfitMargin_Neg=="No" else 1,
        "Performance_Up": 0  if Performance_Up=="No" else 1,
        "Performance_Down": 0  if Performance_Down=="No" else 1,
        "ProfitMargin_Neg": 0  if ProfitMargin_Neg=="No" else 1,
        "Performance_Up": 0  if Performance_Up=="No" else 1,
        "Performance_Down": 0  if Performance_Down=="No" else 1,
        "Employees_Hi": 0  if Employees_Hi=="No" else 1,
        "Employees_Med": 0  if Employees_Med=="No" else 1,
        "Employees_Lo": 0  if Employees_Lo=="No" else 1,
        "Analyst_Rec_Buy": 0  if Analyst_Rec_Buy=="No" else 1,
        "Analyst_Rec_Hold": 0  if Analyst_Rec_Hold=="No" else 1,
        "Risk_Hi": 0  if Risk_Hi=="No" else 1,
        "Risk_Med": 0  if Risk_Med=="No" else 1,
        "Risk_Lo": 0  if Risk_Lo=="No" else 1,
        "Volume_Hi": 0  if Volume_Hi=="No" else 1,
        "Volume_Med": 0  if Volume_Med=="No" else 1,
        "Volume_Lo": 0  if Volume_Lo=="No" else 1,
        "Var_Pos": 0  if Var_Pos=="No" else 1,
        "Var_Neg": 0  if Var_Neg=="No" else 1,
        # "MarketCap": str(MarketCap),
        # "For_PE": str(For_PE),
        # "Dividend": str(Dividend),
        # "EPS_growth_thisyr": str(EPS_growth_thisyr),
        # "EPS_growth_nextyr": str(EPS_growth_nextyr),
        # "EPS_growth_past5": str(EPS_growth_past5),
        # "EPS_growth_next5": str(EPS_growth_next5),
        # "Sales_growth_past5": str(Sales_growth_past5),
        # "Sales": str(Sales),
        # "Float_Short": str(Float_Short),
        # "ProfitMargin": str(ProfitMargin),
        # "Performance": str(Performance),
        # "Employees": str(Employees),
        # "Analyst_Rec": str(Analyst_Rec),
        # "Risk": str(Risk),
        # "Volume": str(Volume),
        # "Var": str(Var)
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