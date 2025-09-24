import csv
from django.http import HttpResponse

def export_jobs_csv(queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="jobs.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','Title','Employer','Category','Posted On'])
    for job in queryset:
        writer.writerow([job.id, job.title, job.employer.email, job.category.name if job.category else '', job.posted_on])
    return response
