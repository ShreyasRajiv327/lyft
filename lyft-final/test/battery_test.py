import unittest
from datetime import date
from Battery import Battery
from Battery.Battery_type.nubbin_battey import NubbinBattery
from Battery.Battery_type.spidler_battery import SpindlerBattery


class BatteryTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary preconditions for the tests
        self.current_date = date.today()
        self.last_service_date = date(2022, 1, 1)

    def tearDown(self):
        # Clean up any resources used during the tests
        pass

    def test_nubbin_battery_needs_service(self):
        battery = NubbinBattery(self.current_date, self.last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        self.last_service_date = date.today()  # Set last_service_date to today
        battery = NubbinBattery(self.current_date, self.last_service_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service(self):
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        self.last_service_date = date.today()  # Set last_service_date to today
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
