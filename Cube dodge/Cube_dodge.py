import pygame
import os
import sys
import time
import random

# Makes pygame window always open on the same coordinates
x = 100
y = 45
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
player_color = (255,0,0)
player_pos = [width/2,550]
player_size = 50
background_color = (0,0,0)
obstacles_color = (0,150,0)
obstacles_size = player_size
obstacles_pos=[random.randint(0,750),-50]
obstacles_speed=10
score = 0
font1 = pygame.font.SysFont("monospace",30)


game_over = False

# Hold key repeat setting
pygame.key.set_repeat(1)

# Create a clock object to set a frame limit
clock = pygame.time.Clock()

# Collision detect
def detect_collision(obstacle_list):
	for i in obstacle_list:
		if i[1]+obstacles_size >= player_pos[1]:
			if i[0] >= player_pos[0]-50 and i[0] <= player_pos[0]+player_size:
				return True

# Populates a list with positions for the obstacles. 10 positions max
# Delay create to randomize the spawn rate
# x_pos randomized
obstacle_list = []
def draw_obstacle(obstacle_list):
	delay = random.random()
	if len(obstacle_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,750)
		y_pos = -50
		obstacle_list.append([x_pos,y_pos])

# Create the obstacles with the coordinates from obstacle_list
def drop_obstacle(obstacle_list):
	for i in obstacle_list:
		pygame.draw.rect(screen,obstacles_color,(i[0],i[1],obstacles_size,
			obstacles_size))

# Fall speed and aceleration
def obstacle_fall(obstacle_list):
	global obstacles_speed
	global score
	for i in obstacle_list:
		if i[1] >= -50 and i[1] < height:
			i[1] += obstacles_speed
			obstacles_speed += 0.001
		else:
			obstacle_list.pop(0)
			score += 1
			print(score)

# Movement keys detect
# Game main loop
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if player_pos[0] >= 10:
					player_pos[0] -= 10
				
			elif event.key == pygame.K_RIGHT:
				if player_pos[0] <= 740:
					player_pos[0] += 10

	screen.fill(background_color)

	if detect_collision(obstacle_list):
		game_over = True

	draw_obstacle(obstacle_list)
	drop_obstacle(obstacle_list)
	obstacle_fall(obstacle_list)
	
# Create red player
	pygame.draw.rect(screen, player_color,(player_pos[0],player_pos[1],
		player_size,player_size))

# Shows score
	text1 = "Score: " + str(score)
	label1 = font1.render(text1,1,(255,255,255))
	screen.blit(label1,(width-200,height-40))


# Control frames limit for fall speed
	clock.tick(30)

	pygame.display.update()
	


	

