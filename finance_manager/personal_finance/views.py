from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense, Budget, FinancialGoal

# View for the homepage
def dashboard(request):
    expenses = Expense.objects.all()
    budgets = Budget.objects.all()
    goals = FinancialGoal.objects.all()
    
    context = {
        'expenses': expenses,
        'budgets': budgets,
        'goals': goals,
    }
    return render(request, 'personal_finance/dashboard.html', context)

# View for adding a new expense
def add_expense(request):
    if request.method == 'POST':
        # Get data from the form
        category = request.POST['category']
        amount = request.POST['amount']
        date = request.POST['date']
        # Save to database
        Expense.objects.create(category=category, amount=amount, date=date)
        return redirect('dashboard')
    return render(request, 'personal_finance/add_expense.html')

# View for adding a new budget
def add_budget(request):
    if request.method == 'POST':
        # Get data from the form
        category = request.POST['category']
        limit = request.POST['limit']
        # Save to database
        Budget.objects.create(category=category, limit=limit)
        return redirect('dashboard')
    return render(request, 'personal_finance/add_budget.html')

# View for setting a financial goal
def add_goal(request):
    if request.method == 'POST':
        # Get data from the form
        goal_name = request.POST['goal_name']
        target_amount = request.POST['target_amount']
        # Save to database
        FinancialGoal.objects.create(goal_name=goal_name, target_amount=target_amount)
        return redirect('dashboard')
    return render(request, 'personal_finance/add_goal.html')

# View to delete an expense
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('dashboard')



# View to list all transactions (expenses)
def transaction_list(request):
    transactions = Expense.objects.all()
    
    context = {
        'transactions': transactions
    }
    
    return render(request, 'personal_finance/transaction_list.html', context)

# View to list all budgets
def budget_list(request):
    budgets = Budget.objects.all()
    
    context = {
        'budgets': budgets
    }
    
    return render(request, 'personal_finance/budget_list.html', context)

# View to add a new budget
def add_budget(request):
    if request.method == 'POST':
        category = request.POST['category']
        limit = request.POST['limit']
        Budget.objects.create(category=category, limit=limit)
        return redirect('budget_list')
    return render(request, 'personal_finance/add_budget.html')

# View to delete a budget
def delete_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    budget.delete()
    return redirect('budget_list')

# View to list all financial goals
def goal_list(request):
    goals = FinancialGoal.objects.all()
    
    context = {
        'goals': goals
    }
    
    return render(request, 'personal_finance/goal_list.html', context)

# View to add a new financial goal
def add_goal(request):
    if request.method == 'POST':
        goal_name = request.POST['goal_name']
        target_amount = request.POST['target_amount']
        FinancialGoal.objects.create(goal_name=goal_name, target_amount=target_amount)
        return redirect('goal_list')
    return render(request, 'personal_finance/add_goal.html')

# View to delete a financial goal
def delete_goal(request, goal_id):
    goal = FinancialGoal.objects.get(id=goal_id)
    goal.delete()
    return redirect('goal_list')

