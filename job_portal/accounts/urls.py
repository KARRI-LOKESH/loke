from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # User Registration (Create New User)
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # User Profile (For Job Seekers and Employers)
    path('profile/', views.profile, name='profile'),
    
    # Job Seeker Profile View
    path('job-seeker/profile/', views.JobSeekerProfileView.as_view(), name='job_seeker_profile'),
    
    # Employer Profile View
    path('employer/profile/', views.EmployerProfileView.as_view(), name='employer_profile'),
    
    # Job Seeker Profile Update View
    path('job-seeker/profile/update/', views.JobSeekerProfileUpdateView.as_view(), name='job_seeker_profile_update'),
    
    # Employer Profile Update View
    path('employer/profile/update/', views.EmployerProfileUpdateView.as_view(), name='employer_profile_update'),
    
    # Job Post List and Create View
    path('jobs/', views.JobPostListCreateView.as_view(), name='job_list_create'),
    
    # Job Post Detail View
    path('jobs/<int:pk>/', views.JobPostDetailView.as_view(), name='job_post_detail'),
]
