class Solution:
    def search(self, N: List[int], T: int) -> int:
        l, r = 0, len(N) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if N[mid] == T:
                return mid
            elif N[mid] > T:
                r = mid - 1
            else:
                l = mid + 1

        return -1


