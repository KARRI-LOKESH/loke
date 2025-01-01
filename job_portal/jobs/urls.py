from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobPostListCreateView,
    JobPostDetailView,
    JobApplicationCreateView,
    JobApplicationListView,
    JobApplicationDetailView,
    JobPostSearchFilterView,
    JobPostViewSet,
    JobPostListView,
    JobApplicationView,
    post_job,
    job_list
)

# Create a router for the JobPostViewSet to handle CRUD operations
router = DefaultRouter()
router.register(r'posts', JobPostViewSet, basename='jobpost')

# Define URL patterns
urlpatterns = [
    # Job Posts
    path('posts/', JobPostListCreateView.as_view(), name='job_post_list_create'),
    path('posts/<int:pk>/', JobPostDetailView.as_view(), name='job_post_detail'),
    path('api/job-posts/', JobPostListView.as_view(), name='job_posts_list'),

    # Job Applications
    path('applications/', JobApplicationCreateView.as_view(), name='apply_job'),
    path('applications/employer/', JobApplicationListView.as_view(), name='view_applications'),
    path('applications/<int:pk>/', JobApplicationDetailView.as_view(), name='application_detail'),

    # Search for Job Posts
    path('search/', JobPostSearchFilterView.as_view(), name='job_post_search'),

    # Custom Views (Job Posting and Job Listing)
    path('post/', post_job, name='post_job'),
    path('list/', job_list, name='job_list'),

    # Job Post ViewSet
    path('api/jobs/', include(router.urls)),

    # Job Application API
    path('api/applications/', JobApplicationView.as_view(), name='job_application'),
]
