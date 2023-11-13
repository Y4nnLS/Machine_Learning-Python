import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/happy', methods=['POST'])
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
    