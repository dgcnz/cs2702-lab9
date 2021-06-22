from sklearn import datasets
from typing import List
from numpy.linalg import norm


class IrisDataset:
    data = []
    target = []

    def __init__(self):
        iris = datasets.load_iris()
        self.data = iris['data']
        self.target = iris['target']

    def bounded_nearest_neighbors(self, i: int, threshold: float) -> List[int]:
        # Returns list of indices of all objects with euclidean
        # distance less than threshold
        # Complexity: O(n)
        u = self.data[i]
        ans = []
        for j, v in enumerate(self.data):
            if j != i and norm(v - u) <= threshold:
                ans.append(j)
        return ans

    def k_nearest_neighbors(self, i: int, k: float) -> List[int]:
        # Returns list of indices k nearest neighbors
        # Complexity: O(n log n)
        u = self.data[i]
        ans = []

        for j, _ in range(len(self.data)):
            if j != i:
                ans.append(j)
        ans.sort(key=lambda v: norm(v - u))
        return ans[:k]

    def precision(self, i: int, candidates: List[int]) -> float:
        return sum(1 if self.target[j] == self.target[i] else 0
                   for j in candidates) / len(candidates)


def main():
    iris = IrisDataset()
    c = iris.bounded_nearest_neighbors(0, 0.4)
    p = iris.precision(0, c)


if __name__ == '__main__':
    main()
