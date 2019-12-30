from django import forms

from przychodnia_wizyta.models import Wizyta


class LekarzWywiadForm(forms.ModelForm):

    class Meta:
        model = Wizyta
        fields = ("opis", "diagnoza")

    def __init__(self, *args, **kwargs):
        super(LekarzWywiadForm, self).__init__(*args, **kwargs)
        self.fields['opis'].widget.attrs.update({
            'class': 'form-control',
            'rows': '4'
        })
        self.fields['diagnoza'].widget.attrs.update({
            'class': 'form-control',
            'rows': '4'
        })
