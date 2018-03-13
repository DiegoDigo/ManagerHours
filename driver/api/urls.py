from django.urls import path
from driver.api import views

urlpatterns = [
    path('veiculos/', views.Veicles.as_view()),
]
