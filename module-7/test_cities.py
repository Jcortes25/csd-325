import unittest
from city_functions import city_country

class TestCityCountryFunction(unittest.TestCase):
    """Test the city_country function."""
    
    def test_city_country(self):
        """Test the city_country function with city, country, population, and language."""
        result = city_country('Santiago', 'Chile', 5000000, 'Spanish')
        self.assertEqual(result, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()
