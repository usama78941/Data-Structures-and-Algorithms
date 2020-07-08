class SequenceIterator:
    """An iterator for any of Python's Sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._sequence = sequence
        self._current_index = -1

    def __next__(self):
        """Return the next element or raise StopIteration error"""
        self._current_index += 1
        if self._current_index < len(self._sequence):
            return self._sequence[self._current_index]
        else:
            raise StopIteration()

    def _iter__(self):
        """by convention, an iterator must return itself as an iterator"""
        return self
