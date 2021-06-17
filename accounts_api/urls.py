from django.urls import path
from . import views

urlpatterns = [
    path('', views.userProfileList, name='user-profiles_list'),
    path('user/<int:pk>', views.AccountDetail, name='account-detail'),
    path('<int:pk>', views.userProfileDetail, name='user-profile-detail'),
    path('current_user', views.currentUser, name='current-user')
]