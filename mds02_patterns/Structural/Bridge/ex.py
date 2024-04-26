from abc import ABC, abstractmethod
from enum import Enum


class TypeShape(Enum):
    circle = "circle"
    square = "square"


class Drawing(ABC):
    @abstractmethod
    def draw_shape(self, shape: TypeShape, x, y):
        pass


class DrawingRed(Drawing):
    def draw_shape(self, shape: TypeShape, x, y):
        print(f"Drawing {shape.value} at {x}, {y} in red")


class DrawingBlue(Drawing):
    def draw_shape(self, shape: TypeShape, x, y):
        print(f"Drawing {shape.value} at {x}, {y} in blue")


class Shape(ABC):
    def __init__(self, x, y, drawing: Drawing):
        self.x = x
        self.y = y
        self.drawing = drawing

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        self.drawing.draw_shape(TypeShape.circle, self.x, self.y)


class Square(Shape):
    def draw(self):
        self.drawing.draw_shape(TypeShape.square, self.x, self.y)


if __name__ == "__main__":

    drawing_red = DrawingRed()
    drawing_blue = DrawingBlue()

    circle = Circle(1, 2, drawing_red)
    circle.draw()

    square = Square(3, 4, drawing_blue)
    square.draw()
