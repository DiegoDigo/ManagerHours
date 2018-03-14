from django.urls import path, include
from driver.api import views

urlpatterns = [
    path('veiculos/', views.Veicles.as_view()),
    path('meses/', include('month.api.urls')),
]
