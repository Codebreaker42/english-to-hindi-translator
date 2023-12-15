import streamlit as st
import json
import requests
input_text=st.text_area(label='Enter Youe English Text')
if st.button('Translate'):
    response = requests.get(f'http://127.0.0.1:5000/response/?document={input_text}')

    if response.status_code == 200:  # Check if the request was successful
        hindi_data = response.json()  # Extract JSON data from the response
        
        # Check if the 'translation' key exists in the JSON data
        if 'translation' in hindi_data:
            translated_text = hindi_data['translation']
            st.write(translated_text)
        else:
            st.write('Translation not available in the response JSON.')
    else:
        st.write(f'Error: Request failed with status code {response.status_code}')
