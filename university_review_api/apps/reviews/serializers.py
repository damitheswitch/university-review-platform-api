from rest_framework import serializers
from apps.reviews.models import Review
from apps.users.serializers import UserSerializer
from apps.universities.serializers import UniversitySerializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'university', 'user', 'rating', 'review_text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    university = UniversitySerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'university', 'user', 'rating', 'review_text', 'created_at', 'updated_at']
