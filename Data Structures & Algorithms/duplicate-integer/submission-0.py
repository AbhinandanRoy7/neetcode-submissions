class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emp=[]
        for i in nums:
            if i not in emp:
                emp.append(i)
        if sorted(emp)==sorted(nums):
            return False
        else :
            return True