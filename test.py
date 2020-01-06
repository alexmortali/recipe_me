from app import app
import unittest

class FlaskTestApp(unittest.TestCase):
    
    def test_index_page_loads(self):
        response = app.test_client(self).get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
if  __name__ == '__main__':
          unittest.main()