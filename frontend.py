import os
import requests
import streamlit as st

st.set_page_config(page_title='Insurance Premium Predictor')
st.title('Insurance Premium Category Predictor')

api_url = st.sidebar.text_input('FastAPI URL', os.getenv('API_URL', 'http://54.253.43.249:8000'))

occupations = ['retired', 'freelancer', 'student', 'government_job',
               'business_owner', 'unemployed', 'private_job']

with st.form('details'):
    age = st.number_input('Age', min_value=1, max_value=119, value=30)
    weight = st.number_input('Weight (kg)', min_value=1.0, value=65.0)
    height = st.number_input('Height (m)', min_value=0.5, max_value=2.5, value=1.70)
    income_lpa = st.number_input('Annual income (LPA)', min_value=0.0, value=10.0)
    smoker = st.selectbox('Are you a smoker?', [False, True], format_func=lambda x: 'Yes' if x else 'No')
    city = st.text_input('City', 'Mumbai')
    occupation = st.selectbox('Occupation', occupations)
    submitted = st.form_submit_button('Predict')

if submitted:
    payload = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occupation': occupation
    }
    try:
        response = requests.post(f"{api_url.rstrip('/')}/predict", json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted premium category: **{result['predicted_catgeory']}**")
            st.write(f"Confidence: {result['confidence']:.2%}")
            st.bar_chart(result['class_proabilites'])
        else:
            st.error(f'API error {response.status_code}: {response.text}')
    except requests.exceptions.RequestException as e:
        st.error(f'Could not reach the API at {api_url}: {e}')
