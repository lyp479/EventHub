from django.http import HttpResponse
from django.template import loader
# from django.shortcuts import render


def index(request):
		template = loader.get_template('hub/index.html')
		return HttpResponse(template.render())
		 # can also use the render shortcut which returns an http response
		 #return render(request, 'hub/index.html')