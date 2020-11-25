from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    def __init__(self, target:int, searchSpace:[int]):
        self._searchSpace = searchSpace
        self._currentIndex = 0
        self._solutions = []
        self._target = target

    def bruteForceSolution(self):
        candidate = self.first()
        while(self.isSearching()):
            if self.isValid(candidate):
                self.updateSolution(candidate)
            candidate = self.next()
        return self._solutions

    def first(self) -> int:
        return self._searchSpace[0]

    def next(self) -> int:
        self._currentIndex += 1
        if self.isSearching():
            return self._searchSpace[self._currentIndex]

    def isSearching(self) -> bool:
        return self._currentIndex < len(self._searchSpace)

    @abstractmethod
    def isValid(self, candidate) -> bool:
        pass

    @abstractmethod
    def updateSolution(self, candidate):
        pass

class EqualitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        return self._target == candidate

    def updateSolution(self, candidate):
        self._solutions.append(candidate)

class DivisibilitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        return candidate % self._target == 0

    def updateSolution(self, candidate):
        self._solutions.append(candidate)

class MinimumSearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        if (len(self._solutions) == 0):
            self._solutions.append(candidate)
        elif self._solutions[0] > candidate:
            return True
        return False

    def updateSolution(self, candidate):
        self._solutions[0] = candidate

def main():
    test1 = MinimumSearchAlgorithm(None, [-1,12,23,34,12,10,9,-3,4,5,3])
    print(test1.bruteForceSolution())

    test2 = DivisibilitySearchAlgorithm(2, [12,12,23,34,12,10,9,5,4,5,3])
    print(test2.bruteForceSolution())

    test2 = EqualitySearchAlgorithm(12, [12,12,23,34,12,10,9,5,4,5,3])
    print(test2.bruteForceSolution())

if __name__ == "__main__":
    main()