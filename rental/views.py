from django.shortcuts import render

# Create your views here.
# from .forms import RentalForm
from .models import Rental

def home(request):
	# obj = Rental.objects.all()
	obj = None
	return render(request, 'index.html', {'objs': obj})

def bymachine(request,machine):
	# obj = RentalDetail.objects.filter(machine__name=machine)
	obj = None
	return render(request, 'machine.html', {'objs': obj,'name':machine})

def bycompany(request,company):
	# obj = RentalDetail.objects.filter(rental__rent_from=company)
	obj = None
	return render(request, 'machine.html', {'objs': obj,'name':company})

def byrental(request,rental):
	# obj = Rental.objects.filter(name=rental)
	obj = None
	return render(request, 'index.html', {'objs': obj,'name':rental})
