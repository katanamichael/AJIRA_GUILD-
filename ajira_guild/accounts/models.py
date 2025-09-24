import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLES = (
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='jobseeker')
    phone = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)

    def is_jobseeker(self): return self.role == 'jobseeker'
    def is_employer(self): return self.role == 'employer'
