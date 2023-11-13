
from json import load
from sklearn import tree
from sklearn.datasets import load_iris
import joblib

iris = load_iris()
X,y = iris.data, iris.target

model = tree.DecisionTreeClassifier()
model = model.fit(X,y)

joblib.dump(model, 'model.joblib')

y_pred = model.predict([[ 5, 3.5, 1.2, 0.5 ]])
print(y_pred)
