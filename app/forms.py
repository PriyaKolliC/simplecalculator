from django import forms

class CalcForm(forms.Form):
	number1 = forms.FloatField(label='Value of x')
	number2 = forms.FloatField(label = 'Value of y')
	btn = forms.CharField(label = 'oprtn',required = False)
	btn = forms.CharField(label = 'oprtn',required = False)
	btn = forms.CharField(label = 'oprtn',required = False)
	btn = forms.CharField(label = 'oprtn',required = False)
	