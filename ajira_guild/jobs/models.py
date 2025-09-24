import uuid
from django.db import models
from django.conf import settings

class JobCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role':'employer'})
    title = models.CharField(max_length=200)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=120, blank=True)
    class Meta:
        ordering = ['-posted_on']
    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = (
        ('submitted','Submitted'),
        ('shortlisted','Shortlisted'),
        ('rejected','Rejected'),
        ('hired','Hired'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role':'jobseeker'})
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/%Y/%m/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    applied_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('job','applicant')
    def __str__(self):
        return f'{self.applicant} -> {self.job}'
