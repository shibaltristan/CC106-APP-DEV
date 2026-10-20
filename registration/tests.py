from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentRegistrationTests(TestCase):
    def test_registration_form_loads(self):
        response = self.client.get(reverse('student_registration'))

        self.assertEqual(response.status_code, 200)
        for field in (
            'student_id',
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'contact_no',
        ):
            self.assertContains(response, f'name="{field}"')
        self.assertContains(response, 'Register Student')

    def test_valid_registration_creates_student_and_shows_success(self):
        response = self.client.post(
            reverse('student_registration'),
            {
                'student_id': 'TEST-001',
                'first_name': 'Taylor',
                'last_name': 'Example',
                'gender': 'Female',
                'date_of_birth': '2000-01-01',
                'contact_no': '09123456789',
            },
        )

        self.assertRedirects(response, reverse('registration_success'))
        self.assertTrue(Student.objects.filter(student_id='TEST-001').exists())

        success_response = self.client.get(reverse('registration_success'))
        self.assertEqual(success_response.status_code, 200)
        self.assertContains(success_response, 'Student Registered Successfully!')
