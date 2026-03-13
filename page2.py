import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if "df" not in st.session_state:
    st.warning("⚠️ Please upload dataset first")
    st.stop()
df = st.session_state.df

choice = st.sidebar.radio(
     "Choose for Cleaning",
     ['Remove Duplicate','ChangeDataType','RemoveNullValue']
)

if choice=='Remove Duplicate':
    st.write(f"Total Number of Duplicated Rows is : {df.duplicated().sum()}")
    if st.button("Drop Duplicate "):
        df.drop_duplicates(inplace=True)
        st.success("Remove Duplicated Rows")

if choice=='ChangeDataType':
    col = st.selectbox(
    "Select Column",
    options=df.columns
 )
    st.write(df[col].dtype)
    dtype=st.selectbox(
        "Select the DataType",
         options=['int8','int16','int32','int64','uint8','uint16','uint32','uint64','float16','float32','float64','bool','object','string','datetime64[ns]','timedelta64[ns]','category','Int64','Float64','boolean']
    )
    if st.button("Change"):
      try:
        df[col] = df[col].astype(dtype)
        st.success("Successfully Change")
      except:
       st.warning(f"❌ Cannot convert to {dtype}")



