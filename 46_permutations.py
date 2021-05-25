class Solution:
    results: List[List[int]] = []

    def generateAllPermutations(self, nums: List[int], numsToBeUsed: List[int]):
        if (len(numsToBeUsed) == 0):
            self.results.append(nums)

        for i in range(0, len(numsToBeUsed)):
            self.generateAllPermutations(
                nums + [numsToBeUsed[i]], numsToBeUsed[:i] + numsToBeUsed[i+1:])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.generateAllPermutations([], nums)
        return self.results
