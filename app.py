from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

model = load('modelo_treinado.joblib')

@app.route('/api/classificar', methods=['POST'])
def classificar():
    try:
        data = request.get_json()
        infoavail = data.get('infoavail')
        housecost = data.get('housecost')
        schoolquality = data.get('schoolquality')
        policetrust = data.get('policetrust')
        streetquality = data.get('streetquality')
        events = data.get('events')
        resultado = model.predict([[infoavail, housecost, schoolquality, policetrust, streetquality, events]])[0]
        resposta = {'classe_prevista' : resultado}
        return jsonify(resposta)
    
    except Exception as e:
        return jsonify({'erro' : str(e)})

if __name__ == '__main__':
    app.run(debug=True)
    