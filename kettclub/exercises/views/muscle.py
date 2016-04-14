from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from kettclub.exercises.models import Muscle


class MuscleListView(ListView):
    '''
        Overview of all muscles and their exercises
    '''
    model = Muscle
    queryset = Muscle.objects.all().order_by('-is_front', 'name'),
    context_object_name = 'muscle_list'
    template_name = 'muscle/overview.html'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(MuscleListView, self).get_context_data(**kwargs)
        context['show_shariff'] = True
        return context


class MuscleAdminListView(MuscleListView):
    '''
    Overview of all muscles, for administration purposes
    '''
    permission_required = 'exercises.change_muscle'
    login_required = True
    queryset = Muscle.objects.order_by('name')
    template_name = 'muscle/admin-overview.html'


class MuscleAddView(CreateView):
    '''
    Generic view to add a new muscle
    '''

    model = Muscle
    fields = '__all__'
    success_url = reverse_lazy('exercise:muscle:admin-list')
    title = ugettext_lazy('Add muscle')
    form_action = reverse_lazy('exercise:muscle:add')
    # permission_required = 'exercises.add_muscle'


class MuscleUpdateView(UpdateView):
    model = Muscle
    success_url = reverse_lazy('muscle_list')
    fields = ['name']


class MuscleDeleteView(DeleteView):
    model = Muscle
    success_url = reverse_lazy('muscle_list')
