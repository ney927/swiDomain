from django import forms
from .models import client, industryChoices, positionChoices

class clientForm(forms.ModelForm):
  class Meta:
    model = client
    fields = [
      'name',
      'country',
      'residency',
      'status',
      'email',
      'phone_number',
      'experience',
      'industry',
      'position',
      'education',
      'resume',
    ]
  def clean(self):
    cleaned_data = super().clean()
    res = cleaned_data.get('residency')
    stat = cleaned_data.get('status')
    print(res)
    print(stat)

    if res == 'CAN' and stat == 'N/A':
      raise forms.ValidationError("Status cannot be N/A if residency is Canada")
    if res == 'Other' and stat != 'N/A':
      raise forms.ValidationError("If residency is other, status must be N/A")
    return cleaned_data

class addIndustry(forms.ModelForm):
  class Meta:
    model = industryChoices
    fields = [
      'ind'
    ]

class addPosition(forms.ModelForm):
  class Meta:
    model = positionChoices
    fields = [
      'pos'
    ]
