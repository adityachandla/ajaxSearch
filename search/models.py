from django.db import models

# Create your models here.

class People(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	dob = models.DateField()

	def __str__(self):
		return "%s  %s   %s"%(self.name,self.email,self.dob)
