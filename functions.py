import pygame
from background import BackgroundCell
from drawing import DrawingElement
from frame import FrameTop,FrameBottom,FrameSide
from pygame.sprite import Sprite
def create_background_grid(settings,screen,background_grid):
	"""Tworzenie w tle niewidzlanej siatki komórek wypełniających całe 
	tło"""
	for collumn in range(5,settings.width_grid_number-5):
		for row in range(5,settings.height_grid_number-10):
			background_cell=BackgroundCell(screen,settings)
			background_cell.rect.left=settings.height_grid*collumn
			background_cell.rect.top=settings.height_grid*row
			background_grid.add(background_cell)
def create_frame(screen,settings,frame):
	"""Tworzenie ramki składającej się z 4 elementów"""
	frame_top=FrameTop(screen,settings)
	frame_bottom=FrameBottom(screen,settings)
	frame_left_side=FrameSide(screen,settings)
	frame_right_side=FrameSide(screen,settings)
	frame_right_side.rect.right=frame_right_side.screen_rect.right
	frame.add(frame_top)
	frame.add(frame_bottom)
	frame.add(frame_left_side)
	frame.add(frame_right_side)
def mouse_click(screen,settings,background_grid,drawing,buttons_group,
frame,color_indicator,eraser_button,reference_grid_button,pointer,
clear_button):
	"""Reakcja na kliknięcie na tło myszą"""
	mouse_x,mouse_y = pygame.mouse.get_pos()
	if pygame.sprite.spritecollideany(pointer,drawing,
	collided=None) and eraser_button.turn_on==True:
		#Jeżeli włączone jest wymazywanie i kliknięty zostanie element 
		#rysunku, kliknięty element zostanie wymazany
		existing_drawing_element=pygame.sprite.spritecollideany(pointer,
		drawing,collided=None)
		existing_drawing_element.kill()
	elif pygame.sprite.spritecollideany(pointer,drawing,collided=None):
		#Jeżeli kliknięty zostanie istniejący element rysunku, zostanie
		#on zastąpiony nowym tylko, jeżeli jego kolor jest inny od 
		#obecnego koloru rysowania
		existing_drawing_element=pygame.sprite.spritecollideany(pointer,
		drawing,collided=None)
		if existing_drawing_element.color!=(
		settings.default_drawing_color):
			drawing_element=DrawingElement(screen,settings,
			settings.default_drawing_color)
			drawing_element.rect.centerx=(
			existing_drawing_element.rect.centerx)
			drawing_element.rect.centery=(
			existing_drawing_element.rect.centery)
			drawing.add(drawing_element)
			existing_drawing_element.kill()
	elif pygame.sprite.spritecollideany(pointer,background_grid,
	collided=None) and eraser_button.turn_on==False:
		#Jeżeli zostanie kliknięte puste tło, zostanie dodany element 
		#rysunku (jeżeli nie jest obecnie włączone wymazywanie)
		pointed_part=pygame.sprite.spritecollideany(pointer,
		background_grid,collided=None)
		drawing_element=DrawingElement(screen,settings,
		settings.default_drawing_color)
		drawing_element.rect.centerx=pointed_part.rect.centerx
		drawing_element.rect.centery=pointed_part.rect.centery
		drawing.add(drawing_element)
	elif eraser_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączanie opcji wymazywania, jeżeli zostanie kliknęty przycisk 
		#gumki
		eraser_button.turn_on=True
	elif reference_grid_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączenie/wyłaczenie siatki pomocniczej.Przy pomocy zmiennej 
		#"enable_changing_grid" siatka zostaje przełączona tylko raz 
		#podczas klikniecia. Dzięki temu siatka nie przełącza się 
		#wielokrotnie przy wciśniętym przycisku
		if (reference_grid_button.button_on==True and 
		settings.enable_changing_grid==True):
			reference_grid_button.button_on=False
			settings.enable_changing_grid=False		
		elif (reference_grid_button.button_on==False and 
		settings.enable_changing_grid==True):
			reference_grid_button.button_on=True
			settings.enable_changing_grid=False
	elif pygame.sprite.spritecollideany(pointer,buttons_group.buttons,
	collided=None):
		#Zmiana domyślnego koloru malowania na ten, który 
		#miał kliknięty przycisk
		button=pygame.sprite.spritecollideany(pointer,
		buttons_group.buttons,collided=None)
		settings.default_drawing_color=button.color
		#Zmiana koloru wskaźnika, który informuje, jaki 
		#kolor jest obecnie używany i wyłączenie wymazywania
		#(jeżeli było aktywne)
		color_indicator.color=settings.default_drawing_color
		eraser_button.turn_on=False
	elif clear_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Czyszczenie całego rysunku
		drawing.empty()
def update_screen(screen,drawing,frame,buttons_group,UI_buttons_group,
reference_grid,reference_grid_button):
	"""Wyświetlenie tła, rysunku, ramki i interfejsu"""
	screen.fill((255,255,255))
	if reference_grid_button.button_on==True:
		for grid_element in reference_grid:
			grid_element.draw_grid_element()
	for frame_element in frame:
		frame_element.draw_frame()
	for drawing_element in drawing:
		drawing_element.draw_cell()
	for button in buttons_group.buttons:
		button.draw_button()
	for button in UI_buttons_group:
		button.draw_button()
	pygame.display.flip()
