from django.shortcuts import render
from .models import Registration, Investment, Member

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    pending_approval = Registration.objects.all()
    members = Member.objects.all()
    context = {"person": pending_approval, "members": members}
    return render(request, 'pending_report.html', context)

def investments(request):
    invest = Investment.objects.all()
    context = {"invest": invest}
    return render(request, "investments.html", context)
