from rest_framework.response import Response
from rest_framework import views, status
from ..serializer import AvocadoSerializer
import joblib, os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, settings.BASE_DIR, 'ml_app', 'model_pkls', 'modelAvo2.pkl')
avocado_model = joblib.load(model_path)

class AvocadoAPIView(views.APIView):
    def post(self, request):
        serializer = AvocadoSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            new_color = data.pop('color_category')
            color0_1 = [
                1 if new_color == 'purple' else 0,
                1 if new_color == 'dark green' else 0,
                1 if new_color == 'green' else 0,
            ]

            features = list(data.values()) + color0_1
            prediction = int(avocado_model.predict([features])[0])
            if prediction == 1:
                prediction = 'Hard'
            elif prediction == 2:
                prediction = 'Pre-conditioned'
            elif prediction == 3:
                prediction = 'Breaking'
            elif prediction == 4:
                prediction = 'Firm-ripe'
            else:
                prediction = 'Ripe'
            return Response({'Ripeness': prediction})
        return Response(status=status.HTTP_400_BAD_REQUEST)