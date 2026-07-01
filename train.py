# train.py
from sklearn.linear_model import LinearRegression
import joblib

X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
