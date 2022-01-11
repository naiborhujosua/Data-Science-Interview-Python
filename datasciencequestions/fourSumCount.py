from collections import defaultdict
def fourSumCount(nums1,nums2,nums3,nums4):
    result,counter =0,defaultdict(int)

    for i in range(len(nums1)):
        for j in range(len(nums1)):
            counter[nums1[i]+nums2[j]] +=1

    for i in range(len(nums3)):
        for j in range(len(nums3)):
            result += counter[-(nums3[i]+nums4[j])]

    return result

