from django.views.generic.list import ListView
from przychodnia_pacjent.models import Pacjent

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.access_decorators_mixins import (
    uprawniania_przegladanie_listy_pacjentow
)
from django.views.generic.detail import DetailView
from przychodnia_wizyta.models import Wizyta


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_przegladanie_listy_pacjentow, name='dispatch')
class PacjentLista(ListView):
    template_name = "przychodnia_app/pacjent-lista.html"
    model = Pacjent
    context_object_name = 'pacjenci'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_przegladanie_listy_pacjentow, name='dispatch')
class RejestratorkaWizytaDetail(DetailView):
    template_name = "przychodnia_app/wizyta-detail.html"
    context_object_name = "wizyta"
    model = Wizyta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
