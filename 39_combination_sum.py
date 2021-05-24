class Solution:
    results: List[List[int]] = []
    candidates: List[List[int]] = []
    target: int = 0

    def backtrack(self, currentIndex: int, currentSum: int, choosen: List[int]):
        if (self.target - currentSum == 0):
            self.results.append(choosen)
            return
        if ((self.target - currentSum < 0) or (currentIndex >= len(self.candidates))):
            return

        # it means the current sum is still not the target
        # there are a couple of options:
        # 1. maintain the current index of candidates to add this candidate to the list of choosen elements
        self.backtrack(currentIndex, currentSum +
                       self.candidates[currentIndex], choosen + [self.candidates[currentIndex]])
        # 2. go to the next index of candidates
        self.backtrack(currentIndex + 1, currentSum, choosen)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.candidates = candidates
        self.target = target
        self.backtrack(0, 0, [])
        return self.results
