from numbers import Number

from utils.calculator import Calculator


class CalculationError(Exception):
    pass


class CalculationService:
    """Calculation service provides calculations using Calculator.
    If no specific Calculator injected via constructor then a default instance will be used
    """

    def __init__(self, calculator: Calculator | None = None) -> None:
        self.calculator = calculator if calculator else Calculator()

    def supported_operations(self) -> set[str]:
        return self.calculator.supported_math_operations()

    def calculate(self, args: list, operations: list) -> Number:
        self._validate_calc_params(args, operations)
        self._validate_math_operations(operations)

        top_pr_ops = self.calculator.top_priority_math_ops()
        top_pr_op_count = len([x for x in operations if x in top_pr_ops])

        args_ = args.copy()
        ops_ = operations.copy()

        # apply top pr operations first
        io = 0
        while io < len(ops_) and top_pr_op_count > 0:
            op = ops_[io]
            if op in top_pr_ops:
                res = self.calculator.calculate(op, *args_[io:io + 2])
                del ops_[io]
                del args_[io + 1]
                args_[io] = res
                top_pr_op_count -= 1
            else:
                io += 1

        # apply rest operations
        while len(ops_) > 0:
            res = self.calculator.calculate(ops_[0], *args_[0:2])
            del ops_[0]
            del args_[1]
            args_[0] = res

        return args_[0]

    def _validate_calc_params(self, args, operations):
        if len(args) != len(operations) + 1:
            raise CalculationError("Incorrect amount of arguments and math operations")

    def _validate_math_operations(self, operations):
        math_ops = self.calculator.supported_math_operations()
        if not set(operations) <= math_ops:
            raise CalculationError(
                f"Found not supported math operations: {set(operations) - math_ops}"
            )

