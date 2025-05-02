from django.urls import path
from .views.auth import AuthView

urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
]