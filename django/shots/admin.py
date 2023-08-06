from django.contrib import admin

from .models import Shot
from .models import Task

admin.site.register(Shot)
admin.site.register(Task)