import pygame
from pygame.sprite import Sprite
class DrawingElement(Sprite):
	"""Tworzenie sprite'ów, z których będzie składał się rysunek. Jako 
	kolor, program pobiera domyślną wartość, która jest aktualnie 
	ustalona"""
	def __init__(self,screen,settings,default_drawing_color):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		#Wymiary są nieco większe niż wyliczone proporcje, żeby
		#zaokrąglenia do liczb całkowitych nie tworzyły dziur
		self.rect=pygame.Rect(0,0,settings.width_grid*1.1,
		settings.height_grid*1.1)
		self.color=default_drawing_color		
	def draw_cell(self):
		"""Wyświetlenie elementu rysunku"""
		pygame.draw.rect(self.screen,self.color,self.rect)
