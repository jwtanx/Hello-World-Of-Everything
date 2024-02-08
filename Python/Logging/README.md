# Basics Notes for Logging

# TL;DR (Too long, didn't read)
## Default logging output into command line and log file
```py
import logging

logging.basicConfig(level=logging.DEBUG)
file_handler = logging.FileHandler(filename="app.log", mode="a")
format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
datetime_format="%Y-%m-%d %H:%M:%S"

# Setting the format
# formatter = logging.Formatter(format) # Also work
formatter = logging.Formatter(format, datetime_format)
logging.root.handlers[0].setFormatter(formatter)
file_handler.setFormatter(formatter)
logging.root.addHandler(file_handler)
logging.debug("debug success")

```
---

## General script for setting up the logging
1. Using the default logging method
```py
import logging
logging.basicConfig(level=logging.INFO)
logging.info("SERVER STARTED")
```

2. Creating a new logger
```py
import logging

# Creating a logger
app_name = "mlflow"
logger = logging.getLogger(app_name)
logger.setLevel(logging.WARNING)
logger.critical("SERVER GG")
```

## Logging Levels
General logging level using the default logging without creating a logger
For example, if we set the logging level to logging.WARNING, the log will only be output only when the logging.warning() to logging.critical(). The logging.info() and logging.debug() will not be output
```py
import logging

logging.root.setLevel(logging.CRITICAL)

# Example logging calls (insert into your program)
logging.critical("Host %s unknown", hostname)
logging.error("Couldn't find %r", item)
logging.warning("Feature is deprecated")
logging.info("Opening file %r, mode = %r", filename, mode)
logging.debug("Got here")

# Setting the default logging level to INFO
logging.basicConfig(level=logging.INFO)

# The log will not be output if we use the logging.debug("run?") but only output starting from INFO TO CRITICAL
logging.info("Server started")

```
2. Using a logger
```py
name_of_logger = "server-logger"
logger = logging.getLogger(name_of_logger)

# Setting the level
logger.setLevel(logging.WARNING)
logger.info("SERVER STARTED") # WILL NOT BE OUTPUT
logger.critical("FORCE SHUTTING DOWN")
```

## Getting the list of logger
```py
# Printing the list of the logger with it respective logging level
print(logging.root.manager.loggerDict)

# Getting the list of loggers
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

```

## Setting the Configuration
1. Using basicConfig to set the configuration of the logger
```py
import logging
logging.basicConfig(filename="app.log", filemode="a", format="%(name)s -> %(levelname)s: %(message)s", level=logging.DEBUG)
# default: %(levelname)s:%(name)s:%(message)s

logging.warning("warning")
# NOTE: output will not be in the command line, but it wlll be saved into the app.log because you have specify a filename
# filemode = "a" --> appending, adding more logs
# filemode = "w" --> recreating a new log file, old log file with data will be cleaned
# filemode by default is "a"
```

2. For self created logger
```py
import logging

logger = logging.getLogger("logger-1")
logger.setLevel(logging.WARNING)
FileOutputHandler = logging.FileHandler("app.log", mode="a")
logger.addHandler(FileOutputHandler)
logger.warning("Warning.") # Output will only be saved into the app.log
```

## SETTING THE FORMAT
```py
import logging

logging.basicConfig(level=logging.DEBUG)
file_handler = logging.FileHandler(filename="app.log", mode="a")
format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
datetime_format="%Y-%m-%d %H:%M:%S %z"

# Setting the format
# formatter = logging.Formatter(format) # Also work
formatter = logging.Formatter(format, datetime_format)
logging.root.handlers[0].setFormatter(formatter)
file_handler.setFormatter(formatter)
logging.root.addHandler(file_handler)
logging.debug("debug success")
```

## SETTING THE FORMAT TO NON-ROOT LOGGER
```py
import logging

APP_NAME = "app-logger"
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S %z")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Hello")
# [02/05/2024 20:29:50 +0800] INFO:my_logger:Hello
```
Logger class
```py
import logging


class Logger:

  def __init__(self,
               name,
               level=logging.INFO,
               fmt="[%(asctime)s] %(levelname)s:%(name)s:%(message)s",
               datefmt="%Y-%m-%d %H:%M:%S %z") -> None:
    """Initialize a logger with the specified name and level.

    Args:
      name (str): The name of the logger
      level (int, optional): The level of the logger. Defaults to logging.INFO.
      fmt (str, optional): The format of the log message. Defaults to "[%(asctime)s] %(levelname)s:%(name)s:%(message)s".
      datefmt (str, optional): The format of the date. Defaults to "%Y-%m-%d %H:%M:%S %z".
    """
    self.name = name
    self.level = level
    self.fmt = fmt
    self.datefmt = datefmt

  def get_logger(self):
    """Return a logger with the specified name, level, format and date format.

    Returns:
      logging.Logger: A logger with the specified name, level, format and date format.
    """
    logger = logging.getLogger(self.name)
    logger.setLevel(self.level)
    formatter = logging.Formatter(fmt=self.fmt, datefmt=self.datefmt)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

```

## OUTPUT LOGS TO FILES AND COMMAND LINE
In the basicConfig, if you added a filename argument, the output will only goes to the output file, it will not be printed out into the command line.
In that case, if you want the handlers to have FileHandler and the StreamHandler.
[REFERENCE](https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout)
[CHECK THE TD;LR](#tldr)
```py
import logging
logging.getLogger().addHandler(logging.StreamHandler())

```
If you want stdout instead of stderr
```py
import sys
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
```