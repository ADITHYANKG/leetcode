class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_count = -1
        best_divisor = float('inf')

        for divisor in divisors:
            count = sum(1 for num in nums if num % divisor == 0)

            if count > max_count or (count == max_count and divisor < best_divisor):
                max_count = count
                best_divisor = divisor

        return best_divisor

      
