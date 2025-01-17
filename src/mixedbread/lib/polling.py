import time
import asyncio
from typing import Union, TypeVar, Callable, Optional, Awaitable
from datetime import datetime

T = TypeVar("T")


def poll(
    fn: Callable[[], T],
    condition: Callable[[T], bool],
    max_attempts: Optional[int] = None,
    timeout_seconds: Optional[float] = None,
    interval_seconds: Union[float, Callable[[T], float]] = 1.0,
    on_retry: Optional[Callable[[T, int], None]] = None,
    error_handler: Optional[Callable[[Exception], Optional[float]]] = None,
) -> T:
    """
    Polls an operation until a condition is met or timeout/max attempts are reached.

    Args:
        operation: Function that performs the operation to be polled
        condition: Function that evaluates if the polling should continue
        max_attempts: Maximum number of polling attempts (None for infinite)
        timeout_seconds: Maximum total time to poll in seconds (None for infinite)
        interval_seconds: Time between polls in seconds, or function that returns interval
        on_retry: Optional callback for each retry attempt
        error_handler: Optional callback for handling exceptions during polling

    Returns:
        The result of the operation once condition is met

    Raises:
        TimeoutError: If timeout_seconds is reached
        RuntimeError: If max_attempts is reached
    """
    start_time = datetime.now()
    attempt = 0

    while True:
        attempt += 1

        try:
            result = fn()

            if condition(result):
                return result

            if on_retry:
                on_retry(result, attempt)

            if callable(interval_seconds):
                wait_time = interval_seconds(result)
            else:
                wait_time = interval_seconds

        except Exception as e:
            if error_handler:
                sleep_time = error_handler(e)
                if sleep_time is not None:
                    time.sleep(sleep_time)
                    continue
            raise

        if max_attempts and attempt >= max_attempts:
            raise RuntimeError(f"Maximum attempts ({max_attempts}) reached")

        if timeout_seconds:
            elapsed = (datetime.now() - start_time).total_seconds()
            if elapsed >= timeout_seconds:
                raise TimeoutError(f"Timeout ({timeout_seconds}s) reached")

        # Calculate next interval

        time.sleep(wait_time)


async def poll_async(
    fn: Callable[[], Awaitable[T]],
    condition: Callable[[T], bool],
    max_attempts: Optional[int] = None,
    timeout_seconds: Optional[float] = None,
    interval_seconds: Union[float, Callable[[T], float]] = 1.0,
    on_retry: Optional[Callable[[T, int], None]] = None,
    error_handler: Optional[Callable[[Exception], Optional[float]]] = None,
) -> T:
    """
    Asynchronous version of poll method.
    Arguments and behavior are the same as poll(), but works with async/await.
    """
    start_time = datetime.now()
    attempt = 0

    while True:
        attempt += 1

        try:
            result = await fn()

            if condition(result):
                return result

            if on_retry:
                on_retry(result, attempt)

        except Exception as e:
            if error_handler:
                sleep_time = error_handler(e)
                if sleep_time is not None:
                    await asyncio.sleep(sleep_time)
                    continue
            raise

        if max_attempts and attempt >= max_attempts:
            raise RuntimeError(f"Maximum attempts ({max_attempts}) reached")

        if timeout_seconds:
            elapsed = (datetime.now() - start_time).total_seconds()
            if elapsed >= timeout_seconds:
                raise TimeoutError(f"Timeout ({timeout_seconds}s) reached")

        # Calculate next interval
        if callable(interval_seconds):
            wait_time = interval_seconds(result)
        else:
            wait_time = interval_seconds

        await asyncio.sleep(wait_time)
