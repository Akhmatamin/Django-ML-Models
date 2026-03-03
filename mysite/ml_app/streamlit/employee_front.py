import streamlit as st
import requests

st.title('Employee Attrition')

employee_url = 'http://127.0.0.1:8000/employee/'

Age = st.number_input('Age', min_value=0, max_value=120, step=1)
DailyRate = st.number_input('DailyRate', min_value=0, max_value=120, step=1)
DistanceFromHome = st.number_input('DistanceFromHome', min_value=0, max_value=120, step=1)
Education = st.number_input('Education', min_value=0, max_value=120, step=1)
EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction', min_value=0, max_value=120, step=1)
Gender = st.selectbox('Gender', ['Female','Male'])
HourlyRate = st.number_input('HourlyRate', min_value=0, max_value=120, step=1)
JobInvolvement = st.number_input('JobInvolvement', min_value=0, max_value=120, step=1)
JobLevel = st.number_input('JobLevel', min_value=0, max_value=120, step=1)
JobSatisfaction = st.number_input('JobSatisfaction', min_value=0, max_value=120, step=1)
MonthlyIncome = st.number_input('MonthlyIncome', min_value=0, max_value=120, step=1)
MonthlyRate = st.number_input('MonthlyRate', min_value=0, max_value=120, step=1)
NumCompaniesWorked = st.number_input('NumCompaniesWorked', min_value=0, max_value=120, step=1)
OverTime = st.selectbox('OverTime', ['Yes', 'No'])
PercentSalaryHike = st.number_input('PercentSalaryHike', min_value=0, max_value=120, step=1)
PerformanceRating = st.number_input('PerformanceRating', min_value=0, max_value=120, step=1)
RelationshipSatisfaction = st.number_input('RelationshipSatisfaction', min_value=0, max_value=120, step=1)
TotalWorkingYears = st.number_input('TotalWorkingYears', min_value=0, max_value=120, step=1)
TrainingTimesLastYear = st.number_input('TrainingTimesLastYear', min_value=0, max_value=120, step=1)
WorkLifeBalance = st.number_input('WorkLifeBalance', min_value=0, max_value=120, step=1)
YearsAtCompany = st.number_input('YearsAtCompany', min_value=0, max_value=120, step=1)
YearsInCurrentRole = st.number_input('YearsInCurrentRole', min_value=0, max_value=120, step=1)
YearsWithCurrManager = st.number_input('YearsWithCurrManager', min_value=0, max_value=120, step=1)
BusinessTravel = st.selectbox('Gender', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
Department = st.selectbox('Gender', ['Sales', 'Research & Development', 'Human Resources'])
JobRole = st.selectbox('Gender', ['Sales Executive' ,'Research Scientist', 'Laboratory Technician','Manufacturing Director' ,
          'Healthcare Representative', 'Manager',
          'Sales Representative' ,'Research Director' ,'Human Resources'])
MaritalStatus = st.selectbox('Gender', ['Single' ,'Married', 'Divorced'])

data = {
    'Age': Age,
    'DailyRate': DailyRate,
    'DistanceFromHome': DistanceFromHome,
    'Education': Education,
    'EnvironmentSatisfaction': EnvironmentSatisfaction,
    'Gender': Gender,
    'HourlyRate': HourlyRate,
    'JobInvolvement': JobInvolvement,
    'JobLevel': JobLevel,
    'JobSatisfaction': JobSatisfaction,
    'MonthlyIncome': MonthlyIncome,
    'MonthlyRate': MonthlyRate,
    'NumCompaniesWorked': NumCompaniesWorked,
    'OverTime': OverTime,
    'PercentSalaryHike': PercentSalaryHike,
    'PerformanceRating': PerformanceRating,
    'RelationshipSatisfaction': RelationshipSatisfaction,
    'TotalWorkingYears': TotalWorkingYears,
    'TrainingTimesLastYear': TrainingTimesLastYear,
    'WorkLifeBalance': WorkLifeBalance,
    'YearsAtCompany': YearsAtCompany,
    'YearsInCurrentRole': YearsInCurrentRole,
    'YearsWithCurrManager': YearsWithCurrManager,
    'BusinessTravel': BusinessTravel,
    'Department': Department,
    'JobRole': JobRole,
    'MaritalStatus': MaritalStatus
}

if st.button('Predict'):
    try:
        response = requests.post(employee_url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f'Response: {result.get("Attrition")}')
        else:
            st.error(f'Error: {response.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'No connection:')