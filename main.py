from typing import Dict

class Stats:
    def __init__(self, built: Dict[int, int], min: int, max: int, size: int):
        self.__built = built
        self.__min = min
        self.__max = max
        self.__size = size
    
    def less(self, number: int) -> int:
        if number <= self.__min:
            return 0
        elif number > self.__max:
            return self.__size
        else:
            return self.__built[number - 1]

    def greater(self, number: int) -> int:
        if number < self.__min:
            return self.__size
        elif number >= self.__max:
            return 0
        else:
            return self.__size - self.__built[number]

    def between(self, lower: int, upper: int):
        return self.less(upper + 1) - self.less(lower)

class DataCapture:
    def __init__(self):
        self.__items : Dict[int, int] = {}
        self.__max : int = 0
        self.__min : int = 1000
        self.__size : int = 0

    def add(self, number):
        self.__items.setdefault(number, 0)
        self.__items[number] += 1
        if number > self.__max: 
            self.__max = number
        if number < self.__min: 
            self.__min = number
        self.__size += 1

    def build_stats(self) -> Stats:
        acumulative : int = 0
        built : Dict[int, int] = {}
        for i in range(self.__min, self.__max):
            built[i] = self.__items.get(i, 0) + acumulative
            acumulative += self.__items.get(i, 0)
        return Stats(built, self.__min, self.__max, self.__size)


def main(values: list, less: int, lower: int, upper: int, greater: int):
    capture = DataCapture()
    for value in values:
        capture.add(value)
    stats = capture.build_stats()
    return stats.less(less), stats.between(lower, upper), stats.greater(greater)

values = [11, 12]
less = 15
lower = 5
upper = 8
greater = 10
less, between, greater = main(values, less, lower, upper, greater)
print(less, between, greater)