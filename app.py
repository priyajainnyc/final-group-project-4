# import libraris
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle

## col names for df
col_names = ['Mkt Cap Cat_Mic Cap',
             'Mkt Cap Cat_Sm Cap',
             'Mkt Cap Cat_Mid Cap',
             'Mkt Cap Cat_Lg Cap',
             'Mkt Cap Cat_Mg Cap',
             'For P/E Cat_Hi',
             'For P/E Cat_Med',
             'For P/E Cat_Lo',
             'Dividend_Yes',
             'Dividend_No',
             'EPS growth this year(%) Cat_Yes',
             'EPS growth this year(%) Cat_No',
             'EPS growth next year(%) Cat_Yes',
             'EPS growth next year(%) Cat_No',
             'EPS growth past 5 years (%) Cat_Yes',
             'EPS growth past 5 years (%) Cat_No',
             'EPS growth next 5 years (%) Cat_Yes',
             'EPS growth next 5 years (%) Cat_No',
             'Sales growth past 5 years (%) Cat_Yes',
             'Sales growth past 5 years (%) Cat_No',
             'Sales Cat_Hi',
             'Sales Cat_Med',
             'Sales Cat_Lo',
             'Float Short (%) Cat_Hi',
             'Float Short (%) Cat_Med',
             'Float Short (%) Cat_Lo',
             'Profit Margin (%) Cat_Pos',
             'Profit Margin (%) Cat_Neg',
             'Performance (Year) (%) Cat_Up',
             'Performance (Year) (%) Cat_Down',
             'Employees Cat_Hi',
             'Employees Cat_Med',
             'Employees Cat_Lo',
             'Analyst Rec Cat_Buy',
             'Analyst Rec Cat_Hold',
             'Risk_Hi',
             'Risk_Med',
             'Risk_Lo',
             'Volume Cat_Hi',
             'Volume Cat_Med',
             'Volume Cat_Lo',
             'Var % Cat_Pos',
             'Var % Cat_Neg'
            ]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# load ml model
model = pickle.load(open('model.pkl', 'rb'))

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """
    Render the main page of the webapp.

    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    X = np.zeros( len(col_names) )
    print("X",X)
    df_XX = pd.DataFrame(data=[dict(zip(col_names, X) ) ] )

    feat_MarketCap = f"Mkt Cap Cat_{request.form['MarketCap']}"
    print("Feat MarketCap:",feat_MarketCap)
    df_XX[ feat_MarketCap ] = 1.0

    feat_ForPE = f"For P/E Cat_{request.form['ForPE']}"
    print("Feat ForPE:",feat_ForPE)
    df_XX[ feat_ForPE ] = 1.0


    print( df_XX )
    print( df_XX.columns )

    prediction = model.predict_proba( df_XX )
    print("prediction",prediction)
    
    output = np.round(prediction[0][1], 2)

    print( 'You should: {}'.format(output) )

    if output > (.65):
        page = "BUY.html"
    else:
        page = "HOLD.html"
    return render_template(page, prediction_text='Probability: {}'.format(output))

# start the flask server
if __name__ == '__main__':
    app.run(debug=True)
