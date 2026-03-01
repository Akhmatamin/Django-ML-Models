from django.urls import path
from .views import avocado, diabetes, loan, mushrooms, telecom,titanic

urlpatterns = [
    path('avocado/', avocado.AvocadoAPIView.as_view(), name='Avocado'),
    path('diabetes/', diabetes.DiabetesAPIView.as_view(), name='Diabetes'),
    path('loan/', loan.LoanBankAPIView.as_view(), name='Bank'),
    path('mushrooms/', mushrooms.MushroomsAPIView.as_view(), name='Mushrooms'),
    path('telecom/',telecom.TelecomAPIView.as_view(), name='Telecom'),
    path('titanic/', titanic.TitanicAPIView.as_view(), name='Titanic')
]