from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Custom User Model
class CustomUser(AbstractUser):
    is_job_seeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

# Job Seeker Profile
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='job_seeker_profile')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Employer Profile
class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

# Signal Handlers to create and save profiles automatically when a user is created or updated
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_job_seeker:
            JobSeekerProfile.objects.create(user=instance)
        elif instance.is_employer:
            EmployerProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_job_seeker:
        instance.job_seeker_profile.save()
    elif instance.is_employer:
        instance.employer_profile.save()
from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    # Add other relevant fields as necessary

    def __str__(self):
        return self.title
