import math
from numbers import Number
from typing import Callable


class Calculator:

    def __init__(self):
        self.__math_operations: dict[str:Callable] = {}
        self.__top_priority_math_ops: set[str] = set()
        self.__register_base_math_ops()

    def supported_math_operations(self) -> set[str]:
        """
        Get list of supported math operation signs
        :return: List of signs string representation
        """
        return set(self.__math_operations.keys())

    def top_priority_math_ops(self) -> set[str]:
        """
        Get list of math operation signs with higher execution priority
        :return: List of signs string representation
        """
        return self.__top_priority_math_ops

    def _register_math_operation(
            self,
            sign: str,
            func: Callable,
            is_top_priority: bool = False
    ):
        """
        Register math operation sign and map an executor to it.
        If you need to extend the class - use this method in your inherited class __init__() method
        to add additional functionality
        :param sign: string representing a math operation sign, like '+', '-' etc.
        :param func: Method to execute to apply the operation
        :param is_top_priority: boolean flag indicating that this type of operation has first
        priority and should be executed in first order
        :return: result of the math operation
        """
        self.__math_operations[sign] = func
        if is_top_priority:
            self.__top_priority_math_ops.add(sign)

    def __register_base_math_ops(self):
        self._register_math_operation('+', lambda v1, v2: v1 + v2)
        self._register_math_operation('-', lambda v1, v2: v1 - v2)
        self._register_math_operation('*', lambda v1, v2: v1 * v2, True)
        self._register_math_operation('/', lambda v1, v2: v1 / v2 if v2 != 0 else math.nan, True)

    def calculate(
            self,
            math_op: str,
            val1: int,
            val2: int
    ) -> Number:
        if math_op in self.__math_operations:
            return self.__math_operations.get(math_op)(val1, val2)
        else:
            raise NotImplementedError(f"{math_op} operation is not supported!")


class CalculatorExtended(Calculator):

    def __init__(self):
        super().__init__()
        self._register_math_operation('^', lambda v1, v2: v1 ** v2, True)
