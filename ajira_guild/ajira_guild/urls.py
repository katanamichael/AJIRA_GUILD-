from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jobs.api_views import JobViewSet

router = routers.DefaultRouter()
router.register('api/jobs', JobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('notifications/', include('notifications.urls')),
    path('training/', include('training.urls')),
    path('', include('core.urls')),
]
urlpatterns += router.urls
