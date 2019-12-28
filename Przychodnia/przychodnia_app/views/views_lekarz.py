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

from przychodnia_wizyta.models import Wizyta
from przychodnia_app.models import Lekarz
from laboratorium_app.models import BadanieLaboratoryjne


def lekarz_by_request(request):
    return Lekarz.objects.get(user=request.user)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzDashboard(View):
    template_name = "przychodnia_app/lekarz/moje-wizyty.html"
    def get(self, request):
        ja = lekarz_by_request(request)
        moje_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="REJ")
        moje_wizyty_count = moje_wizyty.count()
        return render(request, self.template_name, {
            "moje_wizyty": moje_wizyty,
            "moje_wizyty_count": moje_wizyty_count,
        })


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzZakonczoneWizyty(View):
    template_name = "przychodnia_app/lekarz/moje-zakonczone-wizyty.html"
    def get(self, request):
        ja = lekarz_by_request(request)
        zakonczone_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="ZAK")
        return render(request, self.template_name, {
            "zakonczone_wizyty": zakonczone_wizyty
        })


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzRealizujWizyte(View):
    template_name = "przychodnia_app/lekarz/realizuj-wizyte.html"
    def get(self, request, wizyta_id):
        # ja = lekarz_by_request(request)
        realizowana_wizyta = get_object_or_404(Wizyta, id=wizyta_id, status="REJ")
        context = {
            "realizowana_wizyta": realizowana_wizyta,
        }
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzPrzegladajInneWizyty(ListView):
    template_name = "przychodnia_app/lekarz/przegladaj-inne-wizyty.html"
    paginate_by = 20
    model = Wizyta
    context_object_name = "inne_wizyty_pacjenta"
    allow_empty = True

    def get(self, request, *args, **kwargs):
        realizowana_wizyta = get_object_or_404(
            self.model, id=kwargs["wizyta_id"], status="REJ"
        )
        self.object_list = self.get_queryset(realizowana_wizyta)
        context = self.get_context_data()
        context = {
            "realizowana_wizyta": realizowana_wizyta,
            **context,
        }
        return self.render_to_response(context)

    def get_queryset(self, realizowana_wizyta):
        return self.model.wizyty.inne_wizyty_pacjenta(
            realizowana_wizyta
        )


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzZlecBadanieLaboratoryjne(CreateView):
    template_name = "przychodnia_app/lekarz/zlec-badanie-lab.html"
    model = BadanieLaboratoryjne
    fields = ['uwagi_lekarza', 'slownik']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        wizyta_id = self.kwargs["wizyta_id"]
        realizowana_wizyta = get_object_or_404(
            Wizyta, id=wizyta_id, status="REJ"
        )
        context = {
            "realizowana_wizyta": realizowana_wizyta,
            **context,
        }
        return context
