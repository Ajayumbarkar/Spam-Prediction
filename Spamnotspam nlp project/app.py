from distutils.log import debug
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('models/spamnotspam.pkl','rb'))

@app.route('/', methods=['POST','GET'])
def home():
    details = request.form
    if request.method == 'GET':
        return render_template('main.html')
    else:
        text = details['mail']
        pred = model.predict([text])
        return render_template('result.html', pred=pred[0])

if __name__ == '__main__':
    app.run(debug=True, port=4000)