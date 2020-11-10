import pygame
from background import BackgroundCell
from drawing import DrawingElement
from frame import FrameTop,FrameBottom,FrameSide
from UI_buttons import BlackButton,BlueButton,RedButton,GreenButton
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
def mouse_click(screen,settings,background_grid,drawing,buttons,frame):
	"""Reakcja na kliknięcie na tło myszą"""
	mouse_x,mouse_y = pygame.mouse.get_pos()
	for background_cell in background_grid:
		#Program sprawdza, który element niewidzialnej siatki odpowiada
		#aktualnemu położeniu klikniętej myszy
		if background_cell.rect.collidepoint(mouse_x,mouse_y)==True:
			#Sprawdzenie czy w aktualnym położeniu nie ma już rysunku
			make_new=True
			for drawing_element in drawing:
				if drawing_element.rect.collidepoint(mouse_x,
				mouse_y)==True:
					make_new=False
			if make_new==True:
				#Utworzenie elementu rysunku, który będzie miał takie 
				#samo położenie jak pozycja kursora
				drawing_element=DrawingElement(screen,settings,settings.default_drawing_color)
				drawing_element.rect.centerx=(
				background_cell.rect.centerx)
				drawing_element.rect.centery=(
				background_cell.rect.centery)
				drawing.add(drawing_element)
	for frame_part in frame:
		#Jeżeli nastąpi kliknięcie na fragment ramki, program sprawdzi,
		#czy kliknięty został jeden z przycisków koloru
		if frame_part.rect.collidepoint(mouse_x,mouse_y)==True:
			for button in buttons:
				if button.rect.collidepoint(mouse_x,mouse_y)==True:
					#Zmiana domyślnego koloru malowania na ten, który 
					#miał kliknięty przycisk
					settings.default_drawing_color=button.color
def update_screen(screen,drawing,frame,buttons):
	"""Wyświetlenie rysunku oraz białego tła"""
	screen.fill((255,255,255))
	for frame_element in frame:
		frame_element.draw_frame()
	for drawing_element in drawing:
		drawing_element.draw_cell()
	for button in buttons:
		button.draw_button()
	pygame.display.flip()
