class Solution:
    nodes = set()
    resultLists = []

    def lstToStr(self, nums: List[int]):
        lstStr = ""
        for n in nums:
            lstStr += str(n)
        return lstStr

    def generateAllPermutations(self, nums: List[int], numsToBeUsed: List[int]):
        if (len(numsToBeUsed) == 0):
            self.resultLists.append(nums)

        numsStr = self.lstToStr(nums)
        if (numsStr in self.nodes):
            # it means there are duplicates in the array and we've already seen this node
            return

        self.nodes.add(numsStr)

        for i in range(0, len(numsToBeUsed)):
            self.generateAllPermutations(
                nums + [numsToBeUsed[i]], numsToBeUsed[:i] + numsToBeUsed[i+1:])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nodes = set()
        self.resultLists = []
        self.generateAllPermutations([], nums)
        return self.resultLists
