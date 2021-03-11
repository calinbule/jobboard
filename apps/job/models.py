from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField 

class Job(models.Model):


    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EMPLOYED, 'Employed'),
        (ARCHIVED, 'Archived')
    )

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100, null=True, blank=True) 
    long_description = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    cover_letter = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)