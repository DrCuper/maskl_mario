from pygame import *
import pyganim
import os

MOVE_SPEED = 7
WIDTH = 100
HEIGHT = 100
COLOR = "#888888"
JUMP_POWER = 19
GRAVITY = 1
ANIMATION_DELAY = 0.1 # скорость смены кадров
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/mario/r1.png' % ICON_DIR),
			('%s/mario/r2.png' % ICON_DIR),
			('%s/mario/r3.png' % ICON_DIR),
			('%s/mario/r4.png' % ICON_DIR),
			('%s/mario/r5.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
            ('%s/mario/l2.png' % ICON_DIR),
            ('%s/mario/l3.png' % ICON_DIR),
            ('%s/mario/l4.png' % ICON_DIR),
            ('%s/mario/l5.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/textures/muvs/st.png' % ICON_DIR, 0.1)]




class Pleyer(sprite.Sprite):
	def __init__ (self, x, y):
		sprite.Sprite.__init__(self)
		self.xvel = 0
		self.stertX = x
		self.stertY = y
		self.yvel = 0
		self.onGround = False
		self.image = Surface((WIDTH,HEIGHT))
		self.image.fill(Color(COLOR))
		self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
		self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
#        Анимация движения вправо
		boltAnim = []
		for anim in ANIMATION_RIGHT:
			boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimRight = pyganim.PygAnimation(boltAnim)
		self.boltAnimRight.play()
#        Анимация движения влево        
		boltAnim = []
		for anim in ANIMATION_LEFT:
			boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
		self.boltAnimLeft.play()
		
		self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
		self.boltAnimStay.play()
		self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим
		
		self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
		self.boltAnimJumpLeft.play()
		
		self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
		self.boltAnimJumpRight.play()
		
		self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
		self.boltAnimJump.play()

	def update(self, left, right ,up, platforms):
		if up:
			if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
				self.yvel = -JUMP_POWER
			self.image.fill(Color(COLOR))
			self.boltAnimJump.blit(self.image, (0, 0))
			   
					   
		if left:
			self.xvel = -MOVE_SPEED # Лево = x- n
			self.image.fill(Color(COLOR))
			if up: # для прыжка влево есть отдельная анимация
				self.boltAnimJumpLeft.blit(self.image, (0, 0))
			else:
				self.boltAnimLeft.blit(self.image, (0, 0))
 
		if right:
			self.xvel = MOVE_SPEED # Право = x + n
			self.image.fill(Color(COLOR))
			if up:
				self.boltAnimJumpRight.blit(self.image, (0, 0))
			else:
				self.boltAnimRight.blit(self.image, (0, 0))
		 
		if not(left or right): # стоим, когда нет указаний идти
			self.xvel = 0
			if not up:
				self.image.fill(Color(COLOR))
				self.boltAnimStay.blit(self.image, (0, 0))
			
		if not self.onGround:
			self.yvel +=  GRAVITY
			
		self.onGround = False; # Мы не знаем, когда мы на земле((   
		self.rect.y += self.yvel
		self.collide(0, self.yvel, platforms)

		self.rect.x += self.xvel # переносим свои положение на xvel
		self.collide(self.xvel, 0, platforms)

	def collide(self,xvel,yvel,platforms):
		for p in platforms:
			if sprite.collide_rect(self, p):

				if xvel > 0 :
					self.rect.right = p.rect.left

				if xvel < 0 :
					self.rect.left = p.rect.right

				if yvel > 0 :
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0

				if yvel < 0 :
					self.rect.top = p.rect.bottom
					self.yvel = 0