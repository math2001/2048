import pygame
from pygame.locals import *
from couleur import *

from Tools import list_print
from Move import Move
from Keyboard import Keyboard
from Render import Render
from Game import run_game_lose

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('2048')

font = pygame.font.Font('font/ahronbd.ttf', 50)


move = Move()
move.generate_structure()
keyboard = Keyboard()
render = Render()
cont = True
game_lose = False
while cont:
	screen.fill(h333)
	key = keyboard.check()
	
	if key == "down":
		move.down()
	elif key == "up":
		move.up()
	elif key == "left":
		move.left()
	elif key == "right":
		move.right()
	elif key == "end":
		cont = False
	if key in ("down", "up", "left", "right"): 
		if not move.add_nb():
			game_lose = True

	render.set_structure(move.get())
	render.render()

	pygame.display.flip()

	fg_color = [255, 255, 255]
	bg_color = [0, 0, 0]
	value = 1

	while game_lose:
		if keyboard.check() in ("end", 'other_key', 'click'):
			game_lose = False
			move.generate_structure()
		fg_color, bg_color, value = run_game_lose(screen, font, fg_color, bg_color, value)
		pygame.time.wait(5)
		pygame.display.flip()


print 'QUIT'
pygame.quit()