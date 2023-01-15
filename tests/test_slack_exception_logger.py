# Created by @dillibk777 at 15/01/23
import unittest
from unittest.mock import patch, Mock
from slack_exception_logger import SlackExceptionLogger

class TestSlackExceptionLogger(unittest.TestCase):
    def setUp(self):
        self.logger = SlackExceptionLogger()

    @patch('slack_exception_logger.requests.post')
    def test_push_to_slack(self, mock_post):
        """
        Test that the push_to_slack method sends the exception message to slack
        """
        mock_response =  Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        try:
            # Your code that may throw an exception
            1/0
        except Exception as e:
            self.logger.push_to_slack(e)
            mock_post.assert_called_once()
            args, kwargs = mock_post.call_args
            self.assertEqual(kwargs['data'], '{"channel": "#exceptions", "text": "An exception occured: Traceback (most recent call last):\\n  File \"test_slack_exception_logger.py\", line 16, in test_push_to_slack\\n    1/0\\nZeroDivisionError: division by zero\\n"}')

    @patch('slack_exception_logger.requests.post')
    def test_push_to_slack_failure(self, mock_post):
        """
        Test that the push_to_slack method fails gracefully when there is an error while sending the message
        """
        mock_response =  Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        try:
            # Your code that may throw an exception
            1/0
        except Exception as e:
            self.logger.push_to_slack(e)
            mock_post.assert_called_once()
            args, kwargs = mock_post.call_args
            self.assertEqual(kwargs['data'], '{"channel": "#exceptions", "text": "An exception occured: Traceback (most recent call last):\\n  File \"test_slack_exception_logger.py\", line 16, in test_push_to_slack\\n    1/0\\nZeroDivisionError: division by zero\\n"}')
