from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Q
from .models import Job
from .forms import ApplicationForm

def job_list(request):
    qs = Job.objects.filter(is_active=True)
    q = request.GET.get('q')
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q))
    return render(request, 'jobs/job_list.html', {'jobs': qs})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if not request.user.is_authenticated or not request.user.is_jobseeker():
        messages.error(request, "Only jobseekers can apply.")
        return redirect('accounts:login')
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.save()
            messages.success(request, "Application submitted.")
            # Notification.objects.create(user=job.employer, message=f"{request.user} applied to {job.title}")
            return redirect('jobs:detail', job_id=job_id)
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply.html', {'form':form, 'job':job})
