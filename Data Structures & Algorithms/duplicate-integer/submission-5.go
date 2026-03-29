func hasDuplicate(nums []int) bool {
    unique_nums := make(map[int]struct{}, len(nums))
    for _, n := range nums {
        if _, exists := unique_nums[n]; exists {
            return true
        }
        unique_nums[n] = struct{}{}
    }
    return false
}
