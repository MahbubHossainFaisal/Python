class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        nums3=[]

        while(i!= m and j!=n):
            
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
            

        if i!=m:
            while i!=m:
                nums3.append(nums1[i])
                i+=1
        if j!=n:
            while j!=n:
                nums3.append(nums2[j])
                j+=1

        for i in range(m+n):
            nums1[i] = nums3[i]
        