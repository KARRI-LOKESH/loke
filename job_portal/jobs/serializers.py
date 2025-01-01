from rest_framework import serializers
from .models import JobPost, JobApplication
from accounts.models import JobSeekerProfile, EmployerProfile

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
        read_only_fields = ['employer', 'created_at']

class JobApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(slug_field='user__username', read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'

    def validate(self, data):
        job_post = data.get('job_post')
        applicant = data.get('applicant')
        if JobApplication.objects.filter(job_post=job_post, applicant=applicant).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return data
