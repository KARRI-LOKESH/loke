from rest_framework import generics
from .models import JobPost
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser, JobSeekerProfile, EmployerProfile
from .serializers import (
    CustomUserSerializer,
    JobSeekerProfileSerializer,
    EmployerProfileSerializer,
    JobSeekerProfileCreateUpdateSerializer,
    EmployerProfileCreateUpdateSerializer,
)
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobPost
from .serializers import JobPostSerializer

# Register New User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

# Job Seeker Profile View
class JobSeekerProfileView(generics.RetrieveUpdateAPIView):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.job_seeker_profile

# Employer Profile View
class EmployerProfileView(generics.RetrieveUpdateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.employer_profile

# Job Seeker Profile Update View
class JobSeekerProfileUpdateView(generics.UpdateAPIView):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.job_seeker_profile

# Employer Profile Update View
class EmployerProfileUpdateView(generics.UpdateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.employer_profile

# Register view with form for traditional login
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_job_seeker:
                JobSeekerProfile.objects.create(user=user)
            elif user.is_employer:
                EmployerProfile.objects.create(user=user)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User profile view (for either job seeker or employer)
def profile(request):
    try:
        if request.user.is_job_seeker:
            profile = JobSeekerProfile.objects.get(user=request.user)
        elif request.user.is_employer:
            profile = EmployerProfile.objects.get(user=request.user)
    except (JobSeekerProfile.DoesNotExist, EmployerProfile.DoesNotExist):
        profile = None
    return render(request, 'accounts/profile.html', {'profile': profile})

# Job Post List/Create View
class JobPostListCreateView(APIView):
    def get(self, request):
        job_posts = JobPost.objects.all()
        serializer = JobPostSerializer(job_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Job Post Detail View
class JobPostDetailView(APIView):
    def get(self, request, pk):
        try:
            job_post = JobPost.objects.get(pk=pk)
            serializer = JobPostSerializer(job_post)
            return Response(serializer.data)
        except JobPost.DoesNotExist:
            return Response({"error": "Job post not found"}, status=404)
