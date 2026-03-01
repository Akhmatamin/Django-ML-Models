from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from ..serializer import LoanBankSerializer
import joblib, os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'modelLoan.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'scalerLoan.pkl')
loan_model = joblib.load(model_path)
loan_scaler = joblib.load(scaler_path)

education = ['Bachelor','Doctorate','High School', 'Master']
home = ['OTHER','OWN', 'RENT']
intent = ['EDUCATION','HOMEIMPROVEMENT','MEDICAL','PERSONAL','VENTURE']

class LoanBankAPIView(views.APIView):
    def post(self, request):
        instance = LoanBankSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_gender = data.pop('person_gender')
            gender0_1 = [1 if new_gender == 'male' else 0]

            new_loan_file = data.pop('previous_loan_defaults_on_file')
            loan_file0_1 = [1 if new_loan_file == 'Yes' else 0]

            new_education = data.pop('person_education')
            education0_1 = [1 if new_education == i else 0 for i in education]

            new_home = data.pop('person_home_ownership')
            home0_1 = [1 if new_home == i else 0 for i in home]

            new_intent = data.pop('loan_intent')
            intent0_1 = [1 if new_intent == i else 0 for i in intent]

            features = list(data.values()) + gender0_1 + loan_file0_1+ education0_1 + home0_1 + intent0_1
            scaled = loan_scaler.transform([features])
            prediction = loan_model.predict(scaled)[0]
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

