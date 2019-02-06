from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django import forms
from .forms import CalcForm
# Create your views here.


def index(request):  
	if request.method == 'POST':
		form = CalcForm(request.POST)
		if form.is_valid():
			print('Form valid')
			num_string = '- and -'
			num1 = form.cleaned_data['number1']
			print(num1)
			num2 = form.cleaned_data['number2']
			print(num2)
			opr = form.cleaned_data['btn']
			print(opr)
			if opr == '+':
				output = num1+num2
			elif opr == '-':
				output = num1-num2
			elif opr == '*':
				output = num1*num2
			else:
				try:
					output = num1 / num2
				except ZeroDivisionError:
					output = 0
			num_string = str(num1) + ' '+ str(opr) +' ' + str(num2)
			#return render(request,'app/index.html',{'num_string':num_string,'output':output})	
			return render(request,'app/index.html',{'num_string':num_string,'output':output})	
			
		else:
			print('Form not valid')
			num_string = '- and -'
			form = CalcForm()
			return render(request,'app/index.html', {'num_string':num_string,'output':'-'})
	else:
		num_string = '- and -'
		return render(request,'app/index.html', {'num_string':num_string,'output':'-'})
			
def thanks(request,output):
	return render(request, 'app/success.html', output)
	