import logging


class LoggingAlreadyConfiguredError(Exception):
    """Raised when setup_logging is called more than once."""
    pass


def setup_logging(log_level: int=logging.INFO):
    """
    Configures the logging system with a standard format and level. Call this in your
    __main__.py so that it is specific to that module.

    Args:
        log_level (int): The logging level to set. Defaults to `logging.INFO`.

    Logging Format:
        - %(levelname)s: The log level (e.g., INFO, DEBUG).
        - %(asctime)s: The timestamp of the log message (formatted as YYYY-MM-DD HH:MM:SS).
        - %(module)s: The name of the module where the log was generated.
        - %(message)s: The log message.
        - %(pathname)s: The full path of the module generating the log.
        - %(lineno)d: The line number where the log was generated.

    Raises:
        LoggingAlreadyConfiguredError: If setup_logging is called more than once.

    Example:
        ```python
        # In sign module.
        logger = logging.getLogger(__name__)
        setup_logging(log_level=logging.INFO)
        logger.info('Awaiting response from signing server...')
        ```
        INFO 2024-12-16 11:31:06 [sign] Awaiting response from signing server... (build_tool/sign/sign.py:164)

    Remarks:
        DEBUG < INFO < WARNING < ERROR < CRITICAL. Logs below the specified level will not appear.
    """

    # If someone imports logging before importing this module, default handlers could get created
    # which could prevent our custom logger from being used.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Python function attribute. Instead of polluting the global space, we use this to check if we've already
    # setup logging.
    if getattr(setup_logging, "_is_initialized", False):
        raise LoggingAlreadyConfiguredError("Only call logging.setup_logging once.")
    

    log_format = (
        '%(levelname)s %(asctime)s [%(module)s] %(message)s (%(pathname)s:%(lineno)d)'
    )
    logging.basicConfig(level=log_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

    setup_logging._is_initialized = True
