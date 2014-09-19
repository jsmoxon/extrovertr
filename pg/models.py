from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
    	return self.user.username

class Contact(models.Model):
	user = models.ForeignKey(UserProfile, blank=True, null=True)
	name = models.CharField(max_length=1000, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	cadence = models.IntegerField(null=True, blank=True)
	email_next = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name