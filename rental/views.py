from django.shortcuts import render

# Create your views here.
# from .forms import RentalForm
from .models import Rental,RentalDetail

def home(request):
	obj = Rental.objects.all()
	return render(request, 'index.html', {'objs': obj})

def bymachine(request,machine):
	obj = RentalDetail.objects.filter(machine__name=machine)
	return render(request, 'machine.html', {'objs': obj,'name':machine})

def bycompany(request,company):
	obj = RentalDetail.objects.filter(rental__rent_from=company)
	return render(request, 'machine.html', {'objs': obj,'name':company})
