import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Carregando os dados do arquivo CSV
data = pd.read_csv('happydata.csv')

# Definindo as variáveis de entrada (X) e saída (y)
X = data.drop('happy', axis=1)  # Assume que 'happy' é a coluna de saída
y = data['happy']

# Dividindo os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
# model = tree.DecisionTreeClassifier()
# model.fit(X_train, y_train)

#from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(max_depth=2, random_state=0)
# model.fit(X_train, y_train)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# from sklearn.naive_bayes import GaussianNB
# model = GaussianNB()
# model.fit(X, y)

# Salvando o modelo treinado em um arquivo joblib
joblib.dump(model, 'model.joblib')

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliando a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')
