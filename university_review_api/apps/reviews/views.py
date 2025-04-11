from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from .permissions import IsAuthorOrReadOnly

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

class ReviewSearchView(generics.ListAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating', 'university__country']
    search_fields = ['university__name']
    ordering_fields = ['created_at', 'rating']
    
    def get_queryset(self):
        return Review.objects.all()