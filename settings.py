class Settings():
	def __init__(self):
		"""Podstawowe ustanienia programu; rozmiar komórek składających
		sie na tło ekranu jest skalowany na podstawie preferowanego
		rozmiaru ekranu i liczby komórek"""
		#Parametry ekranu
		self.screen_height=650
		self.screen_width=1300
		#Parametry niewidzialnego tła; obliczanie szerokości i wysokości
		#komórek, z kórych będzie składało się niewidzialne tło
		self.width_grid_number=200
		self.height_grid_number=100
		#Proporjce są minimalnie zawiększone, żeby (przy ustawianiu
		#położenia) zaokrąglenia wartości nie skutkowały pustymi
		#odstępami między komórkami
		self.width_grid=self.screen_width/self.width_grid_number
		self.height_grid=self.screen_height/self.height_grid_number
		#Ustalenie koloru ramki
		self.frame_color=(100,100,100)
		#Domyślny kolor rysowania
		self.default_drawing_color=(0,0,0)
		#Proporjce odległości w jakiej będa się znajdowały linie 
		#tworzące pomocniczą siatkę
		self.reference_grid_size=5
		#Dodanie zmiennej, blokujacej stałe włącanie i wyłączanie siatki
		#przy przytrzymanym przycisku
		self.enable_changing_grid=True
		
