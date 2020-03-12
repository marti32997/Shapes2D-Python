import pytest

from ..src.circle import Circle


def test_calculate_area():
	a_circle = Circle("Circle", True, 5, 5, 2)
	assert a_circle.calculate_area() == 12.56
