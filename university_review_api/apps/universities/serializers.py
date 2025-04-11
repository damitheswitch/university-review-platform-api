from rest_framework import serializers
from university_review_api.apps.universities.models import University

class UniversitySerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    
    class Meta:
        model = University
        fields = ('id', 'name', 'country', 'website', 'average_rating')