class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max = r_max = 0

        left_maxes = [0] * len(height)
        l_max = 0
        for i in range(len(height)):
            l_max = max(l_max, height[i])
            left_maxes[i] = l_max

        right_maxes = [0] * len(height)
        r_max = 0
        for i in range(len(height)-1, -1, -1):
            r_max = max(r_max, height[i])
            right_maxes[i] = r_max

        water = 0
        for i in range(len(height)):
            water += max(min(left_maxes[i], right_maxes[i]) - height[i], 0)

        return water