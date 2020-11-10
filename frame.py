import pygame
from pygame.sprite import Sprite
class FrameTop(Sprite):
	"""Ramka, na której będzie znajdował się interfejs użytkownika"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.screen_width,
		settings.height_grid*5)
		self.rect.top=self.screen_rect.top
		self.rect.left=self.screen_rect.left
		self.color=settings.frame_color		
	def draw_frame(self):
		"""Wyświetlenie elementu ramki"""
		pygame.draw.rect(self.screen,self.color,self.rect)
class FrameBottom(Sprite):
	"""Ramka, na której będzie znajdował się interfejs użytkownika"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.screen_width,
		settings.height_grid*10)
		self.rect.bottom=self.screen_rect.bottom
		self.rect.left=self.screen_rect.left
		self.color=settings.frame_color		
	def draw_frame(self):
		"""Wyświetlenie elementu ramki"""
		pygame.draw.rect(self.screen,self.color,self.rect)
class FrameSide(Sprite):
	"""Ramka, na której będzie znajdował się interfejs użytkownika"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.width_grid*5,
		settings.screen_height)
		self.rect.top=self.screen_rect.top
		self.rect.left=self.screen_rect.left
		self.color=settings.frame_color		
	def draw_frame(self):
		"""Wyświetlenie elementu ramki"""
		pygame.draw.rect(self.screen,self.color,self.rect)
