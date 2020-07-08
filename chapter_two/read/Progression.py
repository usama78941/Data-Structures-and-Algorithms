class Progression:
    """ Iterator producing a generic progression

    Default iterator pproduces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """initialize current to the first value of progression, 0 by default"""
        self._current = start

    def _advance(self):
        """Update self._current to the new vale

        This should be overriden by a subclass to customize progression.

        By Convention, if current is set to None, this designates the end of a finite Progression
        """

        self._current += 1

    def __next__(self):
        """Return the next element or else StopItertaion error 
        """
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""
        return self

    def print_progression(self, num_terms):
        """print next n values of the progression"""

        # noinspection PyUnusedLocal
        print(' '.join(str(next(self)) for j in range(num_terms)))


class ArithmeticProgression(Progression):
    """Create a new arithmetic progression"""

    def __init__(self, start=0, step=1):
        """Create a new arithmetic progression.

        start   the first term of the progression
        step    teh fixed term of the progression (default 0)
        """
        super().__init__(start)
        self._step = step

    def _advance(self):
        """”Update current value by adding the fixed increment"""
        self._current += self._step


class GeometricProgression(Progression):
    """Create a new arithmetic progression"""

    def __init__(self, start=1, base=2):
        """Create a new arithmetic progression.

        start   the first term of the progression
        base    the fixed constant of the progression (default 0)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value"""
        self._current = self._current * self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression"""

    def __init__(self, first=0, second=1):
        """creates a new fibonacci sequence

        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """

        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of the previous two values"""
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression: ')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)
    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)
    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)
    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)
    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)
    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
