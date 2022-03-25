class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersec_list =[]
        for i in nums1:
            if i in nums2:
                intersec_list.append(i)
        return set(intersec_list)
                
        