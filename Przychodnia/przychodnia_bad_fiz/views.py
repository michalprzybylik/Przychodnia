from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from common.access_decorators_mixins import (
    uprawniania_lekarz_wymagane
)
from przychodnia_bad_fiz.models import BadanieFizykalne

# Create your views here.
@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class PrzychodniaBadFizDetail(DetailView):
    template_name = "przychodnia_bad_fiz/bad-fiz-detail.html"
    context_object_name = "badanie_fiz"
    model = BadanieFizykalne

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
