import streamlit as st
import requests

st.title('Mushrooms')

mush_url = 'http://127.0.0.1:8000/mushrooms/'

cap_shape = st.selectbox('cap_shape', ['x', 'b', 's', 'f', 'k', 'c'])
cap_surface = st.selectbox('cap_surface', ['s', 'y', 'f', 'g'])
cap_color = st.selectbox('cap_color', ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r'])
bruises = st.selectbox('bruises', ['t', 'f'])
odor = st.selectbox('odor', ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm'])

gill_attachment = st.selectbox('gill_attachment', ['f', 'a'])
gill_spacing = st.selectbox('gill_spacing', ['c', 'w'])
gill_size = st.selectbox('gill_size', ['n', 'b'])
gill_color = st.selectbox('gill_color', ['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o'])

stalk_shape = st.selectbox('stalk_shape', ['e', 't'])
stalk_root = st.selectbox('stalk_root', ['c', 'e', 'r', 'b'])
stalk_surface_above_ring = st.selectbox('stalk_surface_above_ring', ['s', 'f', 'k', 'y'])
stalk_surface_below_ring = st.selectbox('stalk_surface_below_ring', ['s', 'f', 'k', 'y'])
stalk_color_above_ring = st.selectbox('stalk_color_above_ring', ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y'])
stalk_color_below_ring = st.selectbox('stalk_color_below_ring', ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y'])

veil_color = st.selectbox('veil_color', ['w', 'n', 'o', 'y'])

ring_number = st.selectbox('ring_number', ['o', 't', 'n'])
ring_type = st.selectbox('ring_type', ['p', 'e', 'l', 'f', 'n'])

spore_print_color = st.selectbox('spore_print_color', ['k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b'])
population = st.selectbox('population', ['s', 'n', 'a', 'v', 'y', 'c'])
habitat = st.selectbox('habitat', ['u', 'g', 'm', 'd', 'p', 'w', 'l'])


data = {
    'cap_shape': cap_shape,
    'cap_surface': cap_surface,
    'cap_color': cap_color,
    'bruises': bruises,
    'odor': odor,
    'gill_attachment': gill_attachment,
    'gill_spacing': gill_spacing,
    'gill_size': gill_size,
    'gill_color': gill_color,
    'stalk_shape': stalk_shape,
    'stalk_root': stalk_root,
    'stalk_surface_above_ring': stalk_surface_above_ring,
    'stalk_surface_below_ring': stalk_surface_below_ring,
    'stalk_color_above_ring': stalk_color_above_ring,
    'stalk_color_below_ring': stalk_color_below_ring,
    'veil_color': veil_color,
    'ring_number': ring_number,
    'ring_type': ring_type,
    'spore_print_color': spore_print_color,
    'population': population,
    'habitat': habitat,
}

if st.button('Predict'):
    try:
        response = requests.post(mush_url, json=data, timeout=10)
        if response.status_code == 200:
            pred = response.json()
            st.success(f"Answer: {pred.get('Prediction')}")
        else:
            st.error(f"Server responded with {response.status_code}")

    except requests.exceptions.RequestException:
        st.error(f"500 error")




