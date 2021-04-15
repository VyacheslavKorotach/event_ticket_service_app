from django import forms

# from django.forms.extras.widgets import SelectDateWidget

CHOICES = (('1', 'Temperature measurement SOP',),)
ACCEPTANCE = (('1', 'Accept the request',), ('2', 'Decline the request',))
APPROVEMENT = (('1', 'Approve the temperature value',), ('2', 'Disapprove the temperature value',))

class PatientSelection(forms.Form):
    # birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    Choose_The_SOP = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Patient_Code = forms.CharField(max_length=25)


class PatientAcceptance(forms.Form):
    Make_your_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=ACCEPTANCE)


class TemperatureValue(forms.Form):
    Temperature_value = forms.DecimalField(max_value=42, min_value=32)

class TemperatureApprovement(forms.Form):
    Temperature_approvement = forms.ChoiceField(widget=forms.RadioSelect, choices=APPROVEMENT)
