import pygame
from pygame.locals import *
from couleur import *

pygame.init()

def run_game_lose(screen, font):

	bg_color = [0, 0, 0]
	fg_color = [255, 255, 255]

	srect = screen.get_rect()

	while bg_color[1] < 255 and fg_color[1] > 0:

		screen.fill(bg_color)

		text = font.render('Game OVER', 1, fg_color)
		trect = text.get_rect(center=srect.center)

		screen.blit(text, trect)

		for i in range(len(bg_color)):
			bg_color[i] += 1
			fg_color[i] -= 1



		pygame.time.wait(20)
		pygame.display.flip()

