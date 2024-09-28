from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('goals/', views.goal_list, name='goal_list'),
]
