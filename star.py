import pygame
from pygame.sprite import Sprite

from random import randint

class Star(Sprite):
	
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings	

		# Load the star image and set its rect attribute.

		self.image = pygame.image.load(f'images/star{randint(1,3)}.bmp')
		self.rect = self.image.get_rect()

		# Start a new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the star's exact horizontal position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Return True if star is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Move star down"""
		self.y+= (self.settings.star_speed)
		self.rect.y = self.y
