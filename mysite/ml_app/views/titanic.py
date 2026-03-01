from rest_framework.response import Response
from rest_framework import views, status
import joblib
from ..serializer import TitanicSerializer
import os
from django.conf import settings
model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'titanic_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'titanic_scaler.pkl')
titanic_model = joblib.load(model_path)
titanic_scaler = joblib.load(scaler_path)


class TitanicAPIView(views.APIView):
    def post(self, request):
        serializer = TitanicSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            embarked = data.pop("Embarked")
            embarked0_1 = [
                1 if embarked == "S" else 0,
                1 if embarked == "Q" else 0,]
            gender = data.pop("Sex")
            gender0_1 = [
                1 if gender == "female" else 0,]

            features = list(data.values()) + embarked0_1 + gender0_1
            scaled = titanic_scaler.transform([features])
            prediction = int(titanic_model.predict(scaled)[0])
            return Response({'Survived': 'Alive' if prediction == 1 else 'Dead'})
        return Response(status=status.HTTP_400_BAD_REQUEST)

