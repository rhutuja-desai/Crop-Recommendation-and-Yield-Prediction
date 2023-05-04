import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

# model2= pickle.load(open("yield.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/recom")
def func2():
    return render_template("recommend.html")

@flask_app.route("/about.html")
def func():
    return render_template("about.html")

@flask_app.route("/contact.html")
def func1():
    return render_template("contact.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("recommend.html", prediction_text = "THE RECOMMENDED CROP IS {}".format(prediction))

# @flask_app.route("/yield", methods = ["POST"])
# def yield():
#     string_ip = [str(x) for x in request.form.values()]
#     str_features = [np.array(string_ip)]
#     float_features = [float(x) for x in request.form.values()]
#     features = str_features.append([np.array(float_features)])
#     prediction = model2.predict(features)
#     return render_template("yield.html", prediction_text = "THE YIELD PREDICTED CROP IS {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)