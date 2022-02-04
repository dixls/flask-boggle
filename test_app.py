from app import app
from unittest import TestCase

app.config['TESTING'] = True

class BoggleTestCase(TestCase):
    """Tests that the board renders correctly"""

    
    def test_board_render(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<tr>', html)
            self.assertIn('<td>', html)

    def test_check_guess(self):
        with app.test_client() as client:
            resp = client.post('/guess', json = {"guess": "fewfwe"})
            result = resp.get_json()
            
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(False, result['result'])

    def test_get_guesses(self):
        with app.test_client() as client:
            resp = client.get('/guess')
            result = resp.get_json()

            self.assertEqual(resp.status_code, 200)
            self.assertIsInstance(result, dict)
    
    def test_restart_game(self):
        with app.test_client() as client:
            resp = client.get('/restart')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/')
