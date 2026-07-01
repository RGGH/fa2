from sklearn.linear_model import LinearRegression
import joblib

# Features
# size, bedrooms, distance
X = [
    [50, 1, 10],
    [80, 3, 8],
    [120, 2, 5],
    [150, 5, 7],
    [200, 4, 2],
    [90, 4, 12],
]

y = [
    150000,
    300000,
    280000,
    450000,
    600000,
    320000
]

model = LinearRegression()
model.fit(X,y)

joblib.dump(model, "model.pkl")
