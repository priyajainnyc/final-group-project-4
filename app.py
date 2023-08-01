# import libraris
import pandas as pd

import numpy as np
from flask import Flask, render_template, request
import pickle

## col names for df
col_names = ['Market Cap', 
            'Forward P/E', 
            'EPS growth next year', 
            'EPS growth past 5 years',
            'EPS growth next 5 years', 
            'Sales growth past 5 years', 
            'Sales',
            'Total Debt/Equity', 
            'Profit Margin',
            'Categorical_BMI_Underweight', 
            'Average True Range',
            'Employees',
            'Volume', 
            'Target Price',
            'Price',
            'Analyst Recom_BUY',
            'Analyst Recom_HOLD']

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# load ml model
model = pickle.load(open('classifier1.pkl', 'rb'))

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """
    Render the main page of the webapp.

    """
    return render_template('index.html')

@app.route("/predict")
def predict():

    X = np.zeros( len(col_names) )
    print("X",X)
    df_XX = pd.DataFrame(data=[dict(zip(col_names, X) ) ] )

    Profit_Margin = f"Profit_Margin_{request.form['Profit_Margin']}"
    print( "Profit_Margin:", Profit_Margin)
    df_XX[ Profit_Margin ] = 1.0


    # EPS_growth_next_5_years = int ( request.form['EPS growth next 5 years'] )
    # print( "EPS growth next 5 years:", EPS growth next 5 years )

    # if EPS_growth_next_5_years <= 10:
    #      df_XX['Categorical_EPSgrowth_low'] = 1.0
    # elif bmi > 10 and bmi < 40:
    #      df_XX['Categorical_EPSgrowth_medium'] = 1.0
    # else:
    #     df_XX['Categorical_EPSgrowth_high'] = 1.0



    print( df_XX )
    print( df_XX.columns )

    prediction = model.predict_proba( df_XX )
    print("prediction",prediction)
    
    output = np.round(prediction[0][1], 2)

    print( 'You are likely: {}'.format(output) )

    if output > (.65):
        page = "BUY.html"
    else:
        page = "HOLD.html"
    return render_template(page, prediction_text='Probability: {}'.format(output))

# start the flask server
if __name__ == '__main__':
    app.run(debug=True)
