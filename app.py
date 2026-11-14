import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

# Load saved models
folder = os.path.dirname(os.path.abspath(__file__))

preprocessor = joblib.load(
    os.path.join(folder, "loan_preprocessor.pkl")
)

model = joblib.load(
    os.path.join(folder, "loan_logistic_model.pkl")
)

# Website title
st.title("🏦 Loan Approval Prediction System")

st.write(
    "Enter applicant details below to predict loan approval status."
)

st.divider()

# Input form
with st.form("loan_form"):

    st.subheader("Applicant Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])

        married = st.selectbox(
            "Marital Status", ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents", ["0", "1", "2", "3+"]
        )

        education = st.selectbox(
            "Education", ["Graduate", "Not Graduate"]
        )

        self_employed = st.selectbox(
            "Self Employed", ["Yes", "No"]
        )

    with col2:
        applicant_income = st.number_input(
            "Applicant Income", min_value=0, value=5000
        )

        coapplicant_income = st.number_input(
            "Coapplicant Income", min_value=0, value=0
        )

        loan_amount = st.number_input(
            "Loan Amount", min_value=1, value=150
        )

        loan_term = st.number_input(
            "Loan Amount Term", min_value=1, value=360
        )

        credit_history = st.selectbox(
            "Credit History", [1.0, 0.0]
        )

    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

    submit = st.form_submit_button(
        "Predict Loan Status"
    )

# Prediction
if submit:

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    try:
        processed_data = preprocessor.transform(input_data)

        prediction = model.predict(processed_data)

        st.divider()
        st.subheader("Prediction Result")

        if prediction[0] == 1:
            st.success("🎉 Loan Approved!")
        else:
            st.error("❌ Loan Not Approved")

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(processed_data)[0][1]
            st.metric(
                "Model estimated approval probability",
                f"{probability * 100:.2f}%"
            )

        st.caption(
            "This is an educational ML prediction, not an actual lending decision."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")