class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        n = (n1 + n2)
        i, j = 0, 0
        idx2 = n // 2
        idx1 = idx2 - 1
        cnt = 0
        ind1el = ind2el = -1

        while (i < n1 and j < n2):
            if nums1[i] < nums2[j]:
                if cnt == idx1:
                    ind1el = nums1[i]
                if cnt == idx2:
                    ind2el = nums1[i]
                i += 1
            else:
                if cnt == idx1:
                    ind1el = nums2[j]
                if cnt == idx2:
                    ind2el = nums2[j]
                j += 1
            cnt += 1
        
        while j < n2:
            if cnt == idx1:
                ind1el = nums2[j]
            if cnt == idx2:
                ind2el = nums2[j]
            j += 1
            cnt += 1
        
        while i < n1:
            if cnt == idx1:
                ind1el = nums1[i]
            if cnt == idx2:
                ind2el = nums1[i]
            i += 1
            cnt += 1
        
        if n % 2 == 1:
            return float(ind2el)
        else:
            return (ind1el + ind2el) / 2.0
        
            
                