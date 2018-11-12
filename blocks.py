from pygame import *

PLATFORM_W = 32
PLATFORM_H = 32
PLATFORM_COLOR = "#FF6262"

class Platform(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = Surface((PLATFORM_H,PLATFORM_W))
		self.image = image.load("textures/blocks/platform.png")
		self.rect = Rect(x, y, PLATFORM_W, PLATFORM_H)