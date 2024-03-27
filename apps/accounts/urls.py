from django.urls import path

from apps.accounts.views import ProfileUpdateView, ProfileDetailView, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
]
