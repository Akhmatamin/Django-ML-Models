from rest_framework.response import Response
from rest_framework import views, status
from mysite.ml_app.serializer import DiabetesSerializer
import joblib

diabetes_model = joblib.load('mysite/ml_app/model_pkls/diabetes_model.pkl')
diabetes_scaler = joblib.load('mysite/ml_app/scaler_pkls/diabetes_scaler.pkl')

class DiabetesAPIView(views.APIView):
    def post(self, request):
        instance = DiabetesSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data()

            features = list(data.values())
            scaled = diabetes_scaler.fit_transform([features])
            prediction = diabetes_model.predict(scaled)[0]
            prediction = int(prediction)
            prediction = 'No diabetes' if prediction == 0 else 'Yes,Diabetes'
            return {'Diabetes_outcome': prediction}
        return Response(status=status.HTTP_400_BAD_REQUEST)
