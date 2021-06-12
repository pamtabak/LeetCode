class Solution:
    def quadraticSolution(self, nums: List[int]) -> int:
        largestSum = math.pow(-2, 31) #min int
        for i in range(0, len(nums)):
            currentSum = 0
            for j in range(i, len(nums)):
                currentSum += nums[j]
                if (currentSum > largestSum):
                    largestSum = currentSum
        return largestSum
        
    def kadaneAlgorithm (self, nums: List[int]) -> int:
        largestSum = math.pow(-2, 31) #min int
        currentSum = 0
        for n in nums:
            if currentSum < 0:
                currentSum = 0
                
            currentSum += n
            largestSum = max(largestSum, currentSum)
        return largestSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadaneAlgorithm(nums)
