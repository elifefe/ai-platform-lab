from sklearn.linear_model import LinearRegression


# Example training data
hours_studied = [[1], [2], [3], [4], [5], [6], [7], [8]]
test_scores = [42, 48, 55, 61, 68, 74, 82, 89]


model = LinearRegression()
model.fit(hours_studied, test_scores)


def predict_score(hours: float) -> float:
    prediction = model.predict([[hours]])
    return round(float(prediction[0]), 2)