import pygame
from pygame.locals import *
from couleur import *

pygame.init()

def run_game_lose(screen, font, fg_color, bg_color, value):

	srect = screen.get_rect()

	screen.fill(bg_color)

	text = font.render('Game OVER', 1, fg_color)
	trect = text.get_rect(center=srect.center)

	screen.blit(text, trect)

	for i in range(len(bg_color)):
		bg_color[i] += value
		fg_color[i] -= value

		if bg_color[i] >= 255 or bg_color[i] <= 0:
			value = -value
	return fg_color, bg_color, value

