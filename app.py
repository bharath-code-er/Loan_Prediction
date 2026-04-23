import streamlit as st
import joblib
import numpy as np 

# 🔹 Page Config
st.set_page_config(page_title="Loan Prediction App", page_icon="💰", layout="centered")

# 🔹 Load Model
model = joblib.load("loan_model.pkl")

# 🔹 Title
st.markdown("<h1 style='text-align: center; color: green;'>💰 Loan Approval Prediction</h1>", unsafe_allow_html=True)
st.write("Fill the details below to check loan approval status.")

# 🔹 Sidebar (Better UI)
st.sidebar.header("Applicant Information")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
married = st.sidebar.selectbox("Married", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", [0,1,2,3])
education = st.sidebar.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed", ["Yes", "No"])

# 🔹 Main Inputs
st.subheader("Financial Details")

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input("Applicant Income", min_value=0)

with col2:
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)

loan_amount = st.slider("Loan Amount", 0, 500, 100)
loan_term = st.slider("Loan Term", 0, 500, 360)
credit_history = st.radio("Credit History", [0,1])

# 🔹 Convert Inputs to Model Format
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0

# 🔹 Predict Button
if st.button("🔍 Predict Loan Status"):
    data = np.array([[gender, married, applicant_income, loan_amount, loan_term, credit_history]])

    prediction = model.predict(data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
        st.balloons()
    else:
        st.error("❌ Loan Not Approved")

# 🔹 Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made by Bharath M R</p>", unsafe_allow_html=True)
print(model.n_features_in_)
