from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddJobForm, ApplicationForm
from .models import Job

from apps.notification.utilities import create_notification


def search(request):
    return render(request, 'job/search.html')


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    if request.user.is_authenticated:
        userprofile = request.user.userprofile
    else:
        userprofile = ''

    return render(request, 'job/job_detail.html', {'job': job, 'userprofile': userprofile})


@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    x = request.user.userprofile.is_profile_completed

    if request.user.userprofile.is_employer is False:

        if request.user.userprofile.is_profile_completed is True:

            if request.method == 'POST':
                form = ApplicationForm(request.POST)

                if form.is_valid():
                    application = form.save(commit=False)
                    application.job = job
                    application.created_by = request.user
                    application.save()

                    create_notification(request, job.created_by, 'application', extra_id=application.id)

                    return redirect('dashboard')

            else:
                form = ApplicationForm()
        
            return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})

        else:
            denied_message = "You can only apply to a job after you've completed your profile."
            return render(request, 'core/operation_denied.html', {'denied_message': denied_message})           

    else:
        denied_message = "Employers can't apply for jobs."
        return render(request, 'core/operation_denied.html', {'denied_message': denied_message})


@login_required
def add_job(request):
    if request.user.userprofile.is_employer is True:

        if request.method == 'POST':
            form = AddJobForm(request.POST)

            if form.is_valid():
                job = form.save(commit=False)
                job.created_by = request.user
                job.save()

                return redirect('dashboard')
        else:
            form = AddJobForm()
        
        return render(request, 'job/add_job.html', {'form': form})
    
    else:
        denied_message = "Job seekers can't add jobs."
        return render(request, 'core/operation_denied.html', {'denied_message': denied_message})


@login_required
def edit_job(request, job_id):
    if request.user.userprofile.is_employer is True:
        job = get_object_or_404(Job, pk=job_id, created_by=request.user)
        
        if request.method == 'POST':
                form = AddJobForm(request.POST, instance=job)

                if form.is_valid():
                    job = form.save(commit=False)
                    job.status = request.POST.get('status')
                    job.save()

                    return redirect('dashboard')
        else:
            form = AddJobForm(instance=job)
        
        return render(request, 'job/edit_job.html', {'form': form, 'job': job})

    else:
        denied_message = "Job seekers can't edit jobs."
        return render(request, 'core/operation_denied.html', {'denied_message': denied_message})
