from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class DummyTest(TestCase):
    def test_math(self):
        self.assertEqual(1 + 1, 2)

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser")
        self.assertEqual(user.username, "testuser")


