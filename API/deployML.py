from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

@app.get('/')
def welcome():
    return {'response' : 'Welcome to my deployed Machine Learning Model'}

@app.post("/regression")
def postanitem(inp: int):
    inp = np.array(inp).reshape(-1,1)
    filename = 'regression.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    out = loaded_model.predict(inp)
    print(float(out))
    o = {'Output':float(out)}
    return o
