from django.test import TestCase
from .models import Location
# Create your tests here.


class LocationModelTest(TestCase):

    def test_string_representation(self):
        location = Location(location_name="Babbio Room 210")
        self.assertEqual(str(location), location.location_name)



