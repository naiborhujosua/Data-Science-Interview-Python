def nextGreaterElement(nums1,nums2):

    answer ={}
    result =[nums2[0]]

    for i in range(1,len(nums2)):
        while result and nums2[i] > result[-1]:
            answer[result.pop()] = nums2[i]

        result.append(nums2[i])

    for key in result:
        answer[key] =-1

    return  [answer[key] for key in nums1]


