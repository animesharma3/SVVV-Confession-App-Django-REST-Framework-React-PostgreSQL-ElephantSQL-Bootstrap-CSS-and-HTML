from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('confessions/', views.confessionList, name='confession-list'),
    path('confessions/<int:pk>/', views.confessionDetail, name='confession-detail'),
    path('confessions/create/', views.confessionCreate, name='confession-create'),
    path('confessions/edit/<int:pk>/', views.confessionEdit, name='confession-edit'),
    path('confessions/delete/<int:pk>/', views.confessionDelete, name='confession-delete'),
]