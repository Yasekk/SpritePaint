import pygame
from background import BackgroundCell
from drawing import DrawingElement,DrawingRectangle
from frame import FrameTop,FrameBottom,FrameSide
from pygame.sprite import Sprite
import json
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
clear_button,save_button,load_button,rectangle_button,rectangles,
drawing_button):
	"""Reakcja na kliknięcie na tło myszą"""
	mouse_x,mouse_y = pygame.mouse.get_pos()
	if pygame.sprite.spritecollideany(pointer,background_grid,
	collided=None) and settings.active_button=="rectangle":
		#Jeżeli włączony jest tryb rysowania prostokątów, miejsce 
		#kliknięcia na planszy będzie tworzyło jeden z rogów prostokąta 
		#a przeciwległy róg będzie podażał za kursoerm
		if len(rectangles)<=0:
			#Upewnienie się, że w jednym momencie aktywny jest tylko 
			#jeden prostokąt
			drawing_rectangle=DrawingRectangle(screen,settings,
			settings.default_drawing_color,mouse_x,mouse_y)
			rectangles.add(drawing_rectangle)
	elif pygame.sprite.spritecollideany(pointer,drawing,
	collided=None) and settings.active_button=="eraser":
		#Jeżeli włączone jest wymazywanie i kliknięty zostanie element 
		#rysunku, kliknięty element zostanie wymazany
		erase_drawing_element(pointer,drawing)
	elif pygame.sprite.spritecollideany(pointer,drawing,collided=None
	) and settings.active_button=="draw":
		#Jeżeli kliknięty zostanie istniejący element rysunku, zostanie
		#on zastąpiony nowym tylko, jeżeli jego kolor jest inny od 
		#obecnego koloru rysowania
		replace_drawing_element(pointer,drawing,screen,settings)
	elif pygame.sprite.spritecollideany(pointer,background_grid,
	collided=None) and settings.active_button=="draw":
		#Jeżeli zostanie kliknięte puste tło, zostanie dodany element 
		#rysunku (jeżeli zwykłe rysowanie jest obecnie aktywne)
		create_drawing_element(pointer,background_grid,screen,settings,
		drawing)
	elif eraser_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączanie opcji wymazywania, jeżeli zostanie kliknęty przycisk 
		#gumki
		settings.active_button="eraser"
	elif reference_grid_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączenie/wyłaczenie siatki pomocniczej. Przy pomocy zmiennej 
		#"enable_changing_grid" siatka zostaje przełączona tylko raz 
		#podczas klikniecia. Dzięki temu siatka nie przełącza się 
		#wielokrotnie przy wciśniętym przycisku
		if (reference_grid_button.button_on==True and 
		settings.enable_changing_grid==True):
			#Wyłączenie siatki
			reference_grid_button.button_on=False
			settings.enable_changing_grid=False		
		elif (reference_grid_button.button_on==False and 
		settings.enable_changing_grid==True):
			#Włączenie siatki
			reference_grid_button.button_on=True
			settings.enable_changing_grid=False
	elif pygame.sprite.spritecollideany(pointer,buttons_group.buttons,
	collided=None):
		#Zmiana domyślnego koloru malowania na ten, który 
		#odpowiadał klikniętemu przyciskowi
		button=pygame.sprite.spritecollideany(pointer,
		buttons_group.buttons,collided=None)
		settings.default_drawing_color=button.color
		#Zmiana koloru wskaźnika, który informuje, jaki 
		#kolor jest obecnie używany
		color_indicator.color=settings.default_drawing_color
	elif clear_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Czyszczenie całego rysunku
		drawing.empty()
	elif save_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Zapisanie rysunku do pliku
		with open("picture.json","w") as drawing_save:
			#Tworzenie lub czyszczenie pliku "picture.json" i tworzenie 
			#pustej listy, w której przechowane będą dane do zapisu
			drawing_data=[]
		for drawing_element in drawing:
			#Zapisywanie informacji o położeniu i kolorze kazdego 
			#elementu rysunku
			drawing_element_data=[]
			drawing_element_data.append(drawing_element.rect.center)
			drawing_element_data.append(drawing_element.color)
			drawing_data.append(drawing_element_data)
		with open("picture.json","a") as drawing_save:
			#Dodawanie informacji do pliku
			json.dump(drawing_data,drawing_save)
	elif load_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Wczytanie rysunku z pliku
		with open("picture.json","r") as drawing_load:
			#Usuwanie obecnego rysunku
			drawing.empty()
			#Wczytywanie infomacji o elementach zapisanego rysunku i 
			#tworzenie nowych elementów o takich samych parametrach
			drawing_data=json.load(drawing_load)
			for drawing_element_data in drawing_data:
				drawing_element=DrawingElement(screen,
				settings,drawing_element_data[1])
				drawing_element.rect.center=drawing_element_data[0]
				drawing.add(drawing_element)
	elif rectangle_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączenie trybu rysowania prostokątów
		settings.active_button="rectangle"
	elif drawing_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączenie trybu zwykłego rysowania
		settings.active_button="draw"
def erase_drawing_element(pointer,drawing):
	"""Wymazanie klikniętego elementu"""
	existing_drawing_element=pygame.sprite.spritecollideany(pointer,
	drawing,collided=None)
	existing_drawing_element.kill()
def replace_drawing_element(pointer,drawing,screen,settings):
	"""Zastąpienie elementu rysunku nowym jeżeli rysujemy innym kolorem
	"""
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
def create_drawing_element(pointer,background_grid,screen,settings,
drawing):
	"""Dodawanie nowego elementu rysunku"""
	pointed_part=pygame.sprite.spritecollideany(pointer,
	background_grid,collided=None)
	drawing_element=DrawingElement(screen,settings,
	settings.default_drawing_color)
	drawing_element.rect.centerx=pointed_part.rect.centerx
	drawing_element.rect.centery=pointed_part.rect.centery
	drawing.add(drawing_element)
def drawing_rectangle(background_grid,rectangles,drawing,screen,
settings):
	"""Zamiana roboczego prostokąta we fagment rysunku"""
	covered_part=pygame.sprite.groupcollide(background_grid,rectangles,
	False,False,collided=None)
	#Upewnienie sie ze obrazek sie nie nawarstwi z poprzednim rysunkiem
	pygame.sprite.pygame.sprite.groupcollide(rectangles,drawing,False,
	True)
	for part in covered_part:	
		drawing_element=DrawingElement(screen,settings,
		settings.default_drawing_color)
		drawing_element.rect.centerx=part.rect.centerx
		drawing_element.rect.centery=part.rect.centery
		drawing.add(drawing_element)
	rectangles.empty()	
def update_screen(screen,drawing,frame,buttons_group,UI_buttons_group,
reference_grid,reference_grid_button,rectangles):
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
	for rectangle in rectangles:
		rectangle.draw_rectangle()
	pygame.display.flip()
