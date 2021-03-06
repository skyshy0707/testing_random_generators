from .forms import CustomInputUserCreationForm as form_class
from .models import Input
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from . import make10hexs_per_line
from . import makeDir
from diehard.settings import BASE_DIR
import os
import sys
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, '.heroku/python/bin'))
'''from ...heroku.python.bin import makeBin, makeTest'''
'''from . import makeTest'''
import makeBin, makeTest




# Create your views here.

def create(request):
	inp = request
	id = request.COOKIES
	return id
		

def upload_file(request):
	if request.method == 'POST':
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			filename = request.FILES['file'].name
			form.save()
			ID = Input.objects.last().id
			makeDir.main(ID, filename)
			path = os.path.join(BASE_DIR, 'uploads\\' + str(ID))
			make10hexs_per_line.main(os.path.join(path, filename), os.path.join(BASE_DIR,'.heroku\\python\\bin\\hex.ascii'))
			j = makeBin.main('hex.ascii', 'bin')
			makeTest.main('bin', 't.txt')
			makeTest.moveFile(ID)
			
			return HttpResponseRedirect('/results/')
		else:
			return self.form_invalid(form)
	else:
		form = form_class()
	return render(request, 'home.html', {'form': form})
			
