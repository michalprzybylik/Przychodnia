from django import forms

from przychodnia_bad_fiz.models import BadanieFizykalne
from common.models import SlownikBadan


class WykonajBadanieFizykalneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wynik'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['slownik'].widget.attrs.update({
            'class': 'form-control select2-select'
        })
        self.fields['slownik'].queryset = SlownikBadan.objects.filter(typ="F")

    class Meta:
        model = BadanieFizykalne
        fields = ("wynik", "slownik")
