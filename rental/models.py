from django.db import models
from django.core.exceptions import ValidationError

LCB1 = 'LCB1'
LCMT ='LCMT'
COMPANY_CHOICES = (
    (LCB1, 'LCB1'),
    (LCMT, 'LCMT'),
)
# Create your models here.
class Machine_type(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

class Machine(models.Model):
	USED = 'USED'
	REPAIR ='REPAIR'
	PM = 'PM'
	STATUS_CHOICES = (
        (USED, 'Using'),
        (REPAIR, 'Repairing'),
        (PM,'Preventive Maintenance')
    )
	name = models.CharField(max_length=50,primary_key=True)
	company = models.CharField(verbose_name ='Company Name',max_length=50,choices=COMPANY_CHOICES)
	model = models.CharField(verbose_name ='Model Name',max_length=50,blank=True, null=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	machine_type = models.ForeignKey('Machine_type',
		on_delete = models.CASCADE, related_name='machine_list')
	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=USED)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

class Vessel(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

class Purpose(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255,blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name


class Rental(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	machine = models.ManyToManyField(Machine,related_name="rentals")
	vessel = models.ForeignKey('Vessel',
		on_delete = models.CASCADE, related_name='rentals',blank=True, null=True,
		verbose_name ='For Vessel')
	# rent_from = models.CharField(verbose_name ='Rent from',max_length=10 ,choices=COMPANY_CHOICES)
	requested_by = models.CharField(verbose_name ='Requested By',max_length=10 ,choices=COMPANY_CHOICES,blank=True, null=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	start_date = models.DateTimeField(blank=True, null=True)
	stop_date  = models.DateTimeField(blank=True, null=True)
	purpose = models.ForeignKey('Purpose',
		on_delete = models.CASCADE, related_name='rentals',blank=True, null=True,verbose_name ='Rent purpose')
	created_date = models.DateTimeField(verbose_name ='Issued Date',auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True)
	approved = models.BooleanField(default=False)
	approved_date = models.DateTimeField(blank=True, null=True)
	approved_by = models.ForeignKey('auth.User',related_name="approves",blank=True,null=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

	def total_machine(self):
		return self.machine.all().count()

	class Meta:
		ordering = ['-created_date']

# class RentalDetail(models.Model):
# 	machine = models.ManyToManyField(Machine,related_name="machines") #models.ForeignKey('Machine', related_name='rentals')
# 	rental = models.ForeignKey('Rental',
# 		on_delete = models.CASCADE, related_name='items')
# 	description = models.CharField(max_length=255,blank=True, null=True)
# 	start_date = models.DateTimeField(blank=True, null=True)
# 	stop_date  = models.DateTimeField(blank=True, null=True)
# 	created_date = models.DateTimeField(auto_now_add=True)
# 	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
# 	user = models.ForeignKey('auth.User',blank=True,null=True)

# 	def __str__(self):
# 		return self.rental.name

# 	def total_hour(self):
# 		return self.stop_date - self.start_date

# 	def clean(self):
# 		if self.stop_date <= self.start_date :
# 			raise ValidationError('Invalid rental date : Stop date must be after Start date')
	
# 	class Meta:
# 		ordering = ['-created_date']

# class Purpose(models.Model):
# 	name = models.CharField(max_length=50)
# 	description = models.CharField(max_length=255,blank=True, null=True)
# 	created_date = models.DateTimeField(auto_now_add=True)
# 	modified_date = models.DateTimeField(blank=True, null=True)
# 	user = models.ForeignKey('auth.User',blank=True,null=True)

# 	def __str__(self):
# 		return self.name

		# if self.imp_release_date != None :
		# 	if self.imp_release_date <= self.etb :
		# 		raise ValidationError('Import Release Date must be after ETB')

		# if self.export_cutoff_date != None :
		# 	if self.export_cutoff_date >= self.etb :
		# 		raise ValidationError('Export Cutoff Date must be before ETB')




# class Ticket(models.Model):
# 	P = 'PENDING'
# 	A = 'ACK'
# 	W = 'WORKING'
# 	C ='CLOSED'
# 	STATUS_CHOICES = (
#         (P, 'Pending'),
#         (A, 'Acknowledge'),
#         (W, 'Working'),
#         (C, 'Closed'),
#     )
# 	machine = models.ForeignKey('Machine', related_name='tickets')
# 	symptom =  models.CharField(max_length=255)
# 	description = models.TextField(max_length=255,blank=True, null=True)
# 	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=P)
# 	created_date = models.DateTimeField(auto_now_add=True)
# 	ack_date = models.DateTimeField(blank=True, null=True)
# 	target_date = models.DateTimeField(blank=True, null=True)
# 	finished_date = models.DateTimeField(blank=True, null=True)
# 	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
# 	user = models.ForeignKey('auth.User',blank=True,null=True)

# 	def __str__(self):
# 		return ('%s -- %s' % (self.machine,self.symptom))


# class Log(models.Model):
# 	C = 'CREATE'
# 	A = 'ACK'
# 	S = 'START'
# 	F = 'FINISH'
# 	P = 'POSTPONE'
# 	N = 'NOTE'
# 	LOG_CHOICES = (
#         (C, 'Create'),
#         (A,'Acknowledge'),
#         (S,'Start'),
#         (F, 'Finish'),
#         (P, 'Postpone'),
#         (N,'Notice'),
#     )
# 	ticket = models.ForeignKey('Ticket', related_name='logs')
# 	log_type = models.CharField(max_length=10 ,choices=LOG_CHOICES,default=N)
# 	comment = models.TextField(blank=True, null=True)
# 	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
# 	user = models.ForeignKey('auth.User',blank=True,null=True)

# class Pm(models.Model):
# 	P = 'PENDING'
# 	C ='CLOSED'
# 	STATUS_CHOICES = (
#         (P, 'Pending'),
#         (C, 'Closed'),
#     )
# 	machine = models.ForeignKey('Machine', related_name='pms')
# 	description = models.TextField(blank=True, null=True)
# 	planed_date = models.DateTimeField(blank=True, null=True)
# 	finished_date = models.DateTimeField(blank=True, null=True)
# 	created_date = models.DateTimeField(auto_now_add=True)
# 	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=P)
# 	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
# 	user = models.ForeignKey('auth.User',blank=True,null=True)



