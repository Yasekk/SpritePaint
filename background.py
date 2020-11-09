import pygame
from pygame.sprite import Sprite
class BackgroundCell(Sprite):
	"""Tworzenie sprite'ów, z których będzie składało sie tło"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		#Wymiary są nieco większe niż wyliczone proporcje, żeby
		#zaokrąglenia do liczb całkowitych nie tworzyły dziur
		self.rect=pygame.Rect(0,0,settings.width_grid*1.1,
		settings.height_grid*1.1)
