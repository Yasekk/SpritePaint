import pygame
from background import BackgroundCell
from drawing import DrawingElement
def create_background_grid(settings,screen,background_grid):
	"""Tworzenie w tle niewidzlanej siatki komórek wypełniających całe 
	tło"""
	for collumn in range(settings.width_grid_number):
		for row in range(settings.height_grid_number):
			background_cell=BackgroundCell(screen,settings)
			background_cell.rect.left=settings.height_grid*collumn
			background_cell.rect.top=settings.height_grid*row
			background_grid.add(background_cell)
def mouse_click(screen,settings,background_grid,drawing):
	"""Reakcja na kliknięcie na tło myszą"""
	mouse_x,mouse_y = pygame.mouse.get_pos()
	for background_cell in background_grid:
		#Program sprawdza, który element niewidzialnej siatki został
		#kliknięty
		if background_cell.rect.collidepoint(mouse_x,mouse_y):
			#Utworzenie elementu rysunku, który będzie miał takie samo
			#położenie jak kliknięty element siatki
			drawing_element=DrawingElement(screen,settings)
			drawing_element.rect.centerx=background_cell.rect.centerx
			drawing_element.rect.centery=background_cell.rect.centery
			drawing.add(drawing_element)
def update_screen(screen,drawing):
	"""Wyświetlenie rysunku oraz białego tła"""
	screen.fill((255,255,255))
	for drawing_element in drawing:
		drawing_element.draw_cell()
	pygame.display.flip()
