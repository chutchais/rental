from django import forms
import datetime
# from django.forms.widgets import  MultiWidget , to_current_timezone, DateTimeInput
# from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.admin import widgets
from .models import Rental


class RentalForm(forms.Form):
    name = forms.CharField()
    # rent_date = forms.DateTimeField(initial=datetime.date.today,input_formats=["%d %b %Y %H:%M:%S %Z"])
    # xx = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    holiday_date = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))


# class XForm(forms.ModelForm):
#     class Meta:
#         model = Rental
#         fields = ('name','modified_date')

#     def __init__(self, *args, **kwargs):
#         super(XForm, self).__init__(*args, **kwargs)
#         self.fields['modified_date'].widget = widgets.AdminDateWidget()
#         # self.fields['start_time'].widget = widgets.AdminTimeWidget()
#         # self.fields['end_time'].widget = widgets.AdminTimeWidget()