from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successful"""
        email = 'test@abc.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Email for new user is normalized"""
        email = 'test@ABC.COM'
        user = get_user_model().objects.create_user(email, 'test12')
        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        """Validate email is provided"""
        email = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, 'test12')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@abc.com',
            'test12'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
