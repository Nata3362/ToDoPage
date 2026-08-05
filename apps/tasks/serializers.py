from rest_framework import serializers
from .models import Category, Task, DailyCheckIn


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'category', 'title', 'time_block', 'date', 'is_done', 'created_at']
        read_only_fields = ['created_at']


class DailyCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCheckIn
        fields = ['id', 'date', 'note', 'energy']