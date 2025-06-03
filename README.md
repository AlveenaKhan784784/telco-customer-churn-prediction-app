# Telco Customer Churn Prediction App

An end-to-end machine learning project that predicts customer churn for a telecom company using logistic regression and Streamlit. This project involves data preprocessing, feature engineering, model building, evaluation, and deployment using an interactive web application.


**Live App**: [Streamlit Demo](https://telco-customer-churn-prediction-app-jhebpmmuizyzweryuxd4aa.streamlit.app/)

**Dataset**: [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)


## Project Objective

To help telecom companies identify customers who are likely to churn and take preemptive action. The solution involves building a logistic regression model based on customer demographics, service details, and account information.


##  Tools & Technologies

- **Programming**: Python  
- **Libraries**: pandas, numpy, matplotlib, seaborn, scikit-learn, imbalanced-learn  
- **Modeling**: Logistic Regression  
- **App Interface**: Streamlit  
- **Environment**: Jupyter Notebook


## Steps Followed

### 1. Data Preprocessing

- Removed duplicates
- Handled missing values (e.g., total charges)
- Converted categorical variables using encoding
- Feature selection and transformation

### 2. Class Imbalance Handling

- Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to balance churn labels.

### 3. Model Building

- Trained a **Logistic Regression** classifier
- Performed train-test split
- Evaluated using confusion matrix, precision, recall, F1-score

### 4. Streamlit Web App

- Created a user interface to input customer data
- Integrated the trained model to return churn prediction
- Displayed results in a clean, intuitive format

---

## Key Insights

- **Tenure and Monthly Charges** are strong indicators of churn.
- Customers with **month-to-month contracts** are more likely to leave.
- Users with **online security and tech support** are less likely to churn.
- **Senior citizens** show a slightly higher churn tendency.


## Conclusion

This project demonstrates:

- End-to-end understanding of the data science lifecycle.
- Ability to clean, preprocess, and model real-world data.
- Skill in deploying machine learning models with **Streamlit**.
- Effective use of **logistic regression** to generate business insights.

The final product is a production-ready app that can support customer retention strategies in the telecom industry.

