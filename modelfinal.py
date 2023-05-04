
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt

crop_data = pd.read_csv('C:/Users/Rhutuja Desai/Downloads/junk/crop_recommend.csv')

x = crop_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = crop_data['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

import pickle 
pickle.dump(dt_classifier, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

df= pd.read_csv('C:/Users/Rhutuja Desai/Downloads/junk/croprod.csv')
dfx= df[['State_Name','District_Name', 'Season', 'Crop', 'Area']]
dfy= df['Production']


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

dfle = df
dfle.State_Name = le.fit_transform(dfle.State_Name)
dfle
dfle = df
dfle.District_Name = le.fit_transform(dfle.District_Name)
dfle
dfle.Season = le.fit_transform(dfle.Season)
dfle
dfle.Crop = le.fit_transform(dfle.Crop)
dfle

df.dropna()

df['Yield'] = (df['Production'] / df['Area'])

xxx=df[['State_Name','District_Name','Season', 'Crop', 'Area']]
yyy=df['Production']

from sklearn.model_selection import train_test_split
xx_train,xx_test,yy_train,yy_test=train_test_split(xxx,yyy,test_size=0.2,random_state=5)

xx_train.dropna()

xx_test.dropna()
yy_train.dropna()
yy_test.dropna()

xx_train.fillna(xx_train.mean(), inplace=True)
yy_train.fillna(yy_train.mean(), inplace=True)
xx_test.fillna(xx_test.mean(), inplace=True)
yy_test.fillna(yy_test.mean(), inplace=True)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 40)
model.fit(xx_train,yy_train)

pickle.dump(model, open('yield.pkl','wb'))
model2 = pickle.load(open('yield.pkl','rb'))
