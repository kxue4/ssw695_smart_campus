from django.test import TestCase
from .models import *
from .forms import FeedbackForm


# Models
class LocationModelTest(TestCase):

    def test_verbose_name_location(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Location._meta.db_table), "core_location")


class DataModelTest(TestCase):

    def test_verbose_name_data(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Data._meta.db_table), "data")


class PressureModelTest(TestCase):

    def test_verbose_name_pressure(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Pressure._meta.db_table), "core_pressure")


class SensortypeModelTest(TestCase):

    def test_verbose_name_sensortype(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Sensortype._meta.db_table), "core_sensortype")


class SingleboardcomputerModelTest(TestCase):

    def test_verbose_name_singleboardcomputer(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Singleboardcomputer._meta.db_table), "core_singleboardcomputer")


class SingleboardcomputertypeModelTest(TestCase):

    def test_verbose_name_singleboardcomputertype(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Singleboardcomputertype._meta.db_table), "core_singleboardcomputertype")


class TemperatureModelTest(TestCase):

    def test_verbose_name_temperature(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(Temperature._meta.db_table), "core_temperature")


class UserModelTest(TestCase):

    def test_verbose_name_user(self):
        """
        Should return True for table name.
        """
        self.assertEqual(str(User._meta.db_table), "core_user")


# Urls
class ProjectTests(TestCase):

    def test_homepage(self):
        """
        Test the status code for homepage should equal 200.
        """
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 301)

    def test_locationpage(self):
        """
        Test the status code for location page should equal 200.
        """
        response = self.client.get('/select_location')
        self.assertEqual(response.status_code, 301)

    def test_campus_reportpage(self):
        """
        Test the status code for campus report page should equal 200.
        """
        response = self.client.get('/campus_report/')
        self.assertEqual(response.status_code, 200)

    def test_feedbackpage(self):
        """
        Test the status code for feedback page should equal 200.
        """
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

