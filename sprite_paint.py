"""Główny moduł programu."""

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
import functions as fct
from UI_buttons import (ColorIndicator, EraserButton,
                        ReferenceGridButton, ClearButton, ButtonsGroup,
                        SaveButton, LoadButton, RectangleButton,
                        DrawingButton)
from tools import (VerticalReferenceGrid, HorizontalReferenceGrid,
                   Pointer)
from drawing import DrawingElement

def run_program():
	"""Inicjalizacja programu i wczytywanie początkowych wartości."""
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width,
                                     settings.screen_height))
	pygame.display.set_caption("Sprite Painter")
	#Tworzenie w tle niewidzlanej siatki komórek.
	background_grid = Group()
	fct.create_background_grid(settings, screen, background_grid)
	#Tworzenie grupy, w której zapisany będzie rysunek.
	drawing = Group()
	#Tworzenie ramki.
	frame = Group()
	fct.create_frame(screen, settings, frame)
	#Tworzenie siatki, którą będzie mozna włączać w celu ułatwienia 
	#rysowania.
	reference_grid = Group()
	for collumn_number in range(int(settings.width_grid_number
	                                / settings.reference_grid_size)):
		vertical_reference_grid = VerticalReferenceGrid(screen,
		                                                settings)
		vertical_reference_grid.rect.centerx = (
		    (collumn_number+1)
		    * settings.width_grid
		    * settings.reference_grid_size)
		reference_grid.add(vertical_reference_grid)
	for row_number in range(int(settings.height_grid_number
	                            / settings.reference_grid_size)):
		horizontal_reference_grid = HorizontalReferenceGrid(screen,
		                                                    settings)
		horizontal_reference_grid.rect.centery = (
		    (row_number+1)
		    * settings.height_grid
		    * settings.reference_grid_size)
		reference_grid.add(horizontal_reference_grid)	
	#Dodanie zmiennej, która informuje czy mysz jest obecie kliknięta.
	mouse_down = False
	#Tworzenie grupy przycisków kolorów.
	buttons_group = ButtonsGroup(screen, settings)
	#Tworzneie grupy przycisków dodatkowych.
	UI_buttons_group = Group()
	#Dodanie wskaźnika, który pokazuje obecnie używany kolor.
	color_indicator = ColorIndicator(screen, settings)
	UI_buttons_group.add(color_indicator)
	#Dodanie przycisku, który pozwoli na wymazywanie elementów rysunku.
	eraser_button = EraserButton(screen, settings)
	UI_buttons_group.add(eraser_button)
	#Dodanie przycisku, który pozwoli na wyświetlenie siatki pomagającej
	#w rysowaniu.
	reference_grid_button = ReferenceGridButton(screen, settings)
	UI_buttons_group.add(reference_grid_button)
	#Dodanie przycisku, który pozwoli na usunięcie całego rysunku.
	clear_button = ClearButton(screen, settings)
	UI_buttons_group.add(clear_button)
	#Dodanie przycisku, który pozwoli na zapisywanie obrazu.
	save_button = SaveButton(screen, settings)
	UI_buttons_group.add(save_button)
	#Dodanie przycisku, który pozwoli na wczytywanie obrazu.
	load_button = LoadButton(screen, settings)
	UI_buttons_group.add(load_button)
	#Dodanie przycisku, który pozwoli na rysowanie prostokątów.
	rectangle_button = RectangleButton(screen, settings)
	UI_buttons_group.add(rectangle_button)
	#Dodanie przycisku, który pozwoli na zwykłe rysowanie.
	drawing_button = DrawingButton(screen, settings)
	UI_buttons_group.add(drawing_button)
	#Dodanie niewidzialnego kwadratu, który bedzie odpowiadał położeniu
	#kursora i będzie tworzył rysunki w miejscu kliknięcia.
	pointer = Pointer(screen, settings)
	#Dodanie grupy w której będą tymczasowe figury.
	rectangles = Group()
	while True:
		#Ustalenie lub odświeżenie pozycji kursora.
		mouse_x, mouse_y = pygame.mouse.get_pos()
		pointer.rect.centerx = mouse_x
		pointer.rect.centery = mouse_y
		#Reakcja na klawisze i przyciski.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#Włączenie trybu klikniętej myszy.
				mouse_down = True
			elif event.type == pygame.MOUSEBUTTONUP:
				#Wyłączenie trybu klikniętej myszy.
				mouse_down = False
				#Zmiana wartości zmiennej, dzięki czemu po odkliknięciu
				#myszy bdzie można ponownie wcisnąć przycisk siatki 
				#pomocniczej dopiero przy nasetpnym kliknięciu.
				settings.enable_changing_grid = True
				#Jeżeli aktualnie tworzona jest figura, aktualnie 
				#ustalony kształt zostanie dodany do rysunku.
				if len(rectangles) >= 0:
					fct.drawing_rectangle(background_grid, rectangles,
					                      drawing, screen, settings)						
		if mouse_down == True:
			#Reakcja na kliknięcie i przytrzymanie myszy
			fct.mouse_click(screen, settings, background_grid, drawing,
			                buttons_group, frame, color_indicator,
			                eraser_button, reference_grid_button,
			                pointer, clear_button, save_button,
			                load_button, rectangle_button, rectangles,
			                drawing_button)		
		fct.update_screen(screen, drawing, frame, buttons_group,
		                  UI_buttons_group, reference_grid,
		                  reference_grid_button, rectangles)

run_program()
