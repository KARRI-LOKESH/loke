from django.db import models
from accounts.models import JobSeekerProfile, EmployerProfile

class JobPost(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(
        max_length=50,
        choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')],
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default="Uncategorized")
    experience_level = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='applications/resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending',
    )

    def __str__(self):
        return f"{self.applicant.user.username} - {self.job_post.title}"
