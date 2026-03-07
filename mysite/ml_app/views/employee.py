from rest_framework.response import Response
from rest_framework import views, status
import joblib, os
from django.conf import settings
from ..serializer import EmployeeSerializer

model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'employee_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'employee_scaler.pkl')
employee_model = joblib.load(model_path)
employee_scaler = joblib.load(scaler_path)
# print("scaler expects:", getattr(employee_scaler, "n_features_in_", None))
# print("feature names:", getattr(employee_scaler, "feature_names_in_", None))

OVERTIME = ['Yes', 'No']

JOBROLE= ['Sales Executive' ,'Research Scientist', 'Laboratory Technician',
          'Healthcare Representative', 'Manager',
          'Sales Representative' ,'Research Director' ,'Human Resources']

MARITALSTATUS= ['Single' ,'Married']
BUSINESSTRAVEL = ['Travel_Rarely', 'Travel_Frequently']
DEPARTMENT = ['Sales', 'Research & Development']

class EmployeeAttritionView(views.APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            overtime = data.pop('OverTime')
            overtime01 = [1 if overtime == 'Yes' else 0]

            jobrole = data.pop('JobRole')
            jobrole01 = [1 if jobrole == i else 0 for i in JOBROLE]

            gender = data.pop('Gender')
            gender01 = [1 if gender == 'Male' else 0]

            maritialstatus = data.pop('MaritalStatus')
            maritialstatus01 = [1 if maritialstatus == i else 0 for i in MARITALSTATUS]

            business = data.pop('BusinessTravel')
            business01 = [1 if business == i else 0 for i in BUSINESSTRAVEL]

            department = data.pop('Department')
            department01 = [1 if department == i else 0 for i in DEPARTMENT]

            features = [list(data.values()) + overtime01 + jobrole01 + gender01 + maritialstatus01 + business01 + department01]
            scaled = employee_scaler.transform(features)
            prediction = int(employee_model.predict(scaled)[0])
            return Response({'Attrition': 'Yes' if prediction == 1 else 'No'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



