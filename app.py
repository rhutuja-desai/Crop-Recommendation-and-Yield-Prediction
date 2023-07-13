import numpy as np
from flask import Flask, request, render_template
import pickle
from dictionaries import get_state
from dictionaries import get_district
from dictionaries import get_seasons
from dictionaries import get_crops

flask_app = Flask(__name__, static_folder='styling')
model = pickle.load(open("model.pkl", "rb"))
regressor = pickle.load(open("yield.pkl","rb"))

@flask_app.route("/")
def Home():
    return render_template("/index.html")

@flask_app.route("/about.html")
def func():
    return render_template("about.html")

@flask_app.route("/contact.html")
def func1():
    return render_template("contact.html")

@flask_app.route("/intermediate.html")
def func2():
    return render_template("intermediate.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    print(float_features)
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(prediction)
    return render_template("intermediate.html", prediction_text = "THE RECOMMENDED CROP IS {}".format(prediction))

@flask_app.route("/yield.html")
def yield1():
    prediction=0
    return render_template("yield.html", prediction_text = "THE PREDICTED YIELD OF RECOMMENDED CROP IS {}".format(prediction))

@flask_app.route("/predictYield", methods = ["POST"])
def predictYield():
    print(request.form.values())
    for i in request.form.values():
        print(i)
    arr = [x for x in request.form.values()]
    data = []
    data.append(get_state(arr[0].upper()))
    data.append(get_district(arr[1].upper()))
    data.append(get_seasons(arr[2].upper()))
    data.append(get_crops(arr[3].upper()))
    data.append(arr[4])
    form_data = np.array(data)
    print(form_data)
    prediction = regressor.predict([form_data])
    return render_template("yield.html", prediction_text = "THE PREDICTED YIELD OF RECOMMENDED CROP IS {}".format(prediction))


if __name__ == "__main__":
    flask_app.run(debug=True)