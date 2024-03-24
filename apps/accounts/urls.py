from django.urls import path

from apps.accounts.views import ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('<str:slug>/', ProfileDetailView.as_view(), name='profile_detail')
]
