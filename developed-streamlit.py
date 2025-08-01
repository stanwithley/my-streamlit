import streamlit as st
import pandas as pd
from PIL import Image



st.set_page_config(page_title="Project", layout="centered")
page = st.sidebar.radio("Select One:",["Csv Uploader", "User Info Form", "Image Gallery"])

# CSV Uploader
if page == "Csv Uploader":
    st.title("Previewing Csv and LineChart")

    uploaded_file = st.file_uploader("Select a Csv file!", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded!")
            st.dataframe(df)

            numeric_cols = df.select_dtypes(include="number").columns.tolist()

            if numeric_cols:
                col = st.radio("Select Column!", numeric_cols)
                st.line_chart(df[col])
            else:
                st.warning("Column not selected.")
        except Exception as e:
            st.error(f"Error In Reading File!{e}")
    else:
        st.info("Select a Csv file To Start!")



# User Info Form
elif page == "User Info Form":
    st.title("User Information Form")

    with st.form("user_form"):
        name = st.text_input("Enter Your Name:")
        age = st.number_input("Enter Your Age:",  min_value=0, max_value=120, step=1)
        comment = st.text_area("Your feedback:")
        gender = st.radio("Select Your Gender:", ["Male", "Female", "Other"])
        working_days = st.slider("How many days do you work per week?", min_value=1, max_value=7, value=5)
        agree = st.checkbox("I accept the [terms and condition](https://example.com/terms).")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if agree:
                st.success("Information Formed Successfully!")
                st.write(f"**Enter Your Name:** {name}")
                st.write(f"**Enter Your Age:** {age}")
                st.write(f"**Gender:** {gender}")
                st.write(f"**Your feedback:** {comment}")
            else:
                st.warning("You must accept the terms and condition to submit.")

# Image Gallery
elif page == "Image Gallery":

    st.title("Image Gallery")

    uploaded_images = st.file_uploader("Select Your Photos. ", type=["jpg", "jpeg", "png", "gif"], accept_multiple_files=True)

    if uploaded_images:
        st.subheader("Gallery")
        cols = st.columns(3)

        for i, img_file in enumerate(uploaded_images):
            image = Image.open(img_file)
            with cols[i % 3]:
                st.image(image, caption=img_file.name, use_container_width=True)
    else:
        st.info("Please upload one or more photos.")
