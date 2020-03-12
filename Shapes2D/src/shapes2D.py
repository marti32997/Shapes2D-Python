from abc import ABC, abstractmethod


class Shapes2D(ABC):
	def __init__(self, name, warp_space):
		self.name = name
		self.warp_space = warp_space

	@abstractmethod
	def calculate_area(self):
		pass

	@abstractmethod
	def is_point_in_shape(self):
		pass

	@abstractmethod
	def is_point_on_shape(self):
		pass

	@abstractmethod
	def get_all_points_in_shape(self):
		pass

	@abstractmethod
	def get_all_points_on_shape(self):
		pass

	@abstractmethod
	def __str__(self):
		pass
