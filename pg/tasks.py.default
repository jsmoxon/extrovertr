from __future__ import absolute_import

from celery.task import PeriodicTask
from datetime import date, timedelta
from pg.models import *

class Creater(PeriodicTask):
    run_every = timedelta(seconds=5)

    def run(self, **kwargs):
        print "bla bla"
        logger = self.get_logger(**kwargs)
        logger.info("Running printer task.")
        jack = UserProfile.objects.get(pk=1)
        Contact.objects.create(user=jack, name="test")
        return True