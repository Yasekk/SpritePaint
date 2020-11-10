import pygame
import sys
from settings import Settings
import functions as fct
from pygame.sprite import Group
def run_program():
	#Inicjalizacja programu i wczytywanie początkowych wartości
	pygame.init()
	settings=Settings()
	screen=pygame.display.set_mode((settings.screen_width,
	settings.screen_height))
	pygame.display.set_caption("Sprite Painter")
	#Tworzenie w tle niewidzlanej siatki komórek
	background_grid=Group()
	fct.create_background_grid(settings,screen,background_grid)
	#Tworzenie grupy, w której zapisany będzie rysunek
	drawing=Group()
	#Tworzenie ramki
	frame=Group()
	fct.create_frame(screen,settings,frame)
	#Tworzenie przycisków
	buttons=Group()
	fct.create_buttons(screen,settings,buttons)
	#Dodanie zmiennej, która informuje czy mysz jest obecie kliknięta
	mouse_down=False
	while True:
		#Reakcja na klawisze i przyciski
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_down=True
			elif event.type == pygame.MOUSEBUTTONUP:
				mouse_down=False
		if mouse_down==True:
			#Reakcja na kliknięcie i przytrzymanie myszy
			fct.mouse_click(screen,settings,background_grid,drawing,
			buttons,frame)		
		fct.update_screen(screen,drawing,frame,buttons)
run_program()
