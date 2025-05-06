from django.urls import path
from .views import *

urlpatterns = [
    path('recommend/', recommend_assessments),
    #path('test-csv/', test_csv_load),
]
