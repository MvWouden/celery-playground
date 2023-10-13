"""Simple celery task definitions."""

from celery import Celery

app: Celery = Celery(main="tasks")


@app.task
def add(x: int | float, y: int | float) -> int | float:
    """Add two numbers.

    Parameters
    ----------
    x: int | float
        The first number.
    y: int | float
        The second number.

    Returns
    -------
    int | float
        The sum of the two numbers.

    Notes
    -----
    See https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html.
    """
    return x + y
