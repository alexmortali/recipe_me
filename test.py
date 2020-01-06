from app import app
import unittest

class FlaskTestApp(unittest.TestCase):
    
    def test_index_page_loads(self):
        response = app.test_client(self).get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_loads(self):
        response = app.test_client(self).get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_login_page_loads(self):
        response = app.test_client(self).get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_signup_page_loads(self):
        response = app.test_client(self).get('/sign_up', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_addrecipe_page_loads(self):
        response = app.test_client(self).get('/addrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
if  __name__ == '__main__':
          unittest.main()