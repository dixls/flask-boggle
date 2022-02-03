from app import app
from unittest import TestCase


class BoardRenderTestCase(TestCase):
    """Tests that the board renders correctly"""

    def test_board_render(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<tr>', html)
            self.assertIn('<td>', html)
    
