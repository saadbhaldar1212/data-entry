import uuid
import streamlit as st
import pandas as pd

column = ["Name","Age/Gender","Complaint","Phone Number","Date","Time","Follow_Up"]

if 'data' not in st.session_state:
    st.session_state.data = []

st.write('Data Entry')
form = st.form('data_entry')
value = form.text_area(label='Enter value: ')
button = form.form_submit_button(label='Submit')
if button:
    result = value.splitlines()
    st.session_state.data.append(result)

df = pd.DataFrame(st.session_state.data, columns=column)
if not df.empty:
    st.write('Data output')
    st.dataframe(df)
    save_form = st.form('save_form')
    file_name = save_form.text_input('File name')
    save_to_csv_button = save_form.form_submit_button(label='Save to CSV')
    if save_to_csv_button:
        df.to_csv(f'{file_name}.csv', index=False)
        st.write('File Saved successfully')
