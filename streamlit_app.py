import streamlit as st
import pandas as pd

column = ["Name","Age/Gender","Complaint","Phone Number","Date","Time","Follow_Up"]

if 'data' not in st.session_state:
    st.session_state.data = []

st.write('Data Entry')
form = st.form('data_entry')
value = form.text_area(label='Enter value: ', height=300)
button = form.form_submit_button(label='Submit')
if button:
    result = value.splitlines()
    st.session_state.data.append(result)

df = pd.DataFrame(st.session_state.data, columns=column)
# df = st.dataframe(data=st.session_state.data)
if not df.empty:
    st.write('Data output')
    st.dataframe(df)
    # # save_form = st.form('save_form')
    # file_name = st.text_input('File name')
    # st.download_button(file_name=f'{file_name}.csv', label='Download', data=df)
