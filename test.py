import pickle
import numpy as np

regressor = pickle.load(open("yield.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))
print(model.predict([[44, 60, 55, 35, 91, 7, 100]]))
# arr=np.array([0,427,1,2,1254,2000]).reshape(-1,1)
res = regressor.predict([[0,427,1,2,1254]])
print(res)
