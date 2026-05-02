# Maximum Distance Between a Pair of Values
# Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
# Output: 2
# Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
# The maximum distance is 2 with pair (2,4).

def maximum(nums1, nums2):
    i = j = 0
    ans = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:   
            ans = max(ans, j - i)
            j += 1
        else:
            i += 1

    return ans

nums1=[55,30,5,4,2]
nums2=[100,20,10,10,5]
print(maximum(nums1,nums2))