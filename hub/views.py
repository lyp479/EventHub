from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from hub.models import PlannedEvent

# note: request object is an HttpRequestObject, it has information about
#  request, such as the method, which can take several values including GET and POST
def index(request):
	planned_events = PlannedEvent.objects.all()
	context = {
		'events' : planned_events
	}
	# render() looks for HTML templates inside templates directory inside app directory
	return render(request, 'hub/index.html', context)


# This is the view which handles urls for the event pages themselves
def event_detail(request, primary_key):
	event = get_object_or_404(PlannedEvent, pk=primary_key)
	context = {
		'event' : event
	}

	return render(request, 'event_page.html', context)