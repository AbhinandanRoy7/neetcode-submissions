class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[]
        for i in nums:
            if i != val:
                res.append(i)
                # print(i)
        # nums=[i for i in nums if i not in res]
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)