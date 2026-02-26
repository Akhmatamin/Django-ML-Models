from django.db import models

class LoanBankModel(models.Model):
    person_age = models.FloatField()
    person_gender = models.CharField()
    person_income = models.FloatField()
    person_emp_exp = models.IntegerField()
    loan_amnt = models.FloatField()
    loan_int_rate = models.FloatField()
    loan_percent_income = models.FloatField()
    cb_person_cred_hist_length = models.FloatField()
    credit_score = models.IntegerField()
    previous_loan_defaults_on_file = models.CharField()
    person_education = models.CharField()
    person_home_ownership = models.CharField()
    loan_intent = models.CharField()


class DiabetesModel(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    BMI = models.IntegerField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()

class AvocadoModel(models.Model):
    firmness = models.FloatField()
    hue= models.IntegerField()
    saturation= models.IntegerField()
    brightness= models.IntegerField()
    color_category= models.CharField()
    sound_db= models.IntegerField()
    weight_g= models.IntegerField()
    size_cm3= models.IntegerField()

class MushroomsModel(models.Model):
    cap_shape = models.CharField()
    cap_surface = models.CharField()
    cap_color = models.CharField()
    bruises = models.CharField()
    odor = models.CharField()

    gill_attachment = models.CharField()
    gill_spacing = models.CharField()
    gill_size = models.CharField()
    gill_color = models.CharField()

    stalk_shape = models.CharField()
    stalk_root = models.CharField()
    stalk_surface_above_ring = models.CharField()
    stalk_surface_below_ring = models.CharField()
    stalk_color_above_ring = models.CharField()
    stalk_color_below_ring = models.CharField()

    veil_color = models.CharField()

    ring_number = models.CharField()
    ring_type = models.CharField()

    spore_print_color = models.CharField()
    population = models.CharField()
    habitat = models.CharField()


class TitanicModel(models.Model):
    Pclass = models.IntegerField()
    Sex =models.CharField()
    Age = models.IntegerField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare =models.FloatField()
    Embarked=models.CharField()


class TelecomModel(models.Model):
    SeniorCitizen = models.IntegerField()
    tenure = models.IntegerField()
    gender = models.CharField()
    Partner = models.CharField()
    Dependents = models.CharField()
    PhoneService = models.CharField()
    MultipleLines = models.CharField()
    InternetService = models.CharField()
    OnlineSecurity = models.CharField()
    OnlineBackup = models.CharField()
    DeviceProtection = models.CharField()
    TechSupport = models.CharField()
    StreamingTV = models.CharField()
    StreamingMovies = models.CharField()
    Contract = models.CharField()
    PaperlessBilling = models.CharField()
    PaymentMethod = models.CharField()
    MonthlyCharges = models.FloatField()
    TotalCharges = models.FloatField()