import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load the model
model = pickle.load(open('model_diab_rfc.pkl', 'rb'))

l=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

st.title('Diabetes Prediction Web App')
st.write('This app predicts whether a person has diabetes or not based on various health parameters.')
# User will add the input parameters
Preg=st.slider('Number of Pregnancies', 0, 20, 0)
Glu=st.slider('Glucose Level', 0, 250, 100)
BP=st.slider('Blood Pressure value', 0, 200, 70)
ST=st.slider('Skin Thickness value', 0, 200, 10)
Ins=st.slider('Insulin Level', 0, 900, 120)
BMI=st.slider('BMI value', 0.0, 70.0, 25.0)
DPF=st.slider('Diabetes Pedigree Function value', 0.0, 30.0, 0.5)
Age=st.slider('Age of the Person', 1, 120, 35)

# convert user input into dict
user_data = {'Pregnancies': Preg,
             'Glucose': Glu,
                'BloodPressure': BP,
                'SkinThickness': ST,
                'Insulin': Ins,
                'BMI': BMI,
                'DiabetesPedigreeFunction': DPF,
                'Age': Age}

# convert user_dict into dataframe
user_df=pd.DataFrame([user_data])
# Show the df to user
st.subheader('User Input parameters')
st.write(user_df)

# Apply the model to make predictions
if st.button('Predict'):
    result = model.predict(user_df)
    final_result=result[0]
# add doctor stethoscope image
    if final_result==0:
        st.success('The person is not diabetic 🩺')
    else:
        st.error('The person is diabetic 🩺')