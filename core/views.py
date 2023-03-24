from django.shortcuts import render, redirect, get_object_or_404
from urllib3 import HTTPResponse
from .models import Registration, Investment, Member, Transaction, Leaver
from .forms import Register, Login, Leaver
from calendar import monthrange
from datetime import date, timedelta
from django_daraja.mpesa.core import MpesaClient
import math

def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            member_no = form.cleaned_data['member_number']
            password = form.cleaned_data['password']
            member = Member.objects.get(member_number=member_no)

            if password == member.member_password:
                return redirect('member/'+ member_no)

    form = Login()
    context = {'form': form}
    return render(request, 'index.html', context)

def register(request):
    pending_approval = Registration.objects.all()
    members = Member.objects.all()
    context = {"person": pending_approval, "members": members}
    return render(request, 'pending_report.html', context)

def investments(request):
    invest = Investment.objects.all()
    context = {"invest": invest}
    return render(request, "investments.html", context)

def reg_success(request):
    return render(request, 'reg-success.html')


def member(request, member_number):
    member = get_object_or_404(Member, member_number=member_number)
    contributions = Transaction.objects.filter(transaction_type='CTB')
    my_contribs = Transaction.objects.filter(member=member,transaction_type='CTB')
    repayments = Transaction.objects.filter(transaction_type='RPT')
    investments = Investment.objects.all()

    arrears = 1000
    months_spent = monthdelta(member.joined_on, date.today())
    i = months_spent
    while i > 0:
        if months_spent < 3:
            arrears += 500
        else:
            arrears += 1000
        i -= 1

    def calculate(iterable):
        total = 0
        for contribution in iterable:
            total = contribution.amount + total
        return total
    
    total_made = 0
    for investment in investments:
        m =  monthdelta(investment.principal.date, date.today())
        total_made = investment.principal.amount + investment.principal.amount * investment.investment_rate * m

    total = calculate(contributions)
    mine = calculate(my_contribs)
    if repayments:
        repayments = calculate(repayments)
    else:
        repayments = 0 
    arrears -= mine

    if arrears < 0:
        arrears = f"0 | {arrears*-1} overpaid"

    revenue = total + total_made - repayments
    shares = math.floor((mine/total) * revenue)

    context = {"member": member, "contrib": total, "returns": total_made, "mine": mine, "arrears": arrears, "revenue": revenue, "shares":shares}
    return render(request, "member_dash.html", context)


def leaving(request):
    if request.method == 'POST':
        form = Leaver(request.POST)
        if form.is_valid():
            member_no = form.cleaned_data['member_number']
            password = form.cleaned_data['password']
            member = Member.objects.get(member_number=member_no)

            if password == member.member_password:
                return redirect('leaver/'+ member_no)
            else:
                return HTTPResponse('INVALID PASSWORD -- cannot be allowed to leave at this time')

    form = Leaver()
    context = {'form': form}
    return render(request, 'index.html', context)

"""
def transaction(request):
    cl = MpesaClient()
    phone_number = '0700111222'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HTTPResponse(response)
"""
