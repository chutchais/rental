from django.db.models import Q

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

# from .serialize import VoySerializer,VoyDetailSerializer
# from berth.models import Voy

from rental.models import Rental
from .serialize import (RentalSerializer,
						RentalDetailSerializer,
						RentalCreateUpdateSerializer)



class RentalListAPIView(ListAPIView):
	queryset= Rental.objects.all()
	serializer_class=RentalSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields =['name']
	def get_queryset(self,*args,**kwargs):
		queryset_list = None#Rental.objects.all()
		f = self.request.GET.get("f")
		t = self.request.GET.get("t")
		q = self.request.GET.get("q")

		if f != None and t != None :
			print('Query date')
			queryset_list = Rental.objects.filter(
					Q(start_date__range = [f,t]))
		if q != None :
			queryset_list = Rental.objects.filter(
					Q(name__icontains = q)|
					Q(machine__name__icontains = q))

		return queryset_list
	# pagination_class = PostPageNumberPagination

class RentalDetailAPIView(RetrieveAPIView):
	queryset= Rental.objects.all()
	serializer_class=RentalDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class RentalDeleteAPIView(DestroyAPIView):
	queryset= Rental.objects.all()
	serializer_class= RentalDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class ShipperCreateAPIView(CreateAPIView):
	queryset=Rental.objects.all()
	serializer_class=RentalCreateUpdateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()


