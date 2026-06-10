import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title("📊 Automated EDA Tool")

import streamlit as st
import pandas as pd
import time
from pathlib import Path

uploadfile = st.file_uploader(
    "Upload Your Dataset Here",
    type=["csv", "xlsx", "xls", "json", "txt", "parquet"]
)

if uploadfile is not None:

    file_ext = Path(uploadfile.name).suffix.lower()

    try:
        if file_ext == ".csv":
            df = pd.read_csv(uploadfile)

        elif file_ext in [".xlsx", ".xls"]:
            df = pd.read_excel(uploadfile)

        elif file_ext == ".json":
            df = pd.read_json(uploadfile)

        elif file_ext == ".txt":
            df = pd.read_csv(uploadfile, sep=None, engine="python")

        elif file_ext == ".parquet":
            df = pd.read_parquet(uploadfile)

        else:
            st.error("Unsupported file format!")
            st.stop()

        st.dataframe(df.head())

        st.session_state.df = df

        if st.button("Submit"):
            df.to_csv("data/saved_dataset.csv", index=False)

            st.success("Dataset submitted successfully ✅")
            time.sleep(1)

            st.switch_page("pages/page1.py")

    except Exception as e:
        st.error(f"Error loading file: {e}")


