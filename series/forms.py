from django import forms

from series.models import Series


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name', 'episode', 'season')
