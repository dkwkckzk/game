import unittest
import json
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_choice(self):
        response = self.app.post('/play', json={"choice": "rock"})
        data = json.loads(response.data)
        self.assertIn(data["result"], ["player wins", "server wins", "draw"])

    def test_invalid_choice(self):
        response = self.app.post('/play', json={"choice": "invalid"})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
