import streamlit as st

# Page Configuration
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1e3c72;'>💼 Employee Salary Predictor</h1>", unsafe_allow_html=True)

# Education mapping
education_mapping = {
    'LKG (Lower Kindergarten)': 1,
    'UKG (Upper Kindergarten)': 2,
    'Primary School': 3,
    'Middle School': 4,
    'High School': 5,
    'Intermediate': 6,
    'Diploma': 7,
    "Bachelor's Degree": 10,
    "Master's Degree": 13,
    'Doctorate': 16
}

# Workclass mapping
def map_workclass(value):
    mapping = {
        'Private': 0,
        'Self-emp-not-inc': 1,
        'Self-emp-inc': 2,
        'Federal-gov': 3,
        'Local-gov': 4,
        'State-gov': 5,
        'Without-pay': 6,
        'Never-worked': 7
    }
    return mapping.get(value, 0)

# Prediction function
def predict_salary(age, education_num, hours_per_week, workclass_num, gender_num):
    base_salary = 20000
    coef_age = 800
    coef_edu = 2500
    coef_hours = 600
    coef_workclass = 3000
    coef_gender = -2000

    salary = (base_salary +
              coef_age * age +
              coef_edu * education_num +
              coef_hours * hours_per_week +
              coef_workclass * workclass_num +
              coef_gender * gender_num)

    return min(max(salary, 20000), 150000)

# Form Inputs
with st.form("salary_form"):
    age = st.number_input("👤 Age", min_value=18, max_value=90, value=30)
    education = st.selectbox("🎓 Education Level", list(education_mapping.keys()))
    hours_per_week = st.number_input("🕒 Hours Worked per Week", min_value=1, max_value=100, value=40)
    workclass = st.selectbox("🏢 Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
    gender = st.radio("⚧️ Gender", ['Male', 'Female'])

    submit = st.form_submit_button("📊 Predict Salary")

if submit:
    education_num = education_mapping[education]
    workclass_num = map_workclass(workclass)
    gender_num = 0 if gender == "Male" else 1

    predicted_salary = predict_salary(age, education_num, hours_per_week, workclass_num, gender_num)

    st.success(f"💰 Predicted Salary: **${predicted_salary:,.2f}**")
