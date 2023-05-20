import unittest
from tires.tires import Tires
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires

class TiresTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary preconditions for the tests
        self.tire_wear = [0.2, 0.4, 0.5, 0.3]  # Example tire wear values

    def tearDown(self):
        # Clean up any resources used during the tests
        pass

    def test_octoprime_tires_need_service(self):
        tires = OctoprimeTires(self.tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_tires_do_not_need_service(self):
        self.tire_wear = [0.1, 0.2, 0.3, 0.4]  # Lower tire wear values
        tires = OctoprimeTires(self.tire_wear)
        self.assertFalse(tires.needs_service())

    def test_carrigan_tires_need_service(self):
        tires = CarriganTires(self.tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_do_not_need_service(self):
        self.tire_wear = [0.1, 0.2, 0.3, 0.4]  # Lower tire wear values
        tires = CarriganTires(self.tire_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
