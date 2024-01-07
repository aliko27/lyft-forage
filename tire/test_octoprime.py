from tire.octoprime_tire import Octoprime
import unittest

class TestOctoprime(Octoprime):
    def should_be_serviced(self):
        tire_weariness = [0.87, 0.91, 0.90, 0.45]
        carrigan = Octoprime(tire_weariness)
        self.assertTrue(self.carrigan.needs_service())

    def should_not_be_serviced(self):
        tire_weariness = [0.87, 0.89, 0.21, 0.45]
        carrigan = Octoprime(tire_weariness)
        self.assertFalse(self.carrigan.needs_service())


if __name__ == '__main__':
    unittest.main()
