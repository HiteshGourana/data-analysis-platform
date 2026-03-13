import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title("📊 Automated EDA Tool")

uploadfile=st.file_uplocoader("Upload Your DataSet Here")

if uploadfile is not None:
    df=pd.read_csv(uploadfile)
    df.to_csv("data/saved_dataset.csv", index=False)
    st.session_state.df = df
    if st.button("Submit"):
       st.success("Dataset submit successfully")
       time.sleep(1)
       st.switch_page("pages/page1.py")


