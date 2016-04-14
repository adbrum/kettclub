from django import forms

from kettclub.exercises.models import ExerciseImage, ExerciseComment


class ExerciseImageForm(forms.ModelForm):
    class Meta:
        model = ExerciseImage
        fields = ('image',
                  'is_main',
                  'license',
                  'license_author')


class CommentForm(forms.ModelForm):
    class Meta:
        model = ExerciseComment
        exclude = ('exercise',)
