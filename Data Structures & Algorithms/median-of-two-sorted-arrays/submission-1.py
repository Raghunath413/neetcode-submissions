
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        nums = [0] * (m + n)
        index1 = 0
        index2 = 0
        index = 0

        while index1 < m and index2 < n:
            if nums1[index1] < nums2[index2]:
                nums[index] = nums1[index1]
                index1 += 1
            else:
                nums[index] = nums2[index2]
                index2 += 1
            index += 1

        while index1 < m:
            nums[index] = nums1[index1]
            index += 1
            index1 += 1

        while index2 < n:
            nums[index] = nums2[index2]
            index += 1
            index2 += 1

        mid = (m + n) // 2

        if (m + n) % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2

        return nums[mid]
