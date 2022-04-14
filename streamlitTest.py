import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

st.write("## Deploying a Neural network for time series forecasting!!")

st.write("Insert the last five observations: ")


default_value_goes_here = 0
user_input1 = st.text_input("Insert the first obs: ", default_value_goes_here)
user_input2 = st.text_input("Insert the second obs: ", default_value_goes_here)
user_input3 = st.text_input("Insert the third obs: ", default_value_goes_here)
user_input4 = st.text_input("Insert the forth obs: ", default_value_goes_here)
user_input5 = st.text_input("Insert the fifth obs: ", default_value_goes_here)

user_input1 = float(user_input1)
user_input2 = float(user_input2)
user_input3 = float(user_input3)
user_input4 = float(user_input4)
user_input5 = float(user_input5)

st.write("## Here are model predictions : ")

model2 = load_model('models/model.h5')

n_steps_x = 5
x_input = np.array([user_input1,user_input2,user_input3,user_input4,user_input5])
x_input = x_input.reshape((1, n_steps_x))

yhat = model2.predict(x_input)

st.write(yhat[0])
