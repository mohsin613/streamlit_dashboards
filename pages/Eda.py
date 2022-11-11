import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#web app ka title
st.markdown(''' 
    # ***Expolatory Data Analysis Web App***
This app is develop to generate reports using pandas profiling ***EDA App***
    ''')

#how we upload a file from pc
with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file=st.sidebar.file_uploader("upload your file",type=['csv'])
    df=sns.load_dataset("titanic")
    st.sidebar.markdown("[Example Csv File](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)")

#profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header("**Input DataFrame**")
    st.write('---')
    st.header('**Profiling Report With Pandas**')
    st_profile_report(pr)
else:
    st.info("Awaiting for csv file for upload")
    if st.button('Press to use example data'):
        #example data set
        @st.cache
        def load_data():
            a=pd.DataFrame(np.random.rand(100,5),columns=["A","B","C","D","E"])
            return a
            df=load_csv()
        df=load_data()
        pr=ProfileReport(df,explorative=True)
        st.header("**Input DataFrame**")
        st.write('---')
        st.header('**Profiling Report With Pandas**')
        st_profile_report(pr)


