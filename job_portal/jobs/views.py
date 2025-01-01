from rest_framework import generics, permissions, filters, viewsets
from .models import JobPost, JobApplication, EmployerProfile
from .serializers import JobPostSerializer, JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Job Post Views
class JobPostListCreateView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user.employer_profile)

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Job Application Views
class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user.job_seeker_profile)

class JobPostSearchFilterView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location', 'job_type']
    ordering_fields = ['created_at', 'salary']

class JobApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(job_post__employer=self.request.user.employer_profile)

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

# Function-based Views (for traditional HTML views)
def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.employer = request.user
            job_post.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def job_list(request):
    jobs = JobPost.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# JobPost ViewSet
class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employer_profile = get_object_or_404(EmployerProfile, user=self.request.user)
        serializer.save(employer=employer_profile)

# JobPost List API View
class JobPostListView(APIView):
    def get(self, request):
        job_posts = JobPost.objects.all()
        serializer = JobPostSerializer(job_posts, many=True)
        return Response(serializer.data)

class JobApplicationView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Application submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
