from django.conf.urls import patterns, url, include


# sub patterns for muscles
from kettclub.exercises.views.exercises import ExerciseListView, view
from kettclub.exercises.views.muscle import MuscleListView, MuscleAdminListView, MuscleAddView, MuscleUpdateView, \
    MuscleDeleteView

patterns_muscle = [
    url(r'^overview/$',
        MuscleListView.as_view(),
        name='overview'),
    url(r'^admin-overview/$',
        MuscleAdminListView.as_view(),
        name='admin-list'),
    url(r'^add/$',
        MuscleAddView.as_view(),
        name='add'),
    url(r'^(?P<pk>\d+)/edit/$',
        MuscleUpdateView.as_view(),
        name='edit'),
    url(r'^(?P<pk>\d+)/delete/$',
        MuscleDeleteView.as_view(),
        name='delete'),
]

# sub patterns for exercises
patterns_exercise = [
    url(r'^overview/$',
        ExerciseListView.as_view(),
        name='overview'),
    url(r'^(?P<id>\d+)/view/$',
        view,
        name='view'),
    url(r'^(?P<id>\d+)/view/(?P<slug>[-\w]*)/?$',
        view,
        name='view'),
    # url(r'^add/$',
    #     login_required(ExerciseAddView.as_view()),
    #     name='add'),
    # url(r'^(?P<pk>\d+)/edit/$',
    #     ExerciseUpdateView.as_view(),
    #     name='edit'),
    # url(r'^(?P<pk>\d+)/correct$',
    #     ExerciseCorrectView.as_view(),
    #     name='correct'),
    # url(r'^(?P<pk>\d+)/delete/$',
    #     ExerciseDeleteView.as_view(),
    #     name='delete'),
    # url(r'^pending/$',
    #     PendingExerciseListView.as_view(),
    #     name='pending'),
    # url(r'^(?P<pk>\d+)/accept/$',
    #     accept,
    #     name='accept'),
    # url(r'^(?P<pk>\d+)/decline/$',
    #     decline,
    #     name='decline'),
]

urlpatterns = [
   url(r'^muscle/', include(patterns_muscle, namespace="muscle")),
   # url(r'^image/', include(patterns_images, namespace="image")),
   # url(r'^comment/', include(patterns_comment, namespace="comment")),
   # url(r'^category/', include(patterns_category, namespace="category")),
   # url(r'^equipment/', include(patterns_equipment, namespace="equipment")),
   url(r'^', include(patterns_exercise, namespace="exercise")),
]