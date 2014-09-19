from __future__ import absolute_import

from celery.task import PeriodicTask
import datetime
from celery.schedules import crontab
from pg.models import *
from django.core.mail import send_mail

def send_reminder(user_email, contact_email, contact_name):
	subject = "Reach out to %s" % contact_name
	body = "You can reach them at %s. It's been awhile" % contact_email
	from_email = "extrovertrapp@gmail.com"
	return send_mail(subject, body, from_email, [user_email], fail_silently=False)


class send_email_task(PeriodicTask):
    run_every = datetime.timedelta(seconds=60)

    def run(self, **kwargs):
		todays_contacts = Contact.objects.filter(email_next=datetime.date.today())
		for contact in todays_contacts:
			send_reminder(contact.user.user.email, contact.email, contact.name)
			contact.email_next = datetime.date.today() + datetime.timedelta(contact.cadence)
			contact.save()


