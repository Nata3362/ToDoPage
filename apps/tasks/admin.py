from django.contrib import admin
from .models import Category, Task, DailyCheckIn

# Models
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(DailyCheckIn)
