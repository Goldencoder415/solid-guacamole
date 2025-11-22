"""Small Circle class example.

This file defines a `Circle` class that uses `__init__` to set the radius,
and provides `area()` and `perimeter()` methods. A minimal CLI/example
is provided under the usual `if __name__ == '__main__'` guard.
"""

from math import pi
from typing import Union


class Circle:
    def __init__(self, radius: Union[int, float]):
        """Initialize a circle with the given radius (must be positive)."""
        r = float(radius)
        if r <= 0:
            raise ValueError("radius must be positive")
        self.radius = r

    def area(self) -> float:
        """Return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


def _read_radius_from_arg_or_input(arg: Union[None, str]) -> float:
    """Helper: parse radius from optional arg or prompt the user."""
    if arg is None or arg.strip() == "":
        raw = input("Enter radius: ").strip()
    else:
        raw = arg
    return float(raw)


if __name__ == "__main__":
    import sys

    # Usage examples:
    #   python main.py            # prompts for radius
    #   python main.py 3.5        # uses 3.5 as radius

    arg = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        radius = _read_radius_from_arg_or_input(arg)
        c = Circle(radius)
    except Exception as exc:  # keep it simple for this tiny script
        print(f"Error: {exc}")
        sys.exit(1)

    print(f"Radius    : {c.radius}")
    print(f"Area      : {c.area():.6f}")
    print(f"Perimeter : {c.perimeter():.6f}")
