from django.urls import path
from . import views
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
    path('pass_change/', views.pass_change, name='pass_change')
]
