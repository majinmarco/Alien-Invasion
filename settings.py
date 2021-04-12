class Settings:
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's static settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (0, 250, 0)
		self.bullets_allowed = 5

		# Alien settings
		self.fleet_drop_speed = 10
		
		# How quickly the game speeds up
		self.speedup_scale = 1.4

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initlialize_dynamic_settings()

	def initlialize_dynamic_settings(self):
		"""Initialize dynamic settings for the game."""
		self.ship_speed = 5
		self.star_speed = 5
		self.star_density = 40 # Less is more
		self.bullet_speed = 3
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and point values."""
		self.ship_speed*=self.speedup_scale
		self.bullet_speed*=self.speedup_scale
		self.alien_speed*=self.speedup_scale
		self.star_speed*=self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)