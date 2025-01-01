from rest_framework import serializers
from .models import CustomUser, JobSeekerProfile, EmployerProfile
from .models import JobPost

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = JobSeekerProfile
        fields = ['user', 'resume', 'skills']

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = EmployerProfile
        fields = ['user', 'company_name', 'company_website', 'location']

class JobSeekerProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ['resume', 'skills']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = JobSeekerProfile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        instance.resume = validated_data.get('resume', instance.resume)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.save()
        return instance

class EmployerProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_website', 'location']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = EmployerProfile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_website = validated_data.get('company_website', instance.company_website)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'