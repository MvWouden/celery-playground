"""Run celery server."""
from celery import Celery

app: Celery = Celery(
    main="getting_started",
    include=["celery_playground.getting_started.tasks"],
)

# Optional configuration
app.conf.update(result_expires=3600)

if __name__ == "__main__":
    app.start()
