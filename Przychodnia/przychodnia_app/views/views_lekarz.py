from django.shortcuts import render, redirect, reverse
from django.utils import timezone
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
from przychodnia_app.forms import LekarzWywiadForm
from przychodnia_app.models import Lekarz
from laboratorium_app.models import BadanieLaboratoryjne
from przychodnia_bad_fiz.models import BadanieFizykalne
from laboratorium_app.forms import ZlecBadanieLaboratoryjneForm
from przychodnia_bad_fiz.forms import WykonajBadanieFizykalneForm


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
        realizowana_wizyta = get_object_or_404(Wizyta, id=wizyta_id, status="REJ")
        bad_lab_w_ramach_wizyty = BadanieLaboratoryjne.badania.w_ramach_wizyty(
            realizowana_wizyta
        )
        bad_fiz_w_ramach_wizyty = BadanieFizykalne.badania.w_ramach_wizyty(
            realizowana_wizyta
        )
        context = {
            "wywiad_form": LekarzWywiadForm(instance=realizowana_wizyta),
            "realizowana_wizyta": realizowana_wizyta,
            "bad_lab_w_ramach_wizyty": bad_lab_w_ramach_wizyty,
            "bad_fiz_w_ramach_wizyty": bad_fiz_w_ramach_wizyty,
        }
        return render(request, self.template_name, context)

    def post(self, request, wizyta_id):
        wizyta_id = self.kwargs.get('wizyta_id')
        wywiad_action = request.POST.get('wywiad_action')
        realizowana_wizyta = get_object_or_404(Wizyta, id=wizyta_id, status="REJ")
        form = LekarzWywiadForm(request.POST, instance=realizowana_wizyta)

        if wywiad_action == "zapisz":
            form.save()
            messages.success(self.request, "Zapisano stan wizyty")
            return HttpResponseRedirect(reverse(
                "przychodnia_app:lekarz-realizuj-wizyte",
                kwargs={
                "wizyta_id": wizyta_id
                }
            ))

        if wywiad_action == "zatwierdz":
            form.save()
            realizowana_wizyta.status = "ZAK"
            realizowana_wizyta.dt_zak_anul = timezone.now()
            realizowana_wizyta.save()
            messages.success(self.request, "Wizyta została zakończona")
            return HttpResponseRedirect(reverse(
                "przychodnia_app:lekarz-moje-wizyty"
            ))

        messages.success(self.request, "Coś poszło nie tak. Skontaktuj się z administratorem")
        return HttpResponseRedirect(reverse(
            "przychodnia_app:lekarz-realizuj-wizyte",
            kwargs={
            "wizyta_id": wizyta_id
            }
        ))

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


class BadanieView():
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        wizyta = get_object_or_404(
            Wizyta, id=self.kwargs.get("wizyta_id")
        )
        self.object.wizyta = wizyta
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzZlecBadanieLaboratoryjne(BadanieView, CreateView):
    template_name = "przychodnia_app/lekarz/zlec-badanie-lab.html"
    form_class = ZlecBadanieLaboratoryjneForm

    def get_success_url(self):
        messages.success(self.request, "Badanie laboratoryjne dodane poprawnie")
        return reverse(
            "przychodnia_app:lekarz-realizuj-wizyte",
            kwargs={
                "wizyta_id": self.kwargs.get("wizyta_id")
            }
        )


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzWykonajBadanieFizykalne(BadanieView, CreateView):
    template_name = "przychodnia_app/lekarz/wykonaj-badanie-fiz.html"
    form_class = WykonajBadanieFizykalneForm

    def get_success_url(self):
        messages.success(self.request, "Badanie fizykalne dodane poprawnie")
        return reverse(
            "przychodnia_app:lekarz-realizuj-wizyte",
            kwargs={
                "wizyta_id": self.kwargs.get("wizyta_id")
            }
        )
