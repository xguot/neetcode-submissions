class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = sorted(list(set(nums)))
        ans = 1
        tmp = 1

        for i in range(1, len(a)):
            if a[i] == a[i-1] + 1:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1

        return max(ans, tmp)