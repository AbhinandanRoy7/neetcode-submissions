class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # emp=sorted(nums)
        # for i in range(1,len(emp)):
        #     if emp[i]==emp[i-1]:
        #         return True
        # return False

        emp=set()
        for i in nums:
            if i in emp: 
                return True
            emp.add(i)
        return False
            