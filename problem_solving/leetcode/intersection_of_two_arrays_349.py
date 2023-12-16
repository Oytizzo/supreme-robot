# Link
# https://leetcode.com/problems/intersection-of-two-arrays/description/

# Solution 1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in result:
                    result.add(n1)
        return result


# Solution 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dc=defaultdict(lambda:0)
        for a in nums1:
            dc[a]=1
        nums2=set(nums2)
        for a in nums2:
            if(dc[a]==1):
                ans.append(a)
        return ans