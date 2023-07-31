# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.the_area())
rect.set_width(3)
print(rect.the_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.the_area())
sq.set_side(4)
print(sq.the_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)