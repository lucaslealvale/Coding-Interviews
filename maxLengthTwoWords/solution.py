class Solution:
    
    def maxProduct(self, words: list[str]) -> int:
        max_product = 0
        words = sorted(words)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
                    break
        return max_product

        