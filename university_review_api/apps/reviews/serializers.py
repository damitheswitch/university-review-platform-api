from rest_framework import serializers
from university_review_api.apps.reviews.models import Review
from university_review_api.apps.users.serializers import UserProfileSerializer
from university_review_api.apps.universities.serializers import UniversitySerializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'university', 'user', 'rating', 'review_text', 'created_at', 'updated_at')
        read_only_fields = ('user', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        # Set the user to the current authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    university = UniversitySerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('id', 'university', 'user', 'rating', 'review_text', 'created_at', 'updated_at')