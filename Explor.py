import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

udemy = pd.read_csv("data/udemy_courses.csv")
pr = udemy.profile_report()
st.title("Exploratory Data Analysis for Udemy Courses")
if st.button("Generate Report"):
    st_profile_report(pr)