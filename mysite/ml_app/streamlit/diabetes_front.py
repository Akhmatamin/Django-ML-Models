import streamlit as st
import requests

st.title('Diabetes')

diabet_url = 'http://127.0.0.1:8000/diabetes/'

Pregnancies = st.slider('Pregnancies', min_value=0, max_value=20, step=1)
Glucose = st.number_input('Glucose', min_value=0.0, max_value=200.0, step=10.0)
BloodPressure = st.number_input('BloodPressure', min_value=0.0, max_value=190.0, step=10.0)
BMI = st.number_input('BMI', min_value=0.0, max_value=100.0, step=5.0)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, max_value=200.0, step=10.0)
Age = st.slider('Age', min_value=0, max_value=120, step=1)

data = {
    'Pregnancies': Pregnancies,
    'Glucose' : Glucose,
    'BloodPressure': BloodPressure,
    'BMI': BMI,
    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
    'Age': Age
}

if st.button('Check'):
    try:
        response = requests.post(diabet_url, json=data, timeout=10)
        if response.status_code == 200:
            check = response.json()
            st.success(f"Response : {check.get('Diabetes_outcome')}")
        else:
            st.error(f"Server response: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error('Failed to connect to Server')


