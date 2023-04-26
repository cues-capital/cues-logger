import logging
import logging.handlers
import socket
import sys


class CuesLogger:
    """
    A custom logging class to log messages to console and/or file with specified format.
    """

    def __init__(self, name=None, log_file="log.txt"):
        """
        Initialize the CuesLogger instance with a given name and log file.

        :param name: (optional) The logger name, defaults to the hostname.
        :param log_file: (optional) The log file name, defaults to "log.txt".
        """
        self.hostname = socket.gethostname()
        self.name = name or self.hostname
        self.log_file = log_file
        self.log = self.setup_logger()

    def setup_logger(self):
        """
        Setup the logger with the given name.

        :return: A logger instance with the specified name.
        """
        # Set the logging level to NOTSET (all messages will be logged)
        logging.getLogger().setLevel(logging.NOTSET)

        # Create a logger for the given name
        log = logging.getLogger(self.name)

        # Set the logger's propagate attribute to False so that messages are not passed to parent loggers
        log.propagate = False

        return log

    def create_formatter(self):
        """
        Create a formatter to specify the format of the log messages.

        :return: A logging.Formatter instance with the specified format.
        """
        return logging.Formatter(' %(name)-13s: %(asctime)s: %(levelname) -8s: %(message)s', '%Y-%m-%d %H:%M:%S')

    def add_console_handler(self):
        """
        Add a StreamHandler to the logger to log messages to console.
        """
        # Create a StreamHandler to log to console
        console = logging.StreamHandler(sys.stdout)

        # Set the formatter for the handler
        console.setFormatter(self.create_formatter())

        # Add the handler to the logger if it hasn't already been added
        if not any(isinstance(handler, logging.StreamHandler) for handler in self.log.handlers):
            self.log.addHandler(console)

    def add_file_handler(self, log_file=None, level=logging.NOTSET):
        """
        Add a FileHandler to the logger to log messages to a file.

        :param log_file: (optional) The log file name, defaults to the value set during initialization.
        :param level: (optional) The logging level for the FileHandler, defaults to logging.NOTSET.
        """
        log_file = log_file or self.log_file

        # Create a FileHandler to log to a file
        file_handler = logging.FileHandler(log_file)

        # Set the log level for the FileHandler
        file_handler.setLevel(level)

        # Set the formatter for the handler
        file_handler.setFormatter(self.create_formatter())

        # Add the handler to the logger if it hasn't already been added
        if not any(isinstance(handler, logging.FileHandler) for handler in self.log.handlers):
            self.log.addHandler(file_handler)

    def debug(self, msg, *args, **kwargs):
        """
        Log a debug message.

        :param msg: The message format string.
        :param args: Arguments to merge into msg.
        :param kwargs: Keyword arguments to merge into msg.
        """
        self.log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Log an info message.

        :param msg: The message format string.
        :param args: Arguments to merge into msg.
        :param kwargs: Keyword arguments to merge into msg.
        """
        self.log.info(msg, *args, **kwargs)

log = CuesLogger()
log.add_console_handler() # Only add StreamHandler

# Usage example 
# log.info("This is an info message.")
# log.error("This is an error message.")