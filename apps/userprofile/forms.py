from django import forms
from ckeditor.fields import RichTextField
from .models import Userprofile
from django.db import models

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            'name',
            'address_street',
            'address_zipcode',
            'address_city',
            'address_country',
            'email',
            'phone',
            'company_size',
            'company_description',
            'company_fiscal_code',
            'person_last_name',
            'person_drivers_license',
            'person_available_for_remote',
            'person_available_for_relocation',
            'person_available_for_parttime',
            'person_available_for_businesstravel',
            'person_sex',
        ]