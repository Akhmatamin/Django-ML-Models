from django.urls import path
from .views import avocado, diabetes, loan, mushrooms, telecom,titanic, employee, house_price, student

urlpatterns = [
    path('avocado/', avocado.AvocadoAPIView.as_view(), name='Avocado'),
    path('diabetes/', diabetes.DiabetesAPIView.as_view(), name='Diabetes'),
    path('loan/', loan.LoanBankAPIView.as_view(), name='Bank'),
    path('mushrooms/', mushrooms.MushroomsAPIView.as_view(), name='Mushrooms'),
    path('telecom/',telecom.TelecomAPIView.as_view(), name='Telecom'),
    path('titanic/', titanic.TitanicAPIView.as_view(), name='Titanic'),
    path('employee/', employee.EmployeeAttritionView.as_view(), name='Employee'),
    path('house/', house_price.HousePriceView.as_view(), name='House Price'),
    path('student/', student.StudentAPIView.as_view(), name='Student'),
]