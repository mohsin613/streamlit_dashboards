import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="National Statistic",
    page_icon="Data@Science"

)
#web app ka title
st.markdown(''' 
    # ***National Statistic***
    ---
    This app is develop to generate rapid-fire EDA process using Python for ML Implementation
    ''')
st.markdown("##### ***Display a Dataframe as an interactive table.***")
st.sidebar.success("Select a page above")


df = pd.DataFrame(px.data.gapminder())
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)
