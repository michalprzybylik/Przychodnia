from django import forms

from laboratorium_app.models import BadanieLaboratoryjne
from common.models import SlownikBadan


class ZlecBadanieLaboratoryjneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uwagi_lekarza'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['slownik'].widget.attrs.update({
            'class': 'form-control select2-select'
        })
        self.fields['slownik'].queryset = SlownikBadan.objects.filter(typ="L")

    class Meta:
        model = BadanieLaboratoryjne
        fields = ("uwagi_lekarza", "slownik")


class BadanieLabWykonaj(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wynik'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = BadanieLaboratoryjne
        fields = ("wynik",)


class BadanieKierZatwierdz(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uwagi_kierownika'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = BadanieLaboratoryjne
        fields = ("uwagi_kierownika",)
