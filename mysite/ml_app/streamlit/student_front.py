import streamlit as st
import requests

st.title('Student Performance')

student_url = 'http://127.0.0.1:8000/student/'

gender = st.selectbox('Gender', ['male', 'female'])
race_ethnicity = st.selectbox('Race group:' ,['group A', 'group B','group C','group D','group E'])
education = st.selectbox('Education', ["bachelor's degree", 'some college', "master's degree",
       "associate's degree", 'high school', 'some high school'])
lunch = st.selectbox('Lunch type', ['standard', 'free/reduced'])
test_preparation = st.selectbox('Test Preparation', ['none', 'completed'])
math_score = st.number_input('Math score', min_value=0, max_value=100, step=1)
reading_score = st.number_input('Reading score', min_value=0, max_value=100, step=1)


data = {
    'gender' : gender,
    'race_ethnicity' : race_ethnicity,
    'education':education,
    'lunch' : lunch,
    'test_preparation': test_preparation,
    'math_score' : math_score,
    'reading_score' : reading_score,
}

if st.button('Predict'):
    try:
        response = requests.post(student_url, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f'Writing score is: {result.get("Writing score is")}')
        else:
            st.error(f'Response: {response.status_code}')
    except requests.exceptions.RequestException:
        st.error('Failed to connect to server!')
