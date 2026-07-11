from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("titanic_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = np.array([[
        int(request.form["PassengerId"]),
        int(request.form["Pclass"]),
        int(request.form["Sex"]),
        float(request.form["Age"]),
        int(request.form["SibSp"]),
        int(request.form["Parch"]),
        float(request.form["Fare"]),
        int(request.form["Embarked"]),
        int(request.form["FamilySize"]),
        int(request.form["Title"]),
        int(request.form["AgeGroup"])
    ]])

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Survived"
    else:
        result = "Did Not Survive"

    return render_template("index.html", prediction=result)


@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    features = np.array([[
        data["PassengerId"],
        data["Pclass"],
        data["Sex"],
        data["Age"],
        data["SibSp"],
        data["Parch"],
        data["Fare"],
        data["Embarked"],
        data["FamilySize"],
        data["Title"],
        data["AgeGroup"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "prediction": int(prediction)
    })


if __name__ == "__main__":
    app.run(debug=True)