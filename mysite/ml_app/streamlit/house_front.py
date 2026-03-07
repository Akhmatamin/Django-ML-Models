import streamlit as st
import requests


st.title('House price prediction')
house_url = 'http://127.0.0.1:8000/house/'

GrLivArea = st.number_input('GrLivArea', min_value=10, max_value=5642, step=10)
YearBuilt = st.number_input('YearBuilt', min_value=1500, max_value=2026, step=5)
GarageCars = st.number_input('GarageCars', min_value=0, max_value=20, step=1)
TotalBsmtSF = st.number_input('TotalBsmtSF', min_value=0, max_value=6110, step=10)
FullBath = st.number_input('FullBath', min_value=0, max_value=10, step=1)
OverallQual = st.number_input('Overall Quality:', min_value=1, max_value=10, step=1)
Neighborhood = st.selectbox('Neighborhood', [
    'Blueste',
    'BrDale',
    'BrkSide',
    'ClearCr',
    'CollgCr',
    'Crawfor',
    'Edwards',
    'Gilbert',
    'IDOTRR',
    'MeadowV',
    'Mitchel',
    'NAmes',
    'NPkVill',
    'NWAmes',
    'NoRidge',
    'NridgHt',
    'OldTown',
    'SWISU',
    'Sawyer',
    'SawyerW',
    'Somerst',
    'StoneBr',
    'Timber',
    'Veenker',
])

data = {
    'GrLivArea' : GrLivArea,
    'YearBuilt' : YearBuilt,
    'GarageCars' : GarageCars,
    'TotalBsmtSF' : TotalBsmtSF,
    'FullBath' : FullBath,
    'OverallQual' : OverallQual,
    'Neighborhood' : Neighborhood,
}

if st.button('Predict Price'):
    try:
        response = requests.post(house_url, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f'Predicted Price: {result.get("Predicted price")}')
        else:
            st.error(f'Prediction Failed due to {response.status_code}')

    except requests.exceptions.RequestException:
        st.error(f'Failed connect to Server!')

