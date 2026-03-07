from rest_framework.response import Response
from rest_framework import views, status
from ..serializer import StudentSerializer
import os, joblib
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'student_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'student_scaler.pkl')
student_model = joblib.load(model_path)
student_scaler = joblib.load(scaler_path)


class StudentAPIView(views.APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student_dict = serializer.validated_data

            new_st = student_dict.pop('gender')

            gender1_0 = [
                1 if new_st == 'male' else 0,

            ]

            new_race = student_dict.pop('race_ethnicity')

            race1_0 = [
                1 if new_race == 'group B' else 0,
                1 if new_race == 'group C' else 0,
                1 if new_race == 'group D' else 0,
                1 if new_race == 'group E' else 0,
            ]

            new_edu = student_dict.pop('education')
            education1_0 = [
                1 if new_edu == "bachelor's degree" else 0,
                1 if new_edu == "high school" else 0,
                1 if new_edu == "master's degree" else 0,
                1 if new_edu == "some college" else 0,
                1 if new_edu == "some high school" else 0,
            ]

            new_lunch = student_dict.pop('lunch')
            lunch1_0 = [
                1 if new_lunch == "standard" else 0,
            ]

            new_test_preparation = student_dict.pop('test_preparation')
            test_preparation1_0 = [
                1 if new_test_preparation == "none" else 0,
            ]

            feature = list(student_dict.values()) + gender1_0 + race1_0 + education1_0 + lunch1_0 + test_preparation1_0

            scaled_data = student_scaler.transform([feature])
            prediction = student_model.predict(scaled_data)[0]

            return Response({'Writing score is': round(prediction)})