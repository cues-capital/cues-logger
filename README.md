# CuesLogger

A Python logging utility for logging messages to console and/or a file using a specified format. `CuesLogger` provides an easy-to-use interface for adding console and file handlers with custom formatting and logging levels.

## Features

- Log messages to console
- Log messages to a file
- Customizable log format
- Set log levels for console and file handlers separately

## Usage

To utilize `CuesLogger`, simply import the class and create an instance:

```python
from cues_logger import CuesLogger

logger = CuesLogger()
```

By default, the logger instance will not have any handlers. You can add a console handler and a file handler using the following methods:

```python
logger.add_console_handler()
logger.add_file_handler(log_file="example.log", level=logging.ERROR)
```

You can log messages at different log levels using the provided methods:

```python
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
```

## Customization

The logger name defaults to the system's hostname, but you can set a custom name during initialization:

```python
logger = CuesLogger(name="my-custom-logger")
```

You can also change the default log file name:

```python
logger = CuesLogger(log_file="my-log-file.txt")
```

When adding a file handler, you can set a custom log level. For example, to log only error and critical messages to the file:

```python
logger.add_file_handler(log_file="errors.log", level=logging.ERROR)
```

## Installation

To use `CuesLogger` in your project, copy the `cues_logger.py` file to your project directory and import it as shown in the Usage section.

## Requirements

- Python 3.6+

## Example

Here's a complete example demonstrating how to use `CuesLogger`:

```python
from cues_logger import CuesLogger
import logging

# Initialize the logger with a custom name
logger = CuesLogger(name="example-logger")

# Add a console handler
logger.add_console_handler()

# Add a file handler with custom log level
logger.add_file_handler(log_file="example.log", level=logging.WARNING)

# Log messages with different log levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
```

In this example, debug and info messages will only be logged to the console, while warning, error, and critical messages will be logged to both the console and the `example.log` file.

## Contributing

Contributions to `CuesLogger` are welcome! If you find a bug or would like to propose a new feature, feel free to open an issue or submit a pull request.

## License

`CuesLogger` is released under the [MIT License](https://opensource.org/licenses/MIT).
