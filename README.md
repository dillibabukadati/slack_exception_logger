# slack_exception_logger

A Python library that allows you to log exceptions to a Slack channel using the Slack Webhook API. It also allows you to
log information messages, success messages, warning messages and error messages to a Slack channel.

## Installation

You can install slack_exception_logger using pip:

```
pip install slack_exception_logger
```

## Usage

To use slack_exception_logger, you need to import the SlackExceptionLogger class from the library and initialize an
instance of the class:

```
from slack_exception_logger import SlackExceptionLogger
slack_logger = SlackExceptionLogger()
```

## Logging Exceptions

You can log an exception to Slack by calling the push_to_slack method and passing the exception object as an argument
whenever an exception occurs in your code:

```
try:
    # Your code that may throw an exception
    1/0
except Exception as e:
    slack_logger.push_to_slack(e)
```

If the exception object is an instance of the Exception class, it will log the complete exception details, which
includes the exception type, value, and the stack trace. If it is a string, it will log it as an information message.

## Logging Information Messages

You can log an information message to Slack by calling the info method and passing the message text as an argument:

```
slack_logger.info("This is an information message.")
```

## Logging Success Messages

You can log a success message to Slack by calling the success method and passing the message text as an argument:
```python
slack_logger.success("This is a success message.")
```

## Logging Warning Messages
You can log a warning message to Slack by calling the warn method and passing the message text as an argument:
```python
slack_logger.warn("This is a warning message.")
```
## Logging Error Messages
You can log an error message to Slack by calling the error method and passing the message text as an argument:
```python
slack_logger.error("This is an error message.")
```

## Configuration
Before using the library, you need to set the following environment variables:
```
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your-webhook-url'
SLACK_CHANNEL = '#exceptions'
```

You can get the Webhook URL by creating an incoming webhook in your Slack workspace.
[Click here](https://towardsdev.com/easy-error-tracking-a-python-library-that-sends-exceptions-directly-to-your-slack-channel-450ee9944b0c) follow the tutorial to know how enable webhooks in your slack.

## Note

This library uses the traceback module to get the complete exception details, which includes the exception type, value,
and the stack trace, and then sends the traceback information to the slack channel.
It is also possible to filter out the sensitive information from the traceback before sending it to slack.

## License

This library is licensed under the MIT License.

## Contribution

We welcome contributions to this library. If you have an idea for a new feature or have found a bug, please open an
issue on Github.

## Buy me a Coffee

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dillibabukadati)

