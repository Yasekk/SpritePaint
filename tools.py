"""Moduł określające narzędzia pomocnicze do rsowania."""

import pygame
from pygame.sprite import Sprite

class VerticalReferenceGrid(Sprite):
	"""Pionowe elementy siatki podzielonej na kwadraty, która pomaga w
	rysowaniu."""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, 1, settings.screen_height)
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		self.color=(0, 0, 0)

	def draw_grid_element(self):
		"""Wyświetlenie linii stanowiącej element siatki."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class HorizontalReferenceGrid(Sprite):
	"""Poziome elementy siatki podzielonej na kwadraty, która pomaga w
	rysowaniu."""
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.screen_width, 1)
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		self.color = (0, 0, 0)

	def draw_grid_element(self):
		"""Wyświetlenie linii stanowiącej element siatki."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class Pointer(Sprite):
	"""Niewidzialny kwadrat odpowiedzialny za tryb malowania. Jego 
	aktualne położenie odpowiada pozycji kursora. Podczas kliknięcia, 
	będzie tworzył fragment rysunku.
	"""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, 1, 1)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.color = (0, 0, 0)
