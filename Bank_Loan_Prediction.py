import streamlit as st
from PIL import Image
import pickle

# Load the machine learning model
model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))

# Function to run the application
def run():
    # Set page layout
    st.set_page_config(page_title="Bank Loan Prediction", layout="wide")

    # Header
    st.markdown(
        """
        <div style="background-color:#38E54D;padding:10px;border-radius:10px;">
        <h1 style="color:#FFFF;text-align:left;">Bank Loan Prediction using Machine Learning</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Navigation
    nav_selection = st.sidebar.radio(
        "Navigation",
        ("Home", "Form"),
    )

    # Home page content
    if nav_selection == "Home":
        st.write("Welcome to Bank Loan Prediction!")
        st.write("This is a simple application to predict whether a loan will be approved or not based on user input.")

        # Image
        img1 = Image.open('bank_loan.png')
        img1 = img1.resize((400, 300))
        st.image(img1, use_column_width=False)

    # Form page content
    elif nav_selection == "Form":
        st.write("Please fill out the form below:")

        # Account No
        account_no = st.text_input('Account number')

        # Full Name
        fn = st.text_input('Full Name')

        # Gender
        gen_display = ('Female', 'Male')
        gen = st.selectbox("Gender", gen_display)

        # Marital Status
        mar_display = ('No', 'Yes')
        mar = st.selectbox("Marital Status", mar_display)

        # No of Dependents
        dep_display = ('No', 'One', 'Two', 'More than Two')
        dep = st.selectbox("Dependents", dep_display)

        # Education
        edu_display = ('Not Graduate', 'Graduate')
        edu = st.selectbox("Education", edu_display)

        # Employment Status
        emp_display = ('Job', 'Business')
        emp = st.selectbox("Employment Status", emp_display)

        # Property Area
        prop_display = ('Rural', 'Semi-Urban', 'Urban')
        prop = st.selectbox("Property Area", prop_display)

        # Credit Score
        cred_display = ('Between 300 to 500', 'Above 500')
        cred = st.selectbox("Credit Score", cred_display)

        # Applicant Monthly Income
        mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

        # Co-Applicant Monthly Income
        co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

        # Loan Amount
        loan_amt = st.number_input("Loan Amount", value=0)

        # Loan Duration
        dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
        dur = st.selectbox("Loan Duration", dur_display)

        if st.button("Submit"):
            duration = [60, 180, 240, 360, 480][dur_display.index(dur)]
            features = [[gen_display.index(gen), mar_display.index(mar), dep_display.index(dep),
                         edu_display.index(edu), emp_display.index(emp), mon_income, co_mon_income,
                         loan_amt, duration, cred_display.index(cred), prop_display.index(prop)]]
            prediction = model.predict(features)
            if prediction == 0:
                st.error(
                    f"Hello: {fn} || Account number: {account_no} || "
                    "According to our calculations, you will not get the loan from the bank."
                )
            else:
                st.success(
                    f"Hello: {fn} || Account number: {account_no} || "
                    "Congratulations! You will get the loan from the bank."
                )

run()
