from django.urls import path
from . import views

urlpatterns = [
    path("convert/", views.ConvertCurrencyView.as_view(), name="convert_currency"),
    path('api/convert/', views.ConvertCurrencyView.as_view(), name='convert_currency'),
    path("webapp/", views.webapp, name="webapp"),  
]
