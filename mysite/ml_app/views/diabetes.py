from rest_framework.response import Response
from rest_framework import views, status
from ..serializer import DiabetesSerializer
import joblib, os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'diabetes_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'diabetes_scaler.pkl')
diabetes_model = joblib.load(model_path)
diabetes_scaler = joblib.load(scaler_path)

class DiabetesAPIView(views.APIView):
    def post(self, request):
        instance = DiabetesSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            features = list(data.values())
            scaled = diabetes_scaler.transform([features])
            prediction = diabetes_model.predict(scaled)[0]
            prediction = int(prediction)
            prediction = 'No diabetes' if prediction == 0 else 'Yes,Diabetes'
            return Response({'Diabetes_outcome': prediction})
        return Response(status=status.HTTP_400_BAD_REQUEST)
