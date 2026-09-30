class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i, numero in enumerate(nums):
            complemento = target - numero

            if complemento in vistos:
                return [vistos[complemento], i]

            vistos[numero] = i
        
        return