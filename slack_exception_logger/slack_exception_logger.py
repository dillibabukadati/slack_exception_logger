# Created by @dillibk777 at 15/01/23
import json
import os
import requests
import traceback


class SlackExceptionLogger:
    def __init__(self, webhook_url=None, channel=None):
        self.webhook_url = webhook_url or os.environ.get('SLACK_WEBHOOK_URL')
        self.channel = channel or os.environ.get('SLACK_CHANNEL')

    def __send_to_slack(self, message):
        try:
            print(message)
            response = requests.post(self.webhook_url, data=json.dumps(message))
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f'An error occurred while pushing the exception to Slack: {err}')

    def info(self, text: str) -> None:
        """
        Sends given info text to slack
        :param text: info message
        :return: None
        """
        message = {
            'channel': self.channel,
            'text': f"Info: {text}"
        }
        self.__send_to_slack(message)

    def success(self, text: str) -> None:
        """
        Sends given info text to slack
        :param text: Success message
        :return: None
        """
        message = {
            'channel': self.channel,
            'text': f"Success: {text}"
        }
        self.__send_to_slack(message)

    def warn(self, text: str) -> None:
        """
        Sends given info text to slack
        :param text: warning message
        :return: None
        """
        message = {
            'channel': self.channel,
            'text': f"Warning: {text}"
        }
        self.__send_to_slack(message)

    def error(self, text: str) -> None:
        """
        Sends given info text to slack
        :param text: error message
        :return: None
        """
        message = {
            'channel': self.channel,
            'text': f"Error: {text}"
        }
        self.__send_to_slack(message)

    def push_exception(self, exception):
        """
        Logs the given exception to the configured slack channel
        :param exception: The exception to be logged
        """
        tb_str = traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__)
        tb_str = ''.join(tb_str)
        text = f'An exception occurred: {tb_str}'
        message = {
            'channel': self.channel,
            'text': text
        }
        self.__send_to_slack(message)

    def push_to_slack(self, exception):
        """
        Logs the given exception to the configured slack channel
        :param exception: The exception to be logged
        """
        text = ""
        if isinstance(exception, Exception):
            print('Coming')
            tb_str = traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__)
            tb_str = ''.join(tb_str)
            text = f'An exception occurred: {tb_str}'
        else:
            text = f'Info: {exception}'
        message = {
            'channel': self.channel,
            'text': text
        }
        self.__send_to_slack(message)
