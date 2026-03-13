import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if "df" not in st.session_state:
    st.warning("⚠️ Please upload dataset first")
    st.stop()
df = st.session_state.df

# DataSet Preview

st.subheader("DataSet Preview")
st.dataframe(df.head())

# Number of Rows And Columns

st.subheader("DataSet Dimensions ")
dimn=pd.DataFrame(df.shape,index=['Rows','Cols'],columns=['Values'])
st.dataframe(dimn)

# Column Data Types
st.subheader("Column Data Types")
dtypes_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
dtypes_df = dtypes_df.reset_index().rename(columns={"index": "Column"})
st.dataframe(dtypes_df)


#Null Values 

st.subheader("Empty Value In DataSet")
null_df=pd.DataFrame(df.isnull().sum(),columns=['Count'])
null_df=null_df.reset_index().rename(columns={"index": "Column"})
st.dataframe(null_df)


#Duplicate Columns In DataSet

st.subheader("Dupblicate Rows")
dupl_df=df.duplicated().sum()
st.write(f"Duplicate Rows Count : {dupl_df}")

if st.button("Next Page"):
       st.switch_page("pages/page2.py")

