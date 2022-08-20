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

This is the **EDA App** created in `Streamlit` by `python` using the **pandas-profiling** library.

Made by [Benjamin Trinh](https://www.linkedin.com/in/benjamin-binh-trinh/)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/Benjilitics/Streamlit-EDA-Application/main/a%20sample%20csv%20file.csv)
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
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 3),
                columns=['Variable #1', 'Variable #2', 'Variable #3']
                )
            a['Love Ben?'] = np.random.choice(['Yes', 'No'], len(a))
            a['Who is Ben'] = np.random.choice(['Ben is Doctor Strange', 'Ben is Captain Kiwi', 'Ben is Iron Man', 'Ben is nothing'], len(a))
            a['Label'] = np.random.randint(0, 2, len(a))
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

# Creadit
st.markdown('''
**Credit:** thanks to the clear instruction from [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
''')