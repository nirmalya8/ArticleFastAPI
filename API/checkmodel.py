import pickle
import numpy as np
filename = 'regression.sav'
loaded_model = pickle.load(open(filename, 'rb'))
t = np.array([15]).reshape(-1,1)
print(loaded_model.predict(t))