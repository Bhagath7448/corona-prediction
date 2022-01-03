from django.urls import path
from . import views

urlpatterns = [
    path('list_api/',views.list_api,name="list_api"),
    path('corona_prediction/',views.corona_prediction,name="corona_prediction")
]