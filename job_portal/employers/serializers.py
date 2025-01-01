from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['id', 'name', 'email', 'phone_number', 'company_name', 'address', 'created_at', 'updated_at']

