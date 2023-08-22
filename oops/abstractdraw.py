from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    #abstract method draw
class Rectangle(Shape):
    def draw(self):
        print(f"drawing {self.name}")

rec=Rectangle("rectangle")
rec.draw()