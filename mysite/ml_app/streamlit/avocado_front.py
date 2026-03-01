import streamlit as st
import requests

st.title('Avocado')

avo_url = 'http://127.0.0.1:8000/avocado/'

firmness = st.number_input('Firmness level', min_value=0.0,max_value=1000.0, step=0.1)
hue = st.number_input('Hue level', min_value=0,max_value=360, step=1)
saturation = st.number_input('Saturation level', min_value=0,max_value=360, step=1)
brightness = st.number_input('Brightness level', min_value=0,max_value=360, step=1)
color_category = st.selectbox('Color category', ['purple', 'green', 'dark green','black'])
sound_db = st.slider('Sound DB', min_value=0, max_value=80, step=1)
weight_g = st.number_input('Weight G', min_value=0, max_value=300, step=10)
size_cm3 = st.number_input('Size CM3', min_value=0, max_value=300, step=10)

avo_data = {
    'firmness': firmness,
    'hue': hue,
    'saturation': saturation,
    'brightness': brightness,
    'color_category': color_category,
    'sound_db': sound_db,
    'weight_g': weight_g,
    'size_cm3': size_cm3
}


if st.button('Predict'):
    try:
        response = requests.post(avo_url, json=avo_data, timeout=5)
        prediction = response.json()
        if response.status_code == 200:
            st.success(f"Ripeness: {prediction.get('Ripeness')}")
        else:
            st.error(f"Server response: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error(f'Failed to connect')


