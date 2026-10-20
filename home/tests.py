from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_landing_page_loads_and_links_to_home(self):
        response = self.client.get(reverse('landing'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to My Django Application')
        self.assertContains(response, reverse('home'))

    def test_home_page_loads_with_message_and_landing_link(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Home Page')
        self.assertContains(response, 'Welcome to my first Django application!')
        self.assertContains(response, reverse('landing'))
