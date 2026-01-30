from typing import Union

Number = Union[int, float]


def _check_numeric(values, message: str) -> None:
    """
    Checks whether every item in `values` is an int/float.
    Raises ValueError with `message` if any value is invalid.
    """
    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(message)


def fun1(x: Number, y: Number) -> Number:
    """
    Adds two numbers together.
    """
    _check_numeric((x, y), "Both inputs must be numbers.")
    return x + y


def fun2(x: Number, y: Number) -> Number:
    """
    Subtracts y from x.
    """
    _check_numeric((x, y), "Both inputs must be numbers.")
    return x - y


def fun3(x: Number, y: Number) -> Number:
    """
    Multiplies two numbers together.
    """
    _check_numeric((x, y), "Both inputs must be numbers.")
    return x * y


def fun4(x: Number, y: Number, z: Number) -> Number:
    """
    Adds three numbers together.
    """
    _check_numeric((x, y, z), "All three inputs must be numbers.")
    return x + y + z


# f1_op = fun1(2, 3)
# f2_op = fun2(2, 3)
# f3_op = fun3(2, 3)
# f4_op = fun4(f1_op, f2_op, f3_op)
