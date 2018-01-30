from .models import Workbench, upLoad
from django import forms

class DocumentForm(forms.ModelForm):
    class Meta:
        model = upLoad
        fields = ('document', )

# class WorkbenchForm(forms.ModelForm):
#     class Meta:

#         model = Workbench
#         fields = ('',)