from django.test import TestCase

class BasicTestCase(TestCase):
    def test_sanity(self):
        self.assertEqual(1 + 1, 2)
