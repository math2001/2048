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

structure = [
	[0, 2, 0, 2],
	[0, 0, 0, 8],
	[4, 0, 0, 0],
	[0, 0, 0, 2]
]

move = Move(structure)
keyboard = Keyboard()
render = Render()
cont = True
while cont:
	game_lose = True
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

	while game_lose:
		if keyboard.check() == "end":
			game_lose = False
		run_game_lose(screen)


print 'QUIT'
pygame.quit()