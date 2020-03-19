import pytest

from ..src.circle import Circle


@pytest.fixture
def a_circle():
	a_circle = Circle("Circle", True, 4, 5, 3)
	return a_circle


def test_calculate_area(a_circle):
	assert a_circle.calculate_area() == 28.26


def test_is_point_in_shape(a_circle):
	assert a_circle.is_point_in_shape(2, 3)
	assert a_circle.is_point_in_shape(2, 4)
	assert a_circle.is_point_in_shape(2, 5)
	assert a_circle.is_point_in_shape(2, 6)
	assert a_circle.is_point_in_shape(2, 7)

	assert a_circle.is_point_in_shape(3, 3)
	assert a_circle.is_point_in_shape(3, 4)
	assert a_circle.is_point_in_shape(3, 5)
	assert a_circle.is_point_in_shape(3, 6)
	assert a_circle.is_point_in_shape(3, 7)

	assert a_circle.is_point_in_shape(4, 3)
	assert a_circle.is_point_in_shape(4, 4)
	assert a_circle.is_point_in_shape(4, 5)
	assert a_circle.is_point_in_shape(4, 6)
	assert a_circle.is_point_in_shape(4, 7)

	assert a_circle.is_point_in_shape(5, 3)
	assert a_circle.is_point_in_shape(5, 4)
	assert a_circle.is_point_in_shape(5, 5)
	assert a_circle.is_point_in_shape(5, 6)
	assert a_circle.is_point_in_shape(5, 7)

	assert a_circle.is_point_in_shape(6, 3)
	assert a_circle.is_point_in_shape(6, 4)
	assert a_circle.is_point_in_shape(6, 5)
	assert a_circle.is_point_in_shape(6, 6)
	assert a_circle.is_point_in_shape(6, 7)


def test_is_point_on_shape(a_circle):
	assert a_circle.is_point_on_shape(4, 8)
	assert a_circle.is_point_on_shape(7, 5)
	assert a_circle.is_point_on_shape(4, 2)
	assert a_circle.is_point_on_shape(1, 5)
