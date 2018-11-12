import pygame
from pygame import *
from player import *
from blocks import *

#Объявляем переменные
WIN_WIDTH = 1280 #Ширина создаваемого окна
WIN_HEIGHT = 720 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 

#информация для блоков 



def main():
	
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("my mario") 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))      
    bg = pygame.image.load('bg.jpg')
    hero = Pleyer(55,55) # создаем героя по (x,y) координатам
    left = right = False # по умолчанию - стоим
    up= False
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)



    level = [
       "----------------------------------------",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-              -                       -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-                                      -",
       "-       -    -----                     -",
       "-                                --    -",
       "-                     --         --    -",
       "-                     --         --    -",
       "-                     --         --    -",
       "----------------------------------------"]

    x=y=0
    for row in level:
    	for col in row:
    		if col == "-":
    			pf = Platform(x,y)
    			entities.add(pf)
    			platforms.append(pf)
    		x += PLATFORM_W
    	y += PLATFORM_H
    	x = 0
	

    while 1:
    	timer.tick(60)
    	for e in pygame.event.get(): 
    		if e.type == QUIT:
    			raise SystemExit
    		if e.type == KEYDOWN and e.key == K_LEFT:
    			left = True
    		if e.type == KEYDOWN and e.key == K_RIGHT:
    			right = True
    		if e.type == KEYUP and e.key == K_RIGHT:
    			right = False
    		if e.type == KEYUP and e.key == K_LEFT:
    			left = False
    		if e.type == KEYDOWN and e.key == K_SPACE:
    			up = True
    		if e.type == KEYUP and e.key == K_SPACE:
    			up = False
    	screen.blit(bg, (0,0))      

    	hero.update(left, right,up, platforms)
    	entities.draw(screen)
    	pygame.display.update()
        

if __name__ == "__main__":
    main()