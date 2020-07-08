class Range:
    """A class taht mimic's the built in range class"""

    def __init__(self, start, stop=None, step=1):
        """Initialize a range instance

        Semantics is similar to the buil-in range class
        """

        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge f start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """return the number of entries in the range"""
        return self._length

    def __getitem__(self, k):
        """return the entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not (k <= 0 or k < self._length):
            raise IndexError('index out of range')

        return self._start + k * self._step
