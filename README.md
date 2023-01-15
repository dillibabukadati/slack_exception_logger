
# slack_exception_logger

A Python library that allows you to log exceptions to a Slack channel using the Slack Webhook API.
## Installation

You can install slack_exception_logger using pip:
```
pip install slack_exception_logger
```
## Usage

To use slack_exception_logger, you need to import the push_to_slack function from the library:
```
from slack_exception_logger import SlackExceptionLogger
slack_logger = SlackExceptionLogger()
```
You can then call the push_to_slack function and pass the exception object as an argument whenever an exception occurs in your code:
```
try:
    # Your code that may throw an exception
    1/0
except Exception as e:
    slack_logger.push_to_slack(e)
```
Before using the library, you need to set the following environment variables:
```
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your-webhook-url'
SLACK_CHANNEL = '#exceptions'
```
You can get the Webhook URL by creating an incoming webhook in your Slack workspace.
## Note

This library uses the traceback module to get the complete exception details, which includes the exception type, value, and the stack trace, and then sends the traceback information to the slack channel.
It is also possible to filter out the sensitive information from the traceback before sending it to slack.
## License

This library is licensed under the MIT License.
## Contribution

We welcome contributions to this library. If you have an idea for a new feature or have found a bug, please open an issue on Github.

## Buy me a Coffee
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dillibabukadati)

