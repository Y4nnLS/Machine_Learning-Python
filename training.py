from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)

# Carregar o conjunto de dados
data = pd.read_csv("happydata.csv")

# Dividir o conjunto de dados em recursos (X) e rótulos (y)
X = data[["infoavail","housecost","schoolquality","policetrust","streetquality","events"]]
y = data["happy"]

# Treinar um modelo (Random Forest) - Substitua pelo modelo apropriado
model = RandomForestClassifier()
model.fit(X, y)

# Salvar o modelo treinado
joblib.dump(model, "model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data['infoavail'],
        data['housecost'],
        data['schoolquality'],
        data['policetrust'],
        data['streetquality'],
        data['events']
    ]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)