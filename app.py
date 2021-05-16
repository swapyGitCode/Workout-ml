#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import flask as Flask
from flask import request
from flask import render_template
import pickle


# In[12]:


from flask import Flask

app = Flask(__name__)


# In[13]:


@app.route('/')
def home():
    return render_template('WorkoutModel.html')


# In[14]:


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,3)
    loaded_model = pickle.load(open("Workout_flask.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    print(result[0])
    return result[0]


# In[16]:


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        if to_predict_list[0] == 'Male':
            to_predict_list[0] = 0
        else:
            to_predict_list[0] = 1
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result) == 0:
            prediction = 'You are in good shape!!!'
        else:
            prediction = 'Please, start working out'
        return render_template("result.html", prediction = prediction)


# In[17]:


# Main function
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOADED'] = True

