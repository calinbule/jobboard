from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.job.models import Job, Application
from .models import ConversationMessage, Userprofile
from apps.notification.utilities import create_notification
from .forms import EditProfileForm


@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})


@login_required
def profile(request):
    return render(request, 'userprofile/profile.html', {'userprofile': request.user.userprofile})


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by = request.user)

            if request.user.userprofile.is_employer:
                create_notification(request, application.created_by, 'message', extra_id=application.id)
            else:
                create_notification(request, application.job.created_by, 'message', extra_id=application.id)

            return  redirect('view_application', application_id=application_id)

    return render(request, 'userprofile/view_application.html', {'application': application})


@login_required
def view_dashboard_job(request, job_id):
    if request.user.userprofile.is_employer is True:
        job = get_object_or_404(Job, pk=job_id, created_by=request.user)

        return render(request, 'userprofile/view_dashboard_job.html', {'job': job})

    else:
        denied_message = "This area is reserved to jobseekers only."
        return render(request, 'job/operation_denied.html', {'denied_message': denied_message})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Userprofile, user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_profile_completed = True
            profile.save()

            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    
    return render(request, 'userprofile/edit_profile.html', {'form': form, 'profile': profile})
