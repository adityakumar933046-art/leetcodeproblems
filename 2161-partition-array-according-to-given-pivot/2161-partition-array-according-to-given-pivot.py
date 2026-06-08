class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1=[]
        list3 =[]
        list2 =[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                list1.append(nums[i])

            elif nums[i]==pivot:
                list3.append(nums[i])
            else:
                list2.append(nums[i])

        a= list1 +list3+ list2
        return a

        