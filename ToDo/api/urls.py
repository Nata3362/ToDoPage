from django.urls import include, path

urlpatterns = [
    path('', include('apps.tasks.urls')),
]
