from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from common.access_decorators_mixins import (
    uprawnienia_wspolne_lekarz_rejestratorka,
    uprawniania_lekarz_wymagane
)
from przychodnia_pacjent.models import Pacjent
from przychodnia_bad_fiz.models import BadanieFizykalne
from laboratorium_app.models import BadanieLaboratoryjne

@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawnienia_wspolne_lekarz_rejestratorka, name='dispatch')
class PacjentDetailView(DetailView):
    template_name = "przychodnia_pacjent/pacjent-detail.html"
    context_object_name = "pacjent"
    model = Pacjent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class PacjentBadaniaView(DetailView):
    template_name = "przychodnia_pacjent/pacjent-badania.html"
    context_object_name = "pacjent"
    model = Pacjent

    def get_context_data(self, **kwargs):
        pacjent = kwargs.get('object')
        context = super().get_context_data(**kwargs)
        context["badania_fiz"] = BadanieFizykalne.badania.filter(wizyta__pacjent=pacjent)
        context["badania_lab"] = BadanieLaboratoryjne.badania.filter(wizyta__pacjent=pacjent)
        return context
