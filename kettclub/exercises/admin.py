from django.contrib import admin
from kettclub.exercises.models import Exercise, ExerciseCategory, Muscle, Equipment

admin.site.register(ExerciseCategory)
admin.site.register(Exercise)
admin.site.register(Muscle)
admin.site.register(Equipment)
