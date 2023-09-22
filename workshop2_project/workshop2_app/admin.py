from django.contrib import admin
from .models import ABACStudent, MSMEStudent
from .models import Movie

admin.site.register(ABACStudent)
admin.site.register(MSMEStudent)
admin.site.register(Movie)