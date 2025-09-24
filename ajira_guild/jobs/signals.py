from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Application
from notifications.models import Notification

@receiver(post_save, sender=Application)
def notify_employer_on_application(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.job.employer,
            message=f"{instance.applicant.get_full_name()} applied for {instance.job.title}"
        )
