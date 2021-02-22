from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

from apps.job.models import Application

class Userprofile(models.Model):
    SIZE_1_9 = 'size_1-9'
    SIZE_10_49 = 'size_10-49'
    SIZE_50_99 = 'size_50-99'
    SIZE_100 = 'size_100'

    CHOICES_SIZE = (
        (SIZE_1_9, '1-9'),
        (SIZE_10_49, '10-49'),
        (SIZE_50_99, '50-99'),
        (SIZE_100, '100+'),
    )

    MALE = 'M'
    FEMALE = 'F'

    CHOICES_SEX = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    # Common fields
    name = models.CharField(max_length=255, blank=True, null=True)
    address_street = models.CharField(max_length=255, blank=True, null=True)
    address_zipcode = models.CharField(max_length=255, blank=True, null=True)
    address_city = models.CharField(max_length=255, blank=True, null=True)
    address_country = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length = 254, blank=True, null=True)    
    phone = models.CharField(max_length=50, blank=True, null=True)
    
    # Company specific fields
    company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_9)
    company_description = RichTextField(blank=True, null=True)
    company_fiscal_code = models.CharField(max_length=50, blank=True, null=True)

    # Individual person specific fields
    person_last_name = models.CharField(max_length=255, blank=True, null=True)
    person_drivers_license = models.BooleanField(default=False)
    person_available_for_remote = models.BooleanField(default=False)
    person_available_for_relocation = models.BooleanField(default=False)
    person_available_for_parttime = models.BooleanField(default=False)
    person_available_for_businesstravel = models.BooleanField(default=False)
    person_sex = models.CharField(max_length=1, choices=CHOICES_SEX, default=MALE)

    # Userprofile specific fields   
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']