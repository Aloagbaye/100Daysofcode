# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:17:11 2022

@author: alomo
"""

from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

model_pk = pickle.load(open("iris_v1.pkl","rb"))
@app.route('/api_predict', methods=['GET','POST'])
def api_predict():
    if request.method == "GET":
        return "Please send POST request"
    elif request.method=="POST":
        data=request.get_json()
        sepal_length = data['sepal_length']
        sepal_width = data['sepal_width']
        petal_length = data['petal_length']
        petal_width = data['petal_width']
        
        input1 = np.array([[sepal_length, sepal_width, petal_length,petal_width]])
        prediction = model_pk.predict(input1)
        
        return str(prediction)
        
app.run()
