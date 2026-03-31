class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # have a pointer that points to leftmost and then have two pointers
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                   
        return output
                    #[-4,0,1,1,2,3]
                    #[i,   l,    r]
