import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

pygame.init()

class Render(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.font = pygame.font.Font('font/ahronbd.ttf', 50)

	def set_structure(self, structure):
		self.structure = structure

	def get_color(self, color):
		if color == 2:
			return 190, 190, 190
		elif color == 4:
			return 240, 236, 96
		elif color == 8:
			return 240, 171, 96
		elif color == 16:
			return 255, 74, 21
		else:
			return white

	def render(self):
		if self.structure != []:
			top = 0
			for ligne in self.structure:
				left = 0
				for case in ligne:
					if case == 0:
						case = ""
					text = self.font.render(str(case), True, black)
					text_rect = text.get_rect()

					fond = pygame.Surface((100, 100))
					fond.fill( self.get_color(case) )
					fond_rect = fond.get_rect(top=top, left=left)
					pygame.draw.rect(self.screen, (51, 51, 51), fond_rect, 5)

					text_rect.center = fond_rect.center

					self.screen.blit(fond, fond_rect)
					self.screen.blit(text, text_rect)
					left += 100
				top += 100
