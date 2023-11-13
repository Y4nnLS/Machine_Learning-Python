import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/iris', methods=['POST'])
def get_specie():
    features = request.json

    X = []
    X.append(features['SepalLengthCm'])
    X.append(features['SepalWidthCm'])
    X.append(features['PetalLengthCm'])
    X.append(features['PetalWidthCm'])

    model = joblib.load('model.joblib')
    y_pred = model.predict( [X] )
    species = ['Iris-setosa','Iris-versicolor','Iris-virginica']
    return jsonify( { 'class' : species[y_pred[0]] } )

if __name__ == '__main__':
    app.run(debug=True)