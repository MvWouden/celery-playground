"""Simple celery task call."""

from celery_playground.getting_started.tasks import add

if __name__ == "__main__":
    result = add.delay(4, 4)

    print(f"Result ready: {result.ready()}")
    print(f"Result: {result.get(timeout=5, propagate=False)}")
