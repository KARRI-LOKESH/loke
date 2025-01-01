# employers/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet,EmployerListView

router = DefaultRouter()
router.register(r'employers', EmployerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employers/', EmployerListView.as_view(), name='employer-list'),
]
