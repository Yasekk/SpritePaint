import pygame
from background import BackgroundCell
from drawing import DrawingElement
from frame import FrameTop,FrameBottom,FrameSide
from UI_buttons import (BlackButton,BlueButton,RedButton,GreenButton,
ColorIndicator,YellowButton,CyanButton,MagentaButton,GrayButton,
BrownButton)
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
def create_buttons(screen,settings,buttons):
	"""Tworzenie przycisków, które będą określały kolor rysowania"""
	black_button=BlackButton(screen,settings)
	buttons.add(black_button)
	blue_button=BlueButton(screen,settings)
	buttons.add(blue_button)
	red_button=RedButton(screen,settings)
	buttons.add(red_button)
	green_button=GreenButton(screen,settings)
	buttons.add(green_button)
	yellow_button=YellowButton(screen,settings)
	buttons.add(yellow_button)
	cyan_button=CyanButton(screen,settings)
	buttons.add(cyan_button)
	magenta_button=MagentaButton(screen,settings)
	buttons.add(magenta_button)
	gray_button=GrayButton(screen,settings)
	buttons.add(gray_button)
	brown_button=BrownButton(screen,settings)
	buttons.add(brown_button)
def mouse_click(screen,settings,background_grid,drawing,buttons,frame,
color_indicator,eraser_button,reference_grid_button):
	"""Reakcja na kliknięcie na tło myszą"""
	mouse_x,mouse_y = pygame.mouse.get_pos()
	if eraser_button.rect.collidepoint(mouse_x,mouse_y)==True:
		#Włączanie opcji wymazywania, jeżeli zostanie kliknęty przycisk 
		#gumki
		eraser_button.turn_on=True
	for background_cell in background_grid:
		#Program sprawdza, który element niewidzialnej siatki odpowiada
		#aktualnemu położeniu klikniętej myszy
		if background_cell.rect.collidepoint(mouse_x,mouse_y)==True:
			#Sprawdzenie czy w aktualnym położeniu nie ma już rysunku
			make_new=True
			for existing_drawing_element in drawing:
				if existing_drawing_element.rect.collidepoint(mouse_x,
				mouse_y)==True:
					#Usunięcie elementu rysunku, jeżeli włączone jest
					#wymazywanie. Pominięcie dalszego rysowania, jeżeli
					#w wybranym miejscu juz znajduje sie element rysunku
					#lub zastąpienie elementu nowym, jeżeli rysujemy w 
					#innym kolorze
					make_new=False
					if eraser_button.turn_on==True:
						existing_drawing_element.kill()
						break
					elif existing_drawing_element.color!=(
					settings.default_drawing_color):
						drawing_element=DrawingElement(screen,settings,
						settings.default_drawing_color)
						drawing_element.rect.centerx=(
						background_cell.rect.centerx)
						drawing_element.rect.centery=(
						background_cell.rect.centery)
						drawing.add(drawing_element)
						existing_drawing_element.kill()
						break
			if make_new==True and eraser_button.turn_on==False:
				#Utworzenie elementu rysunku, który będzie miał takie 
				#samo położenie jak pozycja kursora
				drawing_element=DrawingElement(screen,settings,
				settings.default_drawing_color)
				drawing_element.rect.centerx=(
				background_cell.rect.centerx)
				drawing_element.rect.centery=(
				background_cell.rect.centery)
				drawing.add(drawing_element)
	for frame_part in frame:
		#Jezeli nastapi kliknięcie na przycisk siatki, siatka zostanie
		#włączona lub wyłączona
		if reference_grid_button.rect.collidepoint(mouse_x,mouse_y)==True:
			#Przy pomocy zmiennej "enable_changing_grid" siatka zostaje
			#przełączona tylko raz podczas klikniecia. Dzięki temu 
			#siatka nie przełącza się wielokrotnie przy wciśniętym 
			#przycisku
			if reference_grid_button.button_on==True and settings.enable_changing_grid==True:
				reference_grid_button.button_on=False
				settings.enable_changing_grid=False
				break
			elif reference_grid_button.button_on==False and settings.enable_changing_grid==True:
				reference_grid_button.button_on=True
				settings.enable_changing_grid=False
				break
		#Jeżeli nastąpi kliknięcie na fragment ramki, program sprawdzi,
		#czy kliknięty został jeden z przycisków koloru
		elif frame_part.rect.collidepoint(mouse_x,mouse_y)==True:
			for button in buttons:
				if button.rect.collidepoint(mouse_x,mouse_y)==True:
					#Zmiana domyślnego koloru malowania na ten, który 
					#miał kliknięty przycisk
					settings.default_drawing_color=button.color
					#Zmiana koloru wskaźnika, który informuje, jaki 
					#kolor jest obecnie używany i wyłączenie wymazywania
					#(jeżeli było aktywne)
					color_indicator.color=settings.default_drawing_color
					eraser_button.turn_on=False
					break
def update_screen(screen,drawing,frame,buttons,color_indicator,
eraser_button,reference_grid_button,reference_grid):
	"""Wyświetlenie tła, rysunku, ramki i interfejsu"""
	screen.fill((255,255,255))
	if reference_grid_button.button_on==True:
		for grid_element in reference_grid:
			grid_element.draw_grid_element()
	for frame_element in frame:
		frame_element.draw_frame()
	for drawing_element in drawing:
		drawing_element.draw_cell()
	for button in buttons:
		button.draw_button()
	color_indicator.draw_indicator()
	eraser_button.draw_eraser()
	reference_grid_button.draw_button()
	pygame.display.flip()
