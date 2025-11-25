import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = city_country("Madrid", "Spain")
        self.assertEqual(formatted_city, "Madrid, Spain")
    def test_city_country_population(self):
        formatted_city = city_country("Madrid", "Spain", 3400000)
        self.assertEqual(formatted_city, "Madrid, Spain - Population: 3400000")

    def test_city_country_with_language(self):
        formatted_city = city_country("Madrid", "Spain", 3400000, "Spanish")
        self.assertEqual(formatted_city,"Madrid, Spain - Population: 3400000, Spanish")


if __name__ == '__main__':
    unittest.main()