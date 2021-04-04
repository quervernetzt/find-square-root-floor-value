from tests.tests_find_square_root import TestCasesFindSquareRoot
from solution.find_square_root import FindSquareRoot

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_find_square_root: TestCasesFindSquareRoot = TestCasesFindSquareRoot()

    tests_find_square_root.negative_input_should_return_none()
    tests_find_square_root.zero_should_return_zero()
    tests_find_square_root.positive_input_should_return_positive_integer()
    tests_find_square_root.large_positive_input_should_return_positive_integer()
    tests_find_square_root.positive_float_input_should_return_positive_integer()

    ###################################
    # Demo
    ###################################
    find_square_root: FindSquareRoot = FindSquareRoot()
    result: int = find_square_root.main(9)
    print(result) # 3