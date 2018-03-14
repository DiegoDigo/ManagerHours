from django.urls import path
from month.api import views

urlpatterns = [
    path('', views.Months.as_view()),
]
