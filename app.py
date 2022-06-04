import numpy as np
from flask import Flask, request, render_template
import pickle
import pickle as cPickle
import bz2

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
Dfile=bz2.BZ2File('model','rb')
model=cPickle.load(Dfile)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    if request.method == 'POST':
            a = request.form["Online Order"]
            b = request.form["Book Table"]
            c = request.form["Votes"]
            d = request.form["Location"]
            e = request.form["Restaurant Type"]
            f = request.form["Cuisines"]
            g = request.form["Cost For 2 Person"]
            h = request.form["Type"]

    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
