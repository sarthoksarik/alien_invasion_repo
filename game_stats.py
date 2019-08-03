class GameStats(object):
	"""track statistics for alien invasion"""
	def __init__(self, ai_game):
		"""initialises statistics."""
		self.settings = ai_game
		self.reset_stats()
	def reset_stats(self):
		"""initializes statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		