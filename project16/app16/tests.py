from django.test import TestCase
from django.test import SimpleTestCase

class MySimpleTest(SimpleTestCase):
    def test_my_main_page(self):
        response = self.client.get('/')
        print(response)
        print("###############")
        print(response.status_code)

class MySimpleeTest(SimpleTestCase):
    def test_my_about_page(self):
        response = self.client.get('about/')
        print(response)
        print("*****************")
        print(response.status_code)


