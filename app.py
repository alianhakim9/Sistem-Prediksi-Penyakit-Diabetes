from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    if(format(output) == 0):
        return render_template('index.html', prediction_text='Negatif Diabetes')
    else:
        return render_template('index.html', prediction_text='Positif Diabetes')

if __name__ == '__main__':
    app.run(debug=True)