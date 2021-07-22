from django import forms
from django.forms import fields
from django.forms.models import construct_instance
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'course_interest', 'description')
