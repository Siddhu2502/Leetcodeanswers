class Solution:
    def findDuplicate(nums: list[int]) -> int:
        # reccuring number 
        
        rnum = {}
        for num in nums:
            if num in rnum:
                return num
            else:
                rnum[num] = 0
     
 
list1 = [10, 20, 10, 30, 40, 40]
print(Solution.findDuplicate(list1))