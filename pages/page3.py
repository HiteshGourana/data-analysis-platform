import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if "df" not in st.session_state:
    st.warning("⚠️ Please upload dataset first")
    st.stop()
df = st.session_state.df

choice=st.sidebar.radio(
    "Choose Option ",
    options=['Basic Statistics',"Dispersion","Distribution",'Correlation Analysis','Grouping & Aggregation']
)

if choice=='Basic Statistics':
    cols = st.multiselect(
    "Select Numerical Columns",
    options=df.columns
 )

    if cols:
     st.dataframe(df[cols].describe().T)

if choice == "Dispersion":

    cols = st.multiselect(
        "Select Numerical Columns",
        options=df.select_dtypes(include='number').columns
    )

    if cols:

        dispersion_df = pd.DataFrame({
            "Variance": df[cols].var(),
            "Std Deviation": df[cols].std(),
            "IQR": (
                df[cols].quantile(0.75)
                - df[cols].quantile(0.25)
            )
        })

        st.dataframe(dispersion_df)

if choice == "Distribution":

    cols = st.multiselect(
        "Select Numerical Columns",
        options=df.select_dtypes(include='number').columns
    )

    if cols:

        distribution_df = pd.DataFrame({
            "Skewness": df[cols].skew(),
            "Kurtosis": df[cols].kurt()
        })

        st.dataframe(distribution_df)

if choice == "Correlation Analysis":

    numeric_cols = df.select_dtypes(include='number').columns

    cols = st.multiselect(
        "Select Numerical Columns",
        options=numeric_cols
    )

    if len(cols) >= 2:

        corr_matrix = df[cols].corr()

        st.subheader("Correlation Matrix")
        st.dataframe(corr_matrix, use_container_width=True)

        
        corr_data = []

        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                corr_value = df[cols[i]].corr(df[cols[j]])

                if corr_value >= 0.7:
                    relation = "Strong Positive"
                elif corr_value >= 0.3:
                    relation = "Moderate Positive"
                elif corr_value > 0:
                    relation = "Weak Positive"
                elif corr_value <= -0.7:
                    relation = "Strong Negative"
                elif corr_value <= -0.3:
                    relation = "Moderate Negative"
                elif corr_value < 0:
                    relation = "Weak Negative"
                else:
                    relation = "No Correlation"

                corr_data.append([
                    cols[i],
                    cols[j],
                    round(corr_value, 4),
                    relation
                ])

        correlation_df = pd.DataFrame(
            corr_data,
            columns=[
                "Column 1",
                "Column 2",
                "Correlation",
                "Relationship"
            ]
        )

        st.subheader("Correlation Summary")
        st.dataframe(
            correlation_df,
            use_container_width=True
        )

    elif len(cols) == 1:
        st.warning("Please select at least 2 numerical columns.")


if choice == "Grouping & Aggregation":

    st.subheader("📊 Grouping & Aggregation")

    group_by = st.selectbox(
        "Select Group By Column",
        options=df.columns
    )

    analysis_cols = st.multiselect(
        "Select Columns for Analysis",
        options=[c for c in df.columns if c != group_by]
    )
    if analysis_cols:

        agg_dict = {}

        for col in analysis_cols:

            st.markdown(f"### {col}")

            if pd.api.types.is_numeric_dtype(df[col]):
                agg_options = [
                    "sum", "mean", "median",
                    "min", "max", "count",
                    "std", "var", "nunique"
                ]
            else:
                agg_options = [
                    "count", "nunique",
                    "min", "max"
                ]

            selected_aggs = st.multiselect(
                f"Aggregation Functions for {col}",
                options=agg_options,
                default=["count"],
                key=col
            )

            if selected_aggs:
                agg_dict[col] = selected_aggs

        if agg_dict:

            try:
                result = df.groupby(group_by).agg(agg_dict)
                st.dataframe(result, use_container_width=True)

                csv = result.to_csv().encode("utf-8")

                st.download_button(
                    "📥 Download Result",
                    data=csv,
                    file_name="grouped_data.csv",
                    mime="text/csv"
                )

            except Exception as e:
                st.error(f"Error: {e}")
            
