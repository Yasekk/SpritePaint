"""Moduł odpowiedzialny za przyciski stanowiące częśc interfejsu."""

import pygame
import pygame.font
from pygame.sprite import Sprite, Group

class ButtonsGroup():
	"""Klasa w której są przechwowywane wszystkie podstawowe
	przyciski.
	"""
	
	def __init__(self, screen, settings):
		"""Tworzenie grupy przycisków."""
		self.buttons = Group()
		self.create_buttons(screen, settings)
		
	def create_buttons(self, screen, settings):
		"""Tworzenie przycisków i dodawanie ich do grupy."""
		self.black_button = BlackButton(screen, settings)
		self.buttons.add(self.black_button)
		self.blue_button = BlueButton(screen, settings)
		self.buttons.add(self.blue_button)
		self.red_button = RedButton(screen, settings)
		self.buttons.add(self.red_button)
		self.green_button = GreenButton(screen, settings)
		self.buttons.add(self.green_button)
		self.yellow_button = YellowButton(screen, settings)
		self.buttons.add(self.yellow_button)
		self.cyan_button = CyanButton(screen, settings)
		self.buttons.add(self.cyan_button)
		self.magenta_button = MagentaButton(screen, settings)
		self.buttons.add(self.magenta_button)
		self.gray_button = GrayButton(screen, settings)
		self.buttons.add(self.gray_button)
		self.brown_button = BrownButton(screen, settings)
		self.buttons.add(self.brown_button)
		self.white_button = WhiteButton(screen, settings)
		self.buttons.add(self.white_button)


class ColorIndicator(Sprite):
	"""Ikona, która pokazuje aktualnie uzywany kolor."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*3,
                                settings.width_grid*3)
		self.rect.top = (self.screen_rect.bottom
		                 - settings.height_grid*15)
		self.rect.left = settings.width_grid
		self.color = settings.default_drawing_color

	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class RectangleButton(Sprite):
	"""Przycisk, który będzie włączał opcję rysowania prostokąta."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = (self.screen_rect.bottom
		                 - settings.height_grid*10)
		self.rect.right = settings.screen_width - settings.width_grid*15
		self.button_color = (255, 255, 255)
		self.prep_msg("Figura")
		
	def prep_msg(self, msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class DrawingButton(Sprite):
	"""Przycisk, który będzie włączał opcję rysowania."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = (self.screen_rect.bottom
		                 - settings.height_grid*10)
		self.rect.right = settings.screen_width - settings.width_grid*25
		self.button_color = (0, 0, 0)
		self.prep_msg("Rysunek")

	def prep_msg(self, msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class SaveButton(Sprite):
	"""Przycisk, który będzie zapisywał obraz do pliku."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*7
		self.rect.right = settings.screen_width - settings.width_grid*15
		self.button_color = (0, 0, 0)
		self.prep_msg("Zapisz")

	def prep_msg(self,msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class LoadButton(Sprite):
	"""Przycisk, który będzie zapisywał obraz do pliku."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*4
		self.rect.right = settings.screen_width - settings.width_grid*15
		self.button_color = (255, 255, 255)
		self.prep_msg("Wczytaj")

	def prep_msg(self,msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class EraserButton(Sprite):
	"""Przycisk, który będzie właczał tryb zmazywania obrazu."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*7
		self.rect.right = settings.screen_width - settings.width_grid*5
		self.button_color = (255, 255, 255)
		self.prep_msg("Gumka")

	def prep_msg(self,msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class ReferenceGridButton(Sprite):
	"""Przycisk właczający siatkę podzieloną na kwadraty, która pomaga w
	rysowaniu.
	"""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
                                settings.height_grid*3)
		self.rect.top = (self.screen_rect.bottom
                         -settings.height_grid*10)
		self.rect.right = settings.screen_width - settings.width_grid*5
		self.button_color = (0, 0, 0)
		self.button_on = False
		self.prep_msg("Siatka")

	def prep_msg(self, msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		"""Wyświetlanie pustego przycisku a następnie komunikatu na nim.
		"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class ClearButton(Sprite):
	"""Przycisk, który będzie usuwał cały rysunek."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, settings.width_grid*9,
		                        settings.height_grid*3)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*4
		self.rect.right = settings.screen_width - settings.width_grid*5
		self.button_color = (0, 0, 0)
		self.prep_msg("Czyść")

	def prep_msg(self,msg):
		"""Umieszczenie komunikatu w wygenerowanym obrazie i 
		wyśrodkowanie tekstu na przycisku.
		"""
		self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Wyświetlenie przycisku oraz napisu na nim."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class BlackButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na czarny."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*5
		self.color = (0, 0, 0)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class BlueButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na niebieski."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*10
		self.color = (0, 0, 255)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class RedButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na czerwony."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*15
		self.color = (255, 0, 0)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class GreenButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na zielony."""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*20
		self.color = (0, 255, 0)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class YellowButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na żółty."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*25
		self.color = (255, 255, 0)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class CyanButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na cyjan."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*30
		self.color = (0, 255, 255)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class MagentaButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na magenta."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*35
		self.color = (255, 0, 255)
			
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class GrayButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na szary."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*40
		self.color = (128, 128, 128)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class BrownButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na brązowy."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*45
		self.color = (165, 42, 42)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)


class WhiteButton(Sprite):
	"""Przycisk, który będzie zmieniał kolor rysowania na biały."""

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.width_grid*4,
                                settings.width_grid*4)
		self.rect.top = self.screen_rect.bottom - settings.height_grid*9
		self.rect.left = settings.width_grid*50
		self.color = (255, 255, 255)
	
	def draw_button(self):
		"""Wyświetlenie przycisku."""
		pygame.draw.rect(self.screen, self.color, self.rect)

