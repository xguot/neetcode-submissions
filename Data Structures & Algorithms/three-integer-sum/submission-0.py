class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(0, len(nums) - 2):
            # Prevent duplicated triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                t = nums[i] + nums[l] + nums[r] 

                if t < 0:
                    l += 1

                elif t > 0:
                    r -= 1

                else:
                    ans.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r < l and nums[r] == nums[r+1]:
                        r += 1

                    l += 1
                    r -= 1
        
        return ans

                    
