import streamlit as st
import pandas as pd
from PIL import Image



st.set_page_config(page_title="Project", layout="centered")
page = st.sidebar.radio("Select One:",["Csv Uploader", "User Info Form", "Image Gallery"])

# CSV Uploader
if page == "Csv Uploader":
    st.title("Csv Uploader")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        search_term = st.text_input("Search:")

        if search_term:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

        sort_col = st.selectbox("Sort by column:", df.columns)
        df = df.sort_values(by=sort_col)

        rows_per_page = 10
        total_pages = max((len(df) - 1) // rows_per_page + 1, 1)

        if total_pages > 1:
            page = st.slider("Select page", 1, total_pages, 1)
        else:
            page = 1

        start = (page - 1) * rows_per_page
        end = start + rows_per_page

        st.caption(f"Showing page {page} of {total_pages} — Total rows: {len(df)}")

        st.dataframe(df.iloc[start:end], use_container_width=True)
    else:
        st.warning("Please upload a CSV file to view the table.")



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
