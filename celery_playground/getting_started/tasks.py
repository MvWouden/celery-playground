"""Simple celery task definitions."""

from celery_playground.getting_started.celery import app


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
    """
    return x + y


@app.task
def mul(x: int | float, y: int | float) -> int | float:
    """Multiply two numbers.

    Parameters
    ----------
    x: int | float
        The first number.
    y: int | float
        The second number.

    Returns
    -------
    int | float
        The product of the two numbers.
    """
    return x * y


@app.task
def xsum(numbers: list[int | float]) -> int | float:
    """Sum a list of numbers.

    Parameters
    ----------
    numbers: list[int | float]
        The numbers to sum.

    Returns
    -------
    int | float
        The sum of the numbers.
    """
    return sum(numbers)
