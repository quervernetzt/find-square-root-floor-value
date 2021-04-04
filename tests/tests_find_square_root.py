import unittest
from solution.find_square_root import FindSquareRoot

class TestCasesFindSquareRoot(unittest.TestCase):
    def negative_input_should_return_none(self: object) -> None:
        # Arrange
        find_square_root: FindSquareRoot = FindSquareRoot()

        # Act
        square_root: int = find_square_root.main(-3)

        # Assert
        self.assertIsNone(square_root)
    
    def zero_should_return_zero(self: object) -> None:
        # Arrange
        find_square_root: FindSquareRoot = FindSquareRoot()

        # Act
        square_root: int = find_square_root.main(0)

        # Assert
        self.assertEqual(square_root, 0)
    
    def positive_input_should_return_positive_integer(self: object) -> None:
        # Arrange
        find_square_root: FindSquareRoot = FindSquareRoot()

        # Act
        square_root_0: int = find_square_root.main(1)
        square_root_1: int = find_square_root.main(2)
        square_root_2: int = find_square_root.main(3)
        square_root_3: int = find_square_root.main(4)
        square_root_4: int = find_square_root.main(5)

        # Assert
        self.assertEqual(square_root_0, 1)
        self.assertEqual(square_root_1, 1)
        self.assertEqual(square_root_2, 1)
        self.assertEqual(square_root_3, 2)
        self.assertEqual(square_root_4, 2)
    
    def large_positive_input_should_return_positive_integer(self: object) -> None:
        # Arrange
        find_square_root: FindSquareRoot = FindSquareRoot()

        # Act
        square_root: int = find_square_root.main(12325352340)

        # Assert
        self.assertEqual(square_root, 111019)
    
    def positive_float_input_should_return_positive_integer(self: object) -> None:
        # Arrange
        find_square_root: FindSquareRoot = FindSquareRoot()

        # Act
        square_root: int = find_square_root.main(5.5)

        # Assert
        self.assertEqual(square_root, 2)