from django.shortcuts import render,redirect
from django.views import View
from .forms import PeopleForm
from .models import People

class Adder(View):
	def get(self,request):
		form = PeopleForm()
		return render(request,'search/add.html',{'form':form})

	def post(self,request):
		form = PeopleForm(request.POST)
		form.save()
		print(People.objects.all())
		return redirect('add')


class Searcher(View):
	def get(self,request):
		searchval = request.GET.get('value')
		if searchval == None:
			return render(request,'search/search.html')
		matches = People.objects.filter(name__startswith=searchval).all()
		print("value was ",searchval)
		return render(request,'search/searchRes.html',{'matches':matches})