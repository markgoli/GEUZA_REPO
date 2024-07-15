from django import forms
from django.contrib import admin
from django.forms import ModelForm
from .models import Event
#from mapbox_location_field.widgets import MapInput
#from bootstrap_datepicker_plus import DateTimePickerInput

class EventAdminForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            #'location': MapInput(),
        }

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

from .models import DonationCause

class DonationCauseForm(forms.ModelForm):
    class Meta:
        model = DonationCause
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
        fields = '__all__'


# forms.py

from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    email = forms.EmailField(label='Your Email', required=True)
    phone = forms.CharField(label='Phone', max_length=15, required=False)
    subject = forms.CharField(label="I'm interested in", max_length=100, required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=False)
