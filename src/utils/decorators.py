import time
import functools
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OmniStore")

def monitor_performance(func):
    """Decorator to log execution time and errors for analytics functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f"✅ {func.__name__} completed in {duration:.4f}s")
            return result
        except Exception as e:
            logger.error(f"❌ Error in {func.__name__}: {str(e)}")
            raise e
    return wrapper