import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    jobslist = []
    data = json.loads(request.body)
    query = data['query']
    company_size = data['company_size']

    jobs = Job.objects\
        .filter(status=Job.ACTIVE)\
        .filter(
            Q(title__icontains=query) | \
            Q(short_description__icontains=query) | \
            Q(long_description__icontains=query) | \
            Q(created_by__userprofile__name__icontains=query) | \
            Q(created_by__userprofile__address_city__icontains=query)
        )

    if company_size:
        jobs = jobs.filter(created_by_company_size=company_size)
    
    for job in jobs:
        obj = {
            'id': job.id,
            'title': job.title,
            'company_name': job.created_by.userprofile.name,
            'url': '/jobs/%s/' % job.id
        }
        jobslist.append(obj)
    
    return JsonResponse({'jobs': jobslist})