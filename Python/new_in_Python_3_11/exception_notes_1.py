import math

try:
    math.sqrt(-1)
except ValueError as e:
    e.add_note('Negative value passed! Please try again.')
    raise