class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Edge case 0"""

        ans = []
        p = 1
        n_0 = 1
        cnt_0 = len(nums)
        for n in nums:
            p *= n
            if n != 0:
                n_0 *= n
                cnt_0 -= 1

        for i in range(0, len(nums)):
            if nums[i] == 0:
                if cnt_0 > 1:
                    ans.append(0)
                else:
                    ans.append(n_0)
            else:
                tmp = p / nums[i]
                ans.append(int(tmp))
                

        return ans
            