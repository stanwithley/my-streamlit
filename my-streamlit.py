import streamlit as st
import pandas as pd

st.title("Uploading Files To Streamlit.")

uploaded_file = st.file_uploader("Chose a CSV File:", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File Uploaded Successfully!")
        if 'Month' in df.columns:
            df.set_index('Month', inplace=True)
        st.subheader("Previewing Datas: ")
        st.dataframe(df)

        numeric_columns = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_columns) >= 1:
            selected_columns = st.multiselect("Select Numerical Columns:", numeric_columns)
            if selected_columns:
                st.subheader("Line Chart: ")
                st.line_chart(df[selected_columns])
        else:
            st.warning("There are no numerical columns selected.")
    except Exception as e:
        st.error(f"Error In Reading File: {e}")
else:
    st.info("Please upload a CSV file.")
