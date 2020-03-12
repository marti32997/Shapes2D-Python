from .shapes2D import Shapes2D
from .point import Point


class Circle(Shapes2D):
	def __init__(self, name, warp_space, x, y, r):
		super().__init__(name, warp_space)
		self.center = Point(x, y)
		self.r = r
		self.area = self.calculate_area()
		self.all_points_in_shape = self.get_all_points_in_shape()
		self.all_points_on_shape = self.get_all_points_on_shape()

	def calculate_area(self):
		return self.r ** 2 * 3.14

	def is_point_in_shape(self, x, y):
		within_X_range = bool(x > self.center.x - self.r and x < self.center.x + self.r)
		within_Y_range = bool(y > self.center.y - self.r and y < self.center.y + self.r)
		if within_X_range and within_Y_range:
			return True

	def is_point_on_shape(self, x, y):
		top = bool(y == self.center.y + self.r and x == self.center.x)
		right = bool(x == self.center.x + self.r and y == self.center.y)
		bottom = bool(y == self.center.y - self.r and x == self.center.x)
		left = bool(x == self.center.x - self.r and y == self.center.y)

		if top or bottom or right or left:
			return True

	def get_all_points_in_shape(self):
		all_points_in_shape = []
		for x in range(self.center.x - self.r + 1, self.center.x + self.r):
			for y in range(self.center.y - self.r + 1, self.center.y + self.r):
				if self.is_point_in_shape(x, y):
					all_points_in_shape.append(Point(x, y))

		return all_points_in_shape

	def get_all_points_on_shape(self):
		all_points_on_shape = []
		for x in range(self.center.x - self.r, self.center.x + self.r + 1):
			for y in range(self.center.y - self.r, self.center.y + self.r + 1):
				if self.is_point_on_shape(x, y):
					all_points_on_shape.append(Point(x, y))

		return all_points_on_shape

	def __str__(self):
		if self.warp_space:
			shape_type = "WS"
		else:
			shape_type = "NS"
		lines = f"{self.name}, {shape_type}, {self.area}, Center: ({self.center.x}, {self.center.y}), Radius : {self.r}"
		lines += "\nAll Points in Shape : "
		for point in self.all_points_in_shape:
			lines += f"({point.x},{point.y}) "
		lines += "\nAll Points on Shape : "
		for point in self.all_points_on_shape:
			lines += f"({point.x},{point.y}) "
		return lines