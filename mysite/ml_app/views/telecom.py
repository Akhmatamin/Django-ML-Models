from rest_framework import views, status
from rest_framework.response import Response
from ..serializer import TelecomSerializer
import joblib, os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'ml_app', 'model_pkls', 'telecom_tree_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'ml_app', 'scaler_pkls', 'telecom_scaler.pkl')
telecom_model = joblib.load(model_path)
telecom_scaler = joblib.load(scaler_path)

yesNoList = ['Yes']
MULTIPLELINES = ['No phone service','Yes']
INTERNETSERVICE = ['Fiber optic','No']
ONLINESECURITY = ['Yes', 'No internet service']
ONLINEBACKUP = ['Yes', 'No internet service']
DEVICEPROTECTION = ['Yes', 'No internet service']
TECHSUPPORT = ['Yes', 'No internet service']
STREAMINGTV = ['Yes', 'No internet service']
STREAMINGMOVIES = ['Yes', 'No internet service']
CONTRACT = ['One year', 'Two year']
PAPERLESSBILLING = ['Yes']
PAYMENTMETHOD = ['Electronic check','Mailed check','Credit card (automatic)']

# Partner_Yes
# Dependents_Yes
# PhoneService_Yes

class TelecomAPIView(views.APIView):
    def post(self, request):
        serializer = TelecomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            new_gender = data.pop('gender')
            gender01 = [1 if new_gender == 'Male' else 0]

            new_partner = data.pop('Partner')
            partner01 = [1 if new_partner =='Yes' else 0]

            new_dependents = data.pop('Dependents')
            dependents01 = [1 if new_dependents =='Yes' else 0]

            new_phone = data.pop('PhoneService')
            phone01 = [1 if new_phone =='Yes' else 0]

            new_lens = data.pop('MultipleLines')
            lens01 = [1 if new_lens == i else 0 for i in MULTIPLELINES]

            new_internet = data.pop('InternetService')
            internet01 = [1 if new_internet == i  else 0 for i in INTERNETSERVICE]

            new_online = data.pop('OnlineSecurity')
            security01 = [1 if new_online == i  else 0 for i in ONLINESECURITY]

            new_backup = data.pop('OnlineBackup')
            backup01 = [1 if new_backup == i  else 0 for i in ONLINEBACKUP]

            new_protection = data.pop('DeviceProtection')
            protection01 = [1 if new_protection == i else 0 for i in DEVICEPROTECTION]

            new_support = data.pop('TechSupport')
            support01 = [1 if new_support == i else 0 for i in TECHSUPPORT]

            new_stream = data.pop('StreamingTV')
            stream01 = [1 if new_stream == i else 0 for i in STREAMINGTV]

            new_movies = data.pop('StreamingMovies')
            movies01 = [1 if new_movies == i else 0 for i in STREAMINGMOVIES]

            new_contract = data.pop('Contract')
            contract01 = [1 if new_contract == 1 else 0 for i in CONTRACT]

            new_paper = data.pop('PaperlessBilling')
            paper01 = [1 if new_paper =='Yes' else 0]

            new_method = data.pop('PaymentMethod')
            method01 = [1 if new_method == i else 0 for i in PAYMENTMETHOD]

            features = [list(data.values()) + gender01 + partner01 + dependents01 + phone01 +
                        lens01 + internet01 + security01 + backup01 + protection01 +
                        support01 + stream01 + movies01 + contract01 + paper01 + method01]

            scaled = telecom_scaler.transform(features)
            prediction = int(telecom_model.predict(scaled)[0])
            return Response({'Churn:': 'Yes' if prediction == 1 else 'No'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
