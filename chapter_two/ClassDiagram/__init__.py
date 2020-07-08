class Goat(object):
    def __init__(self, tail):
        self._tail = tail

    def milk(self):
        pass

    def jump(self):
        pass


class Pig(object):
    def __init__(self, nose):
        self._nose = nose

    def eat(self, food):
        pass

    def wallow(self):
        pass


class Horse(object):
    def __init__(self, height, color):
        self._height = height
        self._color = color

    def run(self):
        pass

    def jump(self):
        pass


class Racer(Horse):

    def __init__(self, height, color):
        super().__init__(height, color)

    def race(self):
        pass


class Equestrian(Horse):
    def __init__(self, height, color, weight):
        super().__init__(height, color)
        self._weight = weight

    def trot(self):
        pass

    def is_trained(self):
        pass
