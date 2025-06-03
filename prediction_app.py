import streamlit as st
import pandas as pd
import pickle

# Load model
with open('best_logreg_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Telco Customer Churn Prediction")

# User inputs for the 8 features
tenure = st.number_input('Tenure (months)', min_value=0, max_value=72, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=50.0)
contract_one_year = st.checkbox('Contract: One year')
contract_two_year = st.checkbox('Contract: Two year')
payment_electronic_check = st.checkbox('Payment Method: Electronic check')
internet_fiber_optic = st.checkbox('Internet Service: Fiber optic')
online_security_yes = st.checkbox('Online Security: Yes')
tech_support_yes = st.checkbox('Tech Support: Yes')

# Create DataFrame with inputs matching training features
input_data = pd.DataFrame({
    'Contract_One year': [int(contract_one_year)],
    'Contract_Two year': [int(contract_two_year)],
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'PaymentMethod_Electronic check': [int(payment_electronic_check)],
    'InternetService_Fiber optic': [int(internet_fiber_optic)],
    'OnlineSecurity_Yes': [int(online_security_yes)],
    'TechSupport_Yes': [int(tech_support_yes)]
})

if st.button('Predict Churn'):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is unlikely to churn.")
