from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.access_decorators_mixins import uprawniania_lekarz_wymagane


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzDashboard(View):
    template_name = "przychodnia_app/lekarz/moje-wizyty.html"
    def get(self, request):
        return render(request, self.template_name, {})
