from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

inputs = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1,1)
outputs = np.array([1,3,2,5,7,8,8,9,10,12]).reshape(-1,1)

model = LinearRegression()

model.fit(inputs,outputs)

filename = 'regression.sav'
pickle.dump(model, open(filename, 'wb'))

