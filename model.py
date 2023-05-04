import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle 


crop_data = pd.read_csv('C:/Users/Rhutuja Desai/Downloads/junk/crop_recommend.csv')
crop_data.head
x = crop_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = crop_data['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

pickle.dump(dt_classifier, open('model.pkl','wb'))



# @flask_app.route("/predictYield", methods = ["POST"])
# def predict():
#     string_ip = [str(x) for x in request.form.values()]
#     features = [np.array(string_ip)]
#     prediction = model.predict(features)
#     return render_template("intermediate.html", prediction_text = "THE RECOMMENDED CROP IS {}".format(prediction))

