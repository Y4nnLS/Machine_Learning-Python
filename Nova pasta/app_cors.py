import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/iris', methods=['POST'])
@cross_origin()
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