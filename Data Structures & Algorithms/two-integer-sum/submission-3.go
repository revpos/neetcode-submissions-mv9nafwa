func twoSum(nums []int, target int) []int {
    nums_map := make(map[int]int)

    for i, n := range nums {
        complement := target - n
        
        if idx, found := nums_map[complement]; found {
            return []int{idx, i}
        }

        nums_map[n] = i
    }
    return []int{}
}
