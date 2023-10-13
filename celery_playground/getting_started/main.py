"""Simple celery task call."""

from celery_playground.getting_started.tasks import add

add.delay(4, 4)
