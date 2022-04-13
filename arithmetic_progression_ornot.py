class Solution:
    def canMakeArithmeticProgression(arr: list[int]) -> bool:

        arr.sort(reverse=True)
        d = arr[1] - arr[0]
        
        for i in range(1, len(arr) - 1):
            if arr[i+1] != arr[i] + d:
                return False
        return True

print(Solution.canMakeArithmeticProgression([3,5,1]))