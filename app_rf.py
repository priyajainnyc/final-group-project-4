# import libraris
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle

## col names for df
col_names = ['For P/E Cat_Hi',
             'For P/E Cat_Med',
             'For P/E Cat_Lo',
             'Sales Cat_Hi',
             'Sales Cat_Med',
             'Sales Cat_Lo',
             'Performance (Year) (%) Cat_Up',
             'Performance (Year) (%) Cat_Down',
             'Employees Cat_Hi',
             'Employees Cat_Med',
             'Employees Cat_Lo',
             'Risk_Hi',
             'Risk_Med',
             'Risk_Lo',
            ]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# load ml model
model = pickle.load(open('rf_model.pkl', 'rb'))

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

    feat_ForPE = f"For P/E Cat_{request.form['ForPE']}"
    print("Feat ForPE:",feat_ForPE)
    df_XX[ feat_ForPE ] = 1.0

    feat_Sales = f"Sales_{request.form['Sales']}"
    print("Feat Sales:",feat_Sales)
    df_XX[ feat_Sales ] = 1.0

    feat_Performance = f"Performance (Year) (%) Cat_{request.form['Performance']}"
    print("feat_Performance:",feat_Performance)
    df_XX[ feat_Performance ] = 1.0

    feat_Employees = f"Employees Cat_{request.form['Employees']}"
    print("feat_Employees:",feat_Employees)
    df_XX[ feat_Employees ] = 1.0

    feat_Risk = f"Risk_{request.form['Risk']}"
    print("feat_Risk:",feat_Risk)
    df_XX[ feat_Risk ] = 1.0

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
