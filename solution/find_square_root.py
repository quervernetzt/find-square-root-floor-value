class FindSquareRoot(object):
    def __init__(self) -> None:
        """Constructor.
        """
        pass

    def main(self: object, number: int) -> int:
        """Main method to find square root of integer in O(log(n)) time.

            Parameters
            ----------
            number : int, required
                Number to get the square root of.
            
            Returns
            ----------
            int
                Returns the integer that either is the square root or where itself squared comes closest.
        """
        if number < 0:
            return None

        x: int = number
        y: int  = (x + 1) // 2

        while y < x:
            x = y
            y = (x + number // x) // 2

        return x