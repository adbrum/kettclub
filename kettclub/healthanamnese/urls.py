from django.conf.urls import url
from kettclub.healthanamnese.views import new, listhealthanamnese, empty_prototipo_form,success, editSaudeAnamnese, \
    delConfirmeSaudeAnamnese

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editSaudeAnamnese, name="edit"),
    url(r'^form/', empty_prototipo_form, name='form'),
    url(r'^lista/', listhealthanamnese, name='list'),
    url(r'^confirmedeletar/', delConfirmeSaudeAnamnese, name='delconfirm'),
    url(r'^sucesso/', success, name='success'),
]
