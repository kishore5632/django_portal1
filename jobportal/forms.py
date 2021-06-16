from django import forms
from .models import *

#apply form
class applyform(forms.ModelForm):
    class Meta:
        model = applyjob
        fields = "__all__"
