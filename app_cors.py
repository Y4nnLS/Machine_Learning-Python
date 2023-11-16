import joblib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/happy', methods=['POST'])
@cross_origin()
def get_happy():
    features = request.json
    X = []
    X.append(features['infoavail'])
    X.append(features['housecost'])
    X.append(features['schoolquality'])
    X.append(features['policetrust'])
    X.append(features['streetquality'])
    X.append(features['events'])

    model = joblib.load('model.joblib')
    y_pred = model.predict( [X] )
    happy = [0, 1]
    return jsonify( { 'class' : happy[y_pred[0]] } )

if __name__ == '__main__':
    app.run(debug=True)