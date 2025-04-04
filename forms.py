from django import forms
from .models import MedicalInfo

class MedicalInfoForm(forms.ModelForm):
    class Meta:
        model = MedicalInfo
        fields = ['name', 'age', 'blood_group', 'weight', 'additional_info']
