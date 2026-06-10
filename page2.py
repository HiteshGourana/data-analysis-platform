import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

if "df" not in st.session_state:
    st.warning("⚠️ Please upload dataset first")
    st.stop()
df = st.session_state.df
st.markdown("""
<style>
[data-testid="stSidebar"]{
    background: rgba(0,0,0,0.2);
    backdrop-filter: blur(10px);
}

.main{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

choice = option_menu(
    menu_title="Data Cleaning",
    options=[
        "Remove A Specific Row",
        "Remove Column",
        "Remove Duplicate",
        "Rename Column",
        "Change Data Type",
        "Remove Null Values",
        "Fill Null Values"
    ],
    icons=[
        "trash",
        "files",
        "arrow-repeat",
        "tag",
        "x-circle",
        "bucket"
    ],
    default_index=0
)

if choice == "Remove A Specific Row":

    col = st.selectbox(
        "Select Column",
        options=df.columns
    )

    search_value = st.text_input("Search Value")

    if search_value:

        filtered_df = df[
            df[col].astype(str).str.contains(
                search_value,
                case=False,
                na=False
            )
        ]

        st.dataframe(filtered_df)

        if not filtered_df.empty:

            selected_row = st.selectbox(
                "Select Row to Delete",
                options=filtered_df.index,
                format_func=lambda x: f"Row {x}"
            )

            if st.button("🗑️ Delete Row"):
                df = df.drop(index=selected_row)
                st.success("Row deleted successfully!")
               
        
if choice=='Remove Column':
   col = st.selectbox(
    "Select Column",
    options=df.columns
 )
   if st.button("Remove"):
    try:
      df.drop(col, axis=1,inplace=True)
      st.success("Removed successfully")
      st.dataframe(df)
    except Exception as e:
     st.error(f"Error: {e}")

if choice=='Remove Duplicate':
     col = st.multiselect(
    "Select Column",
    options=df.columns
 )
     st.write(f"Total Number of Duplicated Rows is : {df[col].duplicated().sum()}")
     if st.button("Drop Duplicate "):
        df.drop_duplicates(subset=col)
        st.success("Remove Duplicated Rows")


if choice=="Rename Column":
    col = st.selectbox(
    "Select Column",
    options=df.columns
 )
    new_name=st.text_input("Enter New Name")
    if st.button("change"):
       df.rename(columns={col: new_name}, inplace=True)
       st.balloons()
       st.success("Column Renamed Successfully!")

if choice=='Change Data Type':
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

if choice=="Remove Null Values":
   col=st.multiselect(
       "Choose Column Prefrence",
        options=df.columns[1:]
   )
   if col:
    st.text(df[col].isnull().sum())
   if st.button("Remove Null Values"):
      try:
         df = df.dropna(subset=col)
         st.success("Complete")
      except:
         st.warning("Something went Wrong")

if choice == "Fill Null Values":
    col1 = st.selectbox(
        "Choose Column",
        options=df.columns[1:]
    )
    if col1:  
     st.text(df[col1].isnull().sum())
    col2 = st.radio(
        "Choose fill with",
        options=["Mean", "Median", "Mode"]
    )

    if st.button("Fill Null Values"):
        try:
            if col2 == "Mean":
                val = df[col1].mean()
                df[col1] = df[col1].fillna(val)

            elif col2 == "Median":
                val = df[col1].median()
                df[col1] = df[col1].fillna(val)

            elif col2 == "Mode":
                val = df[col1].mode()[0]
                df[col1] = df[col1].fillna(val)

            st.success(f"Null values filled using {col2}")
            st.write(df)

        except Exception as e:
            st.error(f"Error: {e}")





    

   
   



      
           
        

   
   
   


