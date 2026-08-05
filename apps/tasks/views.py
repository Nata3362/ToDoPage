# Create your views here.
from rest_framework import viewsets, permissions
from .models import Category, Task, DailyCheckIn
from .serializers import CategorySerializer, TaskSerializer, DailyCheckInSerializer
from django.shortcuts import render

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        date = self.request.query_params.get('date')
        if date:
            queryset = queryset.filter(date=date)
        if start and end:
            queryset = queryset.filter(date__gte=start, date__lte=end)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DailyCheckInViewSet(viewsets.ModelViewSet):
    serializer_class = DailyCheckInSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DailyCheckIn.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def today_view(request):
    return render(request, 'tasks/today.html')