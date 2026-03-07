from rest_framework import serializers

class LoanBankSerializer(serializers.Serializer):
    person_age = serializers.FloatField()
    person_gender = serializers.CharField()
    person_income = serializers.FloatField()
    person_emp_exp = serializers.IntegerField()
    loan_amnt = serializers.FloatField()
    loan_int_rate = serializers.FloatField()
    loan_percent_income = serializers.FloatField()
    cb_person_cred_hist_length = serializers.FloatField()
    credit_score = serializers.IntegerField()
    previous_loan_defaults_on_file = serializers.CharField()
    person_education = serializers.CharField()
    person_home_ownership = serializers.CharField()
    loan_intent = serializers.CharField()


class DiabetesSerializer(serializers.Serializer):
    Pregnancies = serializers.IntegerField()
    Glucose = serializers.FloatField()
    BloodPressure = serializers.FloatField()
    BMI = serializers.FloatField()
    DiabetesPedigreeFunction = serializers.FloatField()
    Age = serializers.IntegerField()


class AvocadoSerializer(serializers.Serializer):
    firmness = serializers.FloatField()
    hue = serializers.IntegerField()
    saturation = serializers.IntegerField()
    brightness = serializers.IntegerField()
    color_category = serializers.CharField()
    sound_db = serializers.IntegerField()
    weight_g = serializers.IntegerField()
    size_cm3 = serializers.IntegerField()


class MushroomsSerializer(serializers.Serializer):
    cap_shape = serializers.CharField()
    cap_surface = serializers.CharField()
    cap_color = serializers.CharField()
    bruises = serializers.CharField()
    odor = serializers.CharField()

    gill_attachment = serializers.CharField()
    gill_spacing = serializers.CharField()
    gill_size = serializers.CharField()
    gill_color = serializers.CharField()

    stalk_shape = serializers.CharField()
    stalk_root = serializers.CharField()
    stalk_surface_above_ring = serializers.CharField()
    stalk_surface_below_ring = serializers.CharField()
    stalk_color_above_ring = serializers.CharField()
    stalk_color_below_ring = serializers.CharField()

    veil_color = serializers.CharField()

    ring_number = serializers.CharField()
    ring_type = serializers.CharField()

    spore_print_color = serializers.CharField()
    population = serializers.CharField()
    habitat = serializers.CharField()


class TitanicSerializer(serializers.Serializer):
    Pclass = serializers.IntegerField()
    Sex = serializers.CharField()
    Age = serializers.IntegerField()
    SibSp = serializers.IntegerField()
    Parch = serializers.IntegerField()
    Fare = serializers.FloatField()
    Embarked = serializers.CharField()


class TelecomSerializer(serializers.Serializer):
    gender = serializers.CharField()
    SeniorCitizen = serializers.IntegerField()
    Partner = serializers.CharField()
    Dependents = serializers.CharField()
    tenure = serializers.IntegerField()
    PhoneService = serializers.CharField()
    MultipleLines = serializers.CharField()
    InternetService = serializers.CharField()
    OnlineSecurity = serializers.CharField()
    OnlineBackup = serializers.CharField()
    DeviceProtection = serializers.CharField()
    TechSupport = serializers.CharField()
    StreamingTV = serializers.CharField()
    StreamingMovies = serializers.CharField()
    Contract = serializers.CharField()
    PaperlessBilling = serializers.CharField()
    PaymentMethod = serializers.CharField()
    MonthlyCharges = serializers.FloatField()
    TotalCharges = serializers.FloatField()


class EmployeeSerializer(serializers.Serializer):
    Age = serializers.IntegerField()
    DailyRate = serializers.IntegerField()
    DistanceFromHome = serializers.IntegerField()
    Education = serializers.IntegerField()
    EnvironmentSatisfaction = serializers.IntegerField()
    Gender = serializers.CharField()
    HourlyRate = serializers.IntegerField()
    JobInvolvement = serializers.IntegerField()
    JobLevel = serializers.IntegerField()
    JobSatisfaction = serializers.IntegerField()
    MonthlyIncome = serializers.IntegerField()
    MonthlyRate = serializers.IntegerField()
    NumCompaniesWorked = serializers.IntegerField()
    OverTime = serializers.CharField()
    PercentSalaryHike = serializers.IntegerField()
    PerformanceRating = serializers.IntegerField()
    RelationshipSatisfaction = serializers.IntegerField()
    TotalWorkingYears = serializers.IntegerField()
    TrainingTimesLastYear = serializers.IntegerField()
    WorkLifeBalance = serializers.IntegerField()
    YearsAtCompany = serializers.IntegerField()
    YearsInCurrentRole = serializers.IntegerField()
    YearsWithCurrManager = serializers.IntegerField()
    BusinessTravel = serializers.CharField()
    Department = serializers.CharField()
    JobRole = serializers.CharField()
    MaritalStatus = serializers.CharField()


class HousePredictSerializer(serializers.Serializer):
    GrLivArea = serializers.IntegerField()
    YearBuilt = serializers.IntegerField()
    GarageCars = serializers.IntegerField()
    TotalBsmtSF = serializers.IntegerField()
    FullBath = serializers.IntegerField()
    OverallQual = serializers.IntegerField()
    Neighborhood = serializers.CharField()


class StudentSerializer(serializers.Serializer):
    gender = serializers.CharField()
    race_ethnicity = serializers.CharField()
    education = serializers.CharField()
    lunch = serializers.CharField()
    test_preparation = serializers.CharField()
    math_score = serializers.IntegerField()
    reading_score = serializers.IntegerField()