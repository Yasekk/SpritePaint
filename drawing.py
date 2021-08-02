"""Moduł zawierający klasy określające elemety rysnków."""

import pygame
from pygame.sprite import Sprite

class DrawingElement(Sprite):
	"""Tworzenie sprite'ów, z których będzie składał się rysunek. Jako 
	kolor, program pobiera domyślną wartość, która jest aktualnie 
	ustalona.
	"""
	
	def __init__(self, screen, settings, default_drawing_color):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#Wymiary są nieco większe niż wyliczone proporcje, żeby
		#zaokrąglenia do liczb całkowitych nie tworzyły dziur.
		self.rect = pygame.Rect(0, 0, settings.width_grid*1.1,
		                        settings.height_grid*1.1)
		self.color = default_drawing_color
		
	def draw_cell(self):
		"""Wyświetlenie elementu rysunku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class DrawingRectangle(Sprite):
	"""Prostokąt, którego wymiary będą zależały od miejsca kliknięcia i
	aktualnego położenia kursora.
	"""
	
	def __init__(self, screen, settings, default_drawing_color, mouse_x,
	             mouse_y):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#Początkowe miejsce kliknięcia myszą, będzie zapisane jako jeden
		#z rogów prostokąta.
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y
		self.color = default_drawing_color
		
	def draw_rectangle(self):
		"""Wyświetlenie prostokąta."""
		mouse_x, mouse_y = pygame.mouse.get_pos()
		#Prostokąt będzie zmieniał położenie i rozmiar w zależności od
		#początkowego miejsca kliknięcia i aktualnej pozycji kursora.
		if mouse_x >= self.mouse_x and mouse_y >= self.mouse_y:
			self.rect = pygame.Rect(0, 0, (mouse_x-self.mouse_x),
			                        (mouse_y-self.mouse_y))
			self.rect.top = self.mouse_y
			self.rect.left = self.mouse_x
		elif mouse_x >= self.mouse_x and mouse_y < self.mouse_y:
			self.rect = pygame.Rect(0, 0, (mouse_x-self.mouse_x),
			                        (self.mouse_y-mouse_y))
			self.rect.bottom = self.mouse_y
			self.rect.left = self.mouse_x
		elif mouse_x < self.mouse_x and mouse_y >= self.mouse_y:
			self.rect = pygame.Rect(0, 0, (self.mouse_x-mouse_x),
			                        (mouse_y-self.mouse_y))
			self.rect.top = self.mouse_y
			self.rect.right = self.mouse_x
		elif mouse_x < self.mouse_x and mouse_y < self.mouse_y:
			self.rect = pygame.Rect(0, 0, (self.mouse_x-mouse_x),
			                        (self.mouse_y-mouse_y))
			self.rect.bottom = self.mouse_y
			self.rect.right = self.mouse_x
		pygame.draw.rect(self.screen, self.color, self.rect)
