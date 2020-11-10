import pygame
from pygame.sprite import Sprite
class BlackButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na czarny"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.width_grid*4,
		settings.width_grid*4)
		self.rect.top=self.screen_rect.bottom-settings.height_grid*9
		self.rect.left=settings.width_grid*5
		self.color=(0,0,0)	
	def draw_button(self):
		"""Wyświetlenie przycisku"""
		pygame.draw.rect(self.screen,self.color,self.rect)
class BlueButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na niebieski"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.width_grid*4,
		settings.width_grid*4)
		self.rect.top=self.screen_rect.bottom-settings.height_grid*9
		self.rect.left=settings.width_grid*10
		self.color=(0,0,255)	
	def draw_button(self):
		"""Wyświetlenie przycisku"""
		pygame.draw.rect(self.screen,self.color,self.rect)
class RedButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na czerwony"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.width_grid*4,
		settings.width_grid*4)
		self.rect.top=self.screen_rect.bottom-settings.height_grid*9
		self.rect.left=settings.width_grid*15
		self.color=(255,0,0)	
	def draw_button(self):
		"""Wyświetlenie przycisku"""
		pygame.draw.rect(self.screen,self.color,self.rect)
class GreenButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na zielony"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.width_grid*4,
		settings.width_grid*4)
		self.rect.top=self.screen_rect.bottom-settings.height_grid*9
		self.rect.left=settings.width_grid*20
		self.color=(0,255,0)	
	def draw_button(self):
		"""Wyświetlenie przycisku"""
		pygame.draw.rect(self.screen,self.color,self.rect)
