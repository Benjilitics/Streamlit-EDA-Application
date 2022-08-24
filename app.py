import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image

# Web App Title
image = Image.open('./instantnoodles.png')
st.image(image, caption='- Like a lot of people, Ben loves Noodles and Instant Insights -')

st.markdown('''
# **The INSTANT EDA App**

This no-code instant **Exploratory Data Analysis App** is created with `Streamlit`, writen in `python`, using the **pandas-profiling** library.

Made by [Benjamin Trinh](https://www.linkedin.com/in/benjamin-binh-trinh/)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Or just download this example CSV and try](https://raw.githubusercontent.com/Benjilitics/Streamlit-EDA-Application/main/a%20sample%20csv%20file.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Exploratory Data Analysis Report for the Input Dataset**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to create an Example Dataset and explore the auto-generated insights'):
        # Example data
        @st.cache
        def load_data():
            df = pd.DataFrame(
                np.random.rand(100, 3),
                columns=['Variable #1', 'Variable #2', 'Variable #3']
                )
            df['Love Ben?'] = np.random.choice(['Yes', 'No'], len(df))
            df['Who is Ben'] = np.random.choice(['Ben is Doctor Strange', 'Ben is Captain Kiwi', 'Ben is Iron Man', 'Ben is nothing'], len(df))
            df['Label'] = np.random.randint(0, 2, len(df))
            return df
        dataframe = load_data()
        pr = ProfileReport(dataframe, explorative=True)
        st.header('**Input DataFrame**')
        st.write(dataframe)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

# Creadit
st.markdown('''
**Credit:** thanks to the clear instruction from [Chanin Nantasenamat](https://data-professor.medium.com/) (aka [Data Professor](http://youtube.com/dataprofessor))
''')