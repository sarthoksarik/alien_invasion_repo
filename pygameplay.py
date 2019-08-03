import pygame

pygame.init()

screen = pygame.display.set_mode((300,300))

flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			flag = False