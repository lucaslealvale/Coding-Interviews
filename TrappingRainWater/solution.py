class Solution:
    def trap(self, height: list[int]) -> int:
        chuva = 0
        for i in range(len(height)):
            margem_e = 0
            margem_d = 0
            for j in range(i):
                if height[j] > margem_e:
                    margem_e = height[j]
            for j in range(i+1, len(height)):
                if height[j] > margem_d:
                    margem_d = height[j]
            if margem_e > height[i] and margem_d > height[i]:
                chuva += min(margem_e, margem_d) - height[i]
        return chuva
