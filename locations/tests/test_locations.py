from django.test import TestCase
from locations import models

class LocationsTestCase(TestCase):
    fixtures = ['locations']
    def setUp(self):
        pass

    def test_countries_by_minimum_city_pib(self):
        country_list = models.Country.objects.filter(states__cities__pib__gt=50).distinct()
        self.assertEqual([ country.name for country in country_list ], [ 'Brasil'])

