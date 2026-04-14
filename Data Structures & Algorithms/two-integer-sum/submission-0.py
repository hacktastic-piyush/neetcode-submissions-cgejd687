class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last = []
        for i in range(0, len(nums)):
            for j in range(1,len(nums)):
                if i==j:
                    continue
                else:
                    temp = nums[i]+nums[j]
                    if temp==target:
                        return [i,j]