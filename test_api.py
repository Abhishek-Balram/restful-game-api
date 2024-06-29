import unittest
import json
from application import application

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()
        # Clear data before each test
        application.players = {}
        application.scores = {}

    def test_get_empty_players(self):
        response = self.app.get('/players')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {})

    def test_post_player(self):
        response = self.app.post('/players', data=dict(data='Test Player'))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)  # There should be one key-value pair
        player_id = list(data.keys())[0]  # Get the first (and only) key
        self.assertEqual(data[player_id], 'Test Player')

    def test_get_players_after_post(self):
        self.app.post('/players', data=dict(data='Test Player'))
        response = self.app.get('/players')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertIn('1', data)
        self.assertEqual(data['1'], 'Test Player')

    def test_get_nonexistent_player(self):
        response = self.app.get('/players/999')
        self.assertEqual(response.status_code, 404)

    def test_put_player(self):
        self.app.post('/players', data=dict(data='Test Player'))
        response = self.app.put('/players/1', data=dict(data='Updated Player'))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['1'], 'Updated Player')

    def test_put_score(self):
        self.app.post('/players', data=dict(data='Test Player'))
        response = self.app.put('/scores/1', data=dict(score='100'))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['1'], '100')

    def test_get_score(self):
        self.app.post('/players', data=dict(data='Test Player'))
        self.app.put('/scores/1', data=dict(score='100'))
        response = self.app.get('/scores/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['1'], '100')

    def test_get_nonexistent_score(self):
        response = self.app.get('/scores/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()