import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class EngineTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary preconditions for the tests
        self.last_service_date = date(2022, 1, 1)
        self.current_mileage = 50000
        self.last_service_mileage = 40000
        self.warning_light_is_on = True

    def tearDown(self):
        # Clean up any resources used during the tests
        pass

    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_capulet_engine_does_not_need_service(self):
        engine = CapuletEngine(self.last_service_date, self.current_mileage, self.current_mileage - 1000)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(self.last_service_date, self.warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_sternman_engine_does_not_need_service(self):
        engine = SternmanEngine(self.last_service_date, False)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_willoughby_engine_does_not_need_service(self):
        engine = WilloughbyEngine(self.last_service_date, self.current_mileage, self.current_mileage - 1000)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
