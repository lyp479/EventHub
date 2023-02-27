from django.db import models

# this is a skeleton of the proper model (this structure is temp)
class PlannedEvent(models.Model):
	title = models.TextField()
	description = models.TextField()
	date = models.DateTimeField()