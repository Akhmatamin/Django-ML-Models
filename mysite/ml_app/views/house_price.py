from rest_framework.response import Response
from rest_framework import views, status
from ..serializer import HousePredictSerializer
import os, joblib
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'house_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'house_scaler.pkl')
house_model = joblib.load(model_path)
house_scaler = joblib.load(scaler_path)


Neighborhood = [
    'Blueste',
    'BrDale',
    'BrkSide',
    'ClearCr',
    'CollgCr',
    'Crawfor',
    'Edwards',
    'Gilbert',
    'IDOTRR',
    'MeadowV',
    'Mitchel',
    'NAmes',
    'NPkVill',
    'NWAmes',
    'NoRidge',
    'NridgHt',
    'OldTown',
    'SWISU',
    'Sawyer',
    'SawyerW',
    'Somerst',
    'StoneBr',
    'Timber',
    'Veenker',
]


class HousePriceView(views.APIView):

    def post(self, request):
        serializer = HousePredictSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_neighborhood = data.get('Neighborhood')
            neighborhood1_0 = [1 if new_neighborhood == i else 0 for i in Neighborhood]

            features = [data['GrLivArea'],
                        data['YearBuilt'],
                        data['GarageCars'],
                        data['TotalBsmtSF'],
                        data['FullBath'],
                        data['OverallQual'],
                        ] + neighborhood1_0
            scaled_data = house_scaler.transform([features])
            prediction = house_model.predict(scaled_data)[0]
            return Response({'Predicted price': prediction})
        return Response(status=status.HTTP_400_BAD_REQUEST)
