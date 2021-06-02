class Solution:
    minJumps: int = 0
    def recursiveJump (self, nums: List[int], currentIndex: int, jumps: int) -> int:
        if (currentIndex >= (len(nums)-1)):
            if (self.minJumps > jumps):
                self.minJumps = jumps
            return
        
        #we already found a better solution
        if (jumps >= self.minJumps):
            return
        
        #we are stuck
        if (nums[currentIndex] == 0):
            return
        
        #we have nums[currentIndex] options
        maxSum = currentIndex + nums[currentIndex]
        maxId = currentIndex
        for i in range(nums[currentIndex], 0, -1):    
            self.recursiveJump(nums, currentIndex + i, jumps + 1)
            
    def greedyAlgorithm(self, nums: List[int]) -> int:
        lastIndex = len(nums) - 1
        jumps = 0
        while (lastIndex > 0):
            for i in range(0, lastIndex):
                if (i + nums[i] >= lastIndex):
                    lastIndex = i
                    jumps += 1
                    break
        return jumps
    
    def jump(self, nums: List[int]) -> int:
        #self.minJumps = len(nums) - 1
        #self.recursiveJump (nums, 0, 0)
        #return self.minJumps
        return self.greedyAlgorithm(nums)
