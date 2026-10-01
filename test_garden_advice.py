"""Tests work both in the course folder and in the published repository."""

from pathlib import Path
import importlib.util
import unittest

code = Path(__file__).parent / "Code Files"
if code.is_dir():
    source = code / "garden_advice.py"
else:
    source = Path(__file__).parent / "garden_advice.py"
spec = importlib.util.spec_from_file_location("garden_advice", source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
get_gardening_advice = module.get_gardening_advice


class GardenTests(unittest.TestCase):
    def test_summer_flowers(self):
        advice = get_gardening_advice("summer", "flower")
        self.assertIn("Water", advice)
        self.assertIn("blooms", advice)

    def test_unknown_inputs(self):
        self.assertIn("No advice", get_gardening_advice("unknown", "unknown"))


if __name__ == "__main__":
    unittest.main()
