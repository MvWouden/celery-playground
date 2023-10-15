"""Simple celery task call."""
from celery.result import AsyncResult

from celery_playground.first_steps.tasks import add

if __name__ == "__main__":
    result: AsyncResult = add.delay(4, 4)

    print(f"Result ready: {result.ready()}")
    print(f"Result: {result.get(timeout=5, propagate=False)}")
