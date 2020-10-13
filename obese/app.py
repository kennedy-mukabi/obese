import flask
import pickle
import pandas as pd
# Use pickle to load in the pre-trained model.
with open(f'model/bike_model_xgboost.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        height = flask.request.form['height']
        weight = flask.request.form['weight']
        input_variables = pd.DataFrame([[height, weight]],
                                       columns=['height', 'weight'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        if prediction == 1:
            value = "underweight"
        elif prediction == 2:
            value="healthy"
        elif prediction == 3:
            value = "overweight"
        elif prediction == 4:
            value ="obese"
        else:
            value="extremely obese"
        return flask.render_template('main.html',
                                     original_input={'height':height,
                                                     'weight':weight},
                                     result=value,
                                     )
        
if __name__ == '__main__':
    app.run()
  
