from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('budgets/add/', views.add_budget, name='add_budget'),
    path('budgets/delete/<int:budget_id>/', views.delete_budget, name='delete_budget'),
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/add/', views.add_goal, name='add_goal'),
    path('goals/delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]
