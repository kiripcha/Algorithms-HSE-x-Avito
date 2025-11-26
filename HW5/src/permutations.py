from typing import List
from src.tracer import trace


class Solution:
    @trace
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        возвращает все возможные перестановки элементов
        выбираем элемент, рекурсивно переставляем остаток.
        """
        if not nums:
            return [[]]

        result = []
        for i in range(len(nums)):
            curr = nums[i]
            rest = nums[:i] + nums[i + 1 :]

            for p in self.permute(rest):
                result.append([curr] + p)

        return result


def permutations(nums: List[int]) -> List[List[int]]:
    return Solution().permute(nums)