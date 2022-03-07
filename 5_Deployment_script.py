from flask import Flask, request, render_template
import pickle
import numpy as np

model = pickle.load(open('outputs/output_4.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['message']
    classes = model.predict([text])
    print(text)
    return render_template('After.html',data =classes )


if __name__ == '__main__':
    app.run(debug=True)
