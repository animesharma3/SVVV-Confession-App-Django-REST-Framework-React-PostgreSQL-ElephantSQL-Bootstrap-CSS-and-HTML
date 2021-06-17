from django.urls import path
from . import views

urlpatterns = [
    path('', views.userProfileList, name='user_profiles_list'),
    path('<int:pk>', views.AccountDetail, name='account-detail')
]