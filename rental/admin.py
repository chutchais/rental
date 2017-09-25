from django.contrib import admin

# Register your models here.
from .models import Machine
from .models import Machine_type
from .models import Rental,Purpose,Vessel

from datetime import datetime


class MachineTypeAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_filter = ['name']
    list_display = ('name','description')
    fieldsets = [
        (None,               {'fields': ['name','description','user']}),
    ]
admin.site.register(Machine_type,MachineTypeAdmin)


# class MachineTicketInline(admin.TabularInline):
#     model = Ticket
#     extra = 1

# class MachinePmInline(admin.TabularInline):
#     model = Pm
#     extra = 1

class MachineAdmin(admin.ModelAdmin):
    search_fields = ['name','model','description']
    list_filter = ['company','machine_type','status']
    list_display = ('name','company','machine_type','model','description','status')
    fieldsets = [
        (None,               {'fields': ['name','company','machine_type','model','description','status','user']}),
    ]
    # inlines = [MachinePmInline,MachineTicketInline]

admin.site.register(Machine,MachineAdmin)


# class RentalDetailline(admin.TabularInline):
#     model = RentalDetail
#     extra = 1
#     readonly_fields = ('total_hour',)

#     def total_hour(self,obj):
#         fmt = '%Y-%m-%d %H:%M:%S'
#         # d1 = datetime.strptime(obj.stop_date, fmt)
#         # d2 = datetime.strptime(obj.start_date, fmt)
#         if obj.stop_date:
#             elapsed = obj.stop_date - obj.start_date
#             return elapsed
#         else:
#             return ''
#         # return  type(obj.stop_date)#(obj.stop_date - obj.start_date)

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     field = super(RentalDetailline, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #     if db_field.name == 'machine':
    #         # print (request._obj_.rent_from)
    #          # field.queryset = field.queryset.filter(company__exact = 'LCMT')  
    #         if request._obj_ is not None:
    #             field.queryset = field.queryset.filter(company__exact = request._obj_.rent_from)  
    #         else:
    #             field.queryset = field.queryset.none()
    #     return field

class PurposeAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_filter = ['name','description']
    list_display = ('name','description','created_date')
    fieldsets = [
        (None,               {'fields': ['name','description']}),
    ]
admin.site.register(Purpose,PurposeAdmin)

class VesselAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_filter = ['name','description']
    list_display = ('name','description','created_date')
    fieldsets = [
        (None,               {'fields': ['name','description']}),
    ]
admin.site.register(Vessel,VesselAdmin)

class RentalAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_filter = ['requested_by','purpose','approved','created_date']
    list_display = ('name','requested_by','purpose','description','total_machine','created_date','approved')
    fieldsets = [
        ('General Information',               {'fields': ['name',('description'),'user','created_date']}),
        ('Rental Details',               {'fields': ['requested_by','purpose','vessel','start_date','stop_date']}),
        ('Machine Details',               {'fields': ['machine',]}),
        ('Approval Details',               {'fields': ['approved','approved_date','approved_by']}),
    ]
    # inlines = [RentalDetailline]
    filter_horizontal = ('machine',)
    readonly_fields =['user','created_date']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(RentalAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        print ('Hook formfield')
        if db_field.name == 'machine':
            # print (request._obj_.rent_from)
            if request._obj_:
                # field.queryset = field.queryset.filter(company__exact = request._obj_.requested_by)  
                field.queryset = field.queryset.all().exclude(company__exact = request._obj_.requested_by)
            # kwargs["queryset"] = Machine.objects.filter(company__exact = request._obj_.rent_from)
            # if request._obj_ is not None:
            #     print(request._obj_)
            #     # field.queryset = field.queryset.filter(company__exact = request._obj_.rent_from)  
            # else:
            #     field.queryset = field.queryset.none()
        return field

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        import datetime
        form = super(RentalAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['name'].initial = 'Rental-' + datetime.datetime.today().strftime("%Y-%m-%d")
        # request._obj_ = obj
        return form #super(RentalAdmin, self).get_form(request, obj, **kwargs)
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(MyModelAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['my_field_name'].initial = 'abcd'
    #     return form
    def save_model(self, request, obj, form, change):
        # if not obj.author.id:
        #     obj.author = request.user
        print ('Hook Save Model')
        obj.user = request.user
        obj.save()

admin.site.register(Rental,RentalAdmin)


# class RentalDetailAdmin(admin.ModelAdmin):
#     search_fields = ['description']
#     list_filter = ['start_date','stop_date']
#     list_display = ('rental','description','start_date','stop_date')
#     filter_horizontal = ('machine',)
#     fieldsets = [
#         (None,  {'fields': ['machine','description','start_date','stop_date','user']}),
#     ]
#     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
#         field = super(RentalDetailAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
#         print ('Hook formfield')
#         if db_field.name == 'machine':
#             # print (self.machine)
#              # field.queryset = field.queryset.filter(company__exact = 'LCMT')  
#              kwargs["queryset"] = Machine.objects.filter(company__exact = 'LCMT')
#             # if request._obj_ is not None:
#             #     print(request._obj_)
#             #     # field.queryset = field.queryset.filter(company__exact = request._obj_.rent_from)  
#             # else:
#             #     field.queryset = field.queryset.none()
#         return field
# admin.site.register(RentalDetail,RentalDetailAdmin)

# class TicketLogline(admin.TabularInline):
#     model = Log
#     extra = 1

# class TicketAdmin(admin.ModelAdmin):
#     search_fields = ['machine__name','symptom','description']
#     list_filter = ['status','machine__machine_type','machine__name']
#     list_display = ('machine','symptom','created_date','ack_date','target_date','status')
#     fieldsets = [
#         (None,               {'fields': ['machine','symptom','description','status','ack_date','target_date','finished_date']}),
#     ]
#     inlines = [TicketLogline]
    
# admin.site.register(Ticket,TicketAdmin)

# class LogAdmin(admin.ModelAdmin):
#     search_fields = ['comment']
#     list_filter = ['ticket__machine__machine_type','log_type','ticket__machine__name']
#     list_display = ('ticket','log_type','comment','modified_date','user')
#     fieldsets = [
#         (None,               {'fields': ['ticket','log_type','comment','user']}),
#     ]
# admin.site.register(Log,LogAdmin)


# class PmAdmin(admin.ModelAdmin):
#     search_fields = ['machine','description']
#     list_filter = ['status','machine__machine_type','machine__name']
#     list_display = ('machine','description','planed_date','finished_date','status')
#     fieldsets = [
#         (None,               {'fields': ['machine','description','planed_date','finished_date','status','user']}),
#     ]
# admin.site.register(Pm,PmAdmin)