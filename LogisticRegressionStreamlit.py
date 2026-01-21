import pandas as pd
import streamlit as st
import pickle as pkl
import warnings
warnings.filterwarnings('ignore')

model = pkl.load(open('LogisticModel.pkl','rb'))

data = pd.read_csv('student.csv')

st.header('Student Result Predictor')

study_hours = st.slider('Select Hours',0,18)

attendance_percent = st.slider('Select Attendance Percentage',1,100)

previous_score = st.slider('Select Previous Marks',1,100)

Student_Data = [[study_hours,attendance_percent,previous_score]]

if st.button('Predict'):
    result = model.predict(Student_Data)
    if result > 0.7:
        st.markdown(f"<h1 style='text-align : center;'>You Are Going To Pass Exam</h1>",unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='text-align : center;'>You Are Going Fail In Exam</h1>",unsafe_allow_html=True)