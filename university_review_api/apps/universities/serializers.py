from rest_framework import serializers
from apps.universities.models import University

class UniversitySerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    
    class Meta:
        model = University
        fields = ['id', 'name', 'country', 'website', 'average_rating']
