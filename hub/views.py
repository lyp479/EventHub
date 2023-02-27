from django.http import HttpResponse
from django.shortcuts import render

# note: request object is an HttpRequestObject, it has information about
#  request, such as the method, which can take several values including GET and POST
def index(request):
	# render() looks for HTML templates inside templates directory inside app directory
	return render(request, 'hub/index.html', {})