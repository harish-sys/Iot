import unittest
from unittest.mock import patch
from iot_base.model import Event, Device
from datetime import datetime
from app import app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.db.session.query')
    def test_get_events(self, mock_query):
        # Arrange
        mock_event = Event(
            id=1,
            device_id=1,
            timestamp=datetime(2024, 7, 19, 12, 34, 56),
            temperature=23.5
        )
        mock_query.return_value.filter.return_value.all.return_value = [mock_event]

        # Act
        response = self.app.get('/events?device_id=1&start_date=2024-07-01&end_date=2024-07-31')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{
            'id': 1,
            'device_id': 1,
            'timestamp': '2024-07-19T12:34:56',
            'temperature': 23.5
        }])

    @patch('app.db.session.query')
    def test_get_summary(self, mock_query):
        # Arrange
        mock_summary = {
            'min_temp': 23.5,
            'max_temp': 23.5,
            'avg_temp': 23.5
        }
        mock_query.return_value.filter.return_value.first.return_value = mock_summary

        # Act
        response = self.app.get('/summary?device_id=1&start_date=2024-07-01&end_date=2024-07-31')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'device_id': 1,
            'min_temp': 23.5,
            'max_temp': 23.5,
            'avg_temp': 23.5
        })


if __name__ == '__main__':
    unittest.main()
