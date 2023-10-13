"""Simple celery task call."""

from celery_playground.getting_started.tasks import add

if __name__ == "__main__":
    add.delay(4, 4)
