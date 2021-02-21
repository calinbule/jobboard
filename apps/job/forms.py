from django import forms
from ckeditor.fields import RichTextField
from .models import Job, Application
from django.db import models


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'short_description', 'long_description', 'company_name', 'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'experience']