"""Moduł testowy."""

import unittest

from settings import Settings

class TestRatio(unittest.TestCase):
	"""Test sprawdzający czy proporcje szerokości i wysokości ekranu
		zgadzają się z liczbą elementów siatki w poziomie i pionie.
		"""
	
	def test_cells_square(self):		
		settings = Settings()
		self.assertEqual(
		    settings.screen_width/settings.screen_height,
		    settings.width_grid_number/settings.height_grid_number)

unittest.main()
