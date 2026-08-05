from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#3B82F6')  # hex color, e.g. blue

    def __str__(self):
        return self.name


class Task(models.Model):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    EVENING = 'evening'
    TIME_BLOCK_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=200)
    time_block = models.CharField(max_length=10, choices=TIME_BLOCK_CHOICES, default=MORNING)
    date = models.DateField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time_block']

    def __str__(self):
        return f"{self.title} ({self.date})"


class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField()
    note = models.TextField(blank=True)
    energy = models.PositiveSmallIntegerField(null=True, blank=True)  # 1-5 scale

    class Meta:
        unique_together = ('user', 'date')  # one check-in per user per day

    def __str__(self):
        return f"Check-in {self.date}"