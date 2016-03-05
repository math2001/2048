import pygame
from pygame.locals import *
from couleur import *

pygame.init()

class Keyboard:
	def __init__(self):
		pass

	def check(self):
		for e in pygame.event.get():
			if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE): return "end"
			if e.type == KEYDOWN:
				if e.key == K_UP: return 'up'
				elif e.key == K_DOWN: return "down"
				elif e.key == K_LEFT: return "left"
				elif e.key == K_RIGHT: return "right"