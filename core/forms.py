from django.utils import timezone
from django import forms
from .models import Chamado


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChamadoForm, self).__init__(*args, **kwargs)
        self.fields['update_at'].initial = timezone.now