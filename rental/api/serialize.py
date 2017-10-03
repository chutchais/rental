from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField,
	RelatedField,
	ReadOnlyField
	)


from rental.models import Rental

rental_detail_url=HyperlinkedIdentityField(
		view_name='rental-api:detail',
		lookup_field='slug'
		)


class RentalCreateUpdateSerializer (ModelSerializer):
	class Meta:
		model = Rental
		fields =[
			'name',
			'machine',
			'vessel'
		]


class RentalSerializer(ModelSerializer):
	# url = rental_detail_url
	# vessel = BookingVesselSerializer()
	# shipper = BookingShipperSerializer()
	# purpose = StringRelatedField(many=True)
	# 'ReadOnlyField' RelatedField
	purpose_name = ReadOnlyField()

	class Meta:
		model = Rental
		# fields ='__all__'
		fields = [
			'name',
			'requested_by',
			'purpose_name',
			'purpose',
			'description',
			'total_machine',
			'machine',
			'vessel',
			'description',
			'start_date',
			'stop_date',
			'total_time'
			]
		# extra_kwargs = {'url': {'view_name': 'rental-api:detail'}}


class RentalDetailSerializer(ModelSerializer):
	class Meta:
		model = Rental
		fields =['name']




