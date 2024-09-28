from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Borrower, Loan, Investor

# View for the homepage
def dashboard(request):
    loans = Loan.objects.all()
    investors = Investor.objects.all()
    
    context = {
        'loans': loans,
        'investors': investors,
    }
    return render(request, 'peer_to_peer_lending/dashboard.html', context)

# View for creating a loan listing
def create_loan(request):
    if request.method == 'POST':
        borrower_name = request.POST['borrower_name']
        loan_amount = request.POST['loan_amount']
        interest_rate = request.POST['interest_rate']
        duration = request.POST['duration']
        # Save loan listing
        Loan.objects.create(borrower_name=borrower_name, loan_amount=loan_amount, interest_rate=interest_rate, duration=duration)
        return redirect('platform_dashboard')
    return render(request, 'peer_lending/create_loan.html')

# View for verifying a borrower
def verify_borrower(request, borrower_id):
    borrower = Borrower.objects.get(id=borrower_id)
    borrower.verified = True
    borrower.save()
    return redirect('platform_dashboard')

# View for managing investor portfolio
def investor_portfolio(request, investor_id):
    investor = Investor.objects.get(id=investor_id)
    portfolio = investor.portfolio_set.all()
    
    context = {
        'investor': investor,
        'portfolio': portfolio,
    }
    return render(request, 'peer_lending/investor_portfolio.html', context)

# View for automating loan repayment
def process_repayment(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    # Logic to process repayment
    loan.repaid = True
    loan.save()
    return redirect('platform_dashboard')



def investor_list(request):
    investors = Investor.objects.all()  # Fetch all investors from the database
    context = {
        'investors': investors,
    }
    return render(request, 'peer_to_peer_lending/investor_list.html', context)


def loan_list(request):
    loans = Loan.objects.all()  # Fetch all loans from the database
    context = {
        'loans': loans,
    }
    return render(request, 'peer_to_peer_lending/loan_list.html', context)


def add_loan(request):
    if request.method == 'POST':
        # Retrieve data from the form
        borrower = request.POST['borrower']
        amount = request.POST['amount']
        interest_rate = request.POST['interest_rate']
        term = request.POST['term']

        # Save the new loan to the database
        Loan.objects.create(borrower=borrower, amount=amount, interest_rate=interest_rate, term=term)
        return redirect('loan_list')

    return render(request, 'peer_to_peer_lending/create_loan.html')

def add_investor(request):
    if request.method == 'POST':
        # Get data from the form
        investor_name = request.POST['investor_name']
        investment_amount = request.POST['investment_amount']
        
        # Save to database
        Investor.objects.create(
            investor_name=investor_name,
            investment_amount=investment_amount
        )
        return redirect('investor_list')  # Redirect to the investor list after adding

    return render(request, 'peer_to_peer_lending/add_investor.html')