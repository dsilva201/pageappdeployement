from django.test import SimpleTestCase
class SimpleTests(SimpleTestCase):
    def testhome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testabout(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)