from django.urls import path
from . import views

urlpatterns = [
     path('dashboard', views.dashboard, name='dashboard'),
    
    
    path('loans/', views.loan_list, name='loan_list'),  
    path('loans/add/', views.add_loan, name='loan_create'),  
    
    
    path('investors/', views.investor_list, name='investor_list'),  
    path('investors/add/', views.add_investor, name='add_investor'), 
]
