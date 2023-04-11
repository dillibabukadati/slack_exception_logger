# Created by @dillibk777 at 15/01/23
import json
import os
import requests
import traceback


class SlackExceptionLogger:
    def __init__(self, webhook_url=None, channel=None):
        self.webhook_url = webhook_url or os.environ.get('SLACK_WEBHOOK_URL')
        self.channel = channel or os.environ.get('SLACK_CHANNEL')

    def push_to_slack(self, exception):
        """
        Logs the given exception to the configured slack channel
        :param exception: The exception to be logged
        """
        text = ""
        if isinstance(exception, Exception):
            tb_str = traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__)
            f'An exception occurred: {tb_str}'
        else:
            text = f'Info: {exception}'
        message = {
            'channel': self.channel,
            'text': text
        }

        try:
            response = requests.post(self.webhook_url, data=json.dumps(message))
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f'An error occurred while pushing the exception to Slack: {err}')
