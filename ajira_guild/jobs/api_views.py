from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
