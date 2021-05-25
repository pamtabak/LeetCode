class Solution:
    results: List[List[int]] = []
    candidates: List[List[int]] = []
    target: int = 0
    
        
    def backtrack(self, currentIndex: int, currentSum: int, chosen: List[int]):
        if (self.target - currentSum == 0):
            chosen = sorted(chosen)
            if (chosen not in self.results):
                self.results.append(chosen)
            return
        if ((self.target - currentSum < 0) or (currentIndex >= len(self.candidates))):
            return
        
        # we need to check if it is still possible to make it to the target
        # if we sum the current sum with all the candidates still available and that still doesnt add up to the target, we can return
        maxSum = currentSum
        for i in range(currentIndex, len(self.candidates)):
            maxSum += self.candidates[i]
        if (maxSum < self.target):
            return

        # we can only add each candidate once
        # so there are two options: add it exactly once or dont add it
        self.backtrack(currentIndex + 1 , currentSum +
                       self.candidates[currentIndex], chosen + [self.candidates[currentIndex]])
        # 2. go to the next index of candidates
        self.backtrack(currentIndex + 1, currentSum, chosen)
    
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.candidates = candidates
        self.target = target
        self.backtrack(0, 0, [])
        return self.results