class Solution:
    def maxArea(self, H: List[int]) -> int:
        A, l, r = 0, 0, len(H) - 1

        while l < r:
            a = min(H[l], H[r])*(r - l)
            A = max(A, a)

            if H[l] > H[r]:
                r -= 1
            else:
                l += 1
        
        return A