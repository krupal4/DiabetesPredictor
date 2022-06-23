from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the pickel file of model
with open("model/diabetes_model.pkl", "rb") as f:
         classifier = pickle.load(f)

# file= '/diabetes_model.pkl '
# classifier = pickle.load( open('file', 'rb') )

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('index.html') # Starter Template

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bp = float(request.form['bloodpressure'])
        st = float(request.form['skinthickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction) # Result Template 

if __name__ == '__main__':
	app.run(debug=True)