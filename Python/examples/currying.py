from collections.abc import Callable


def multiply_setup(a: float) -> Callable:
    def multiply(b: float) -> float:
        return a * b

    return multiply


double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(10))
print(triple(10))
