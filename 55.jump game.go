func canJump(nums []int) bool {
	farthest := 0
	for i := 0; i < len(nums); i++ {
		if i > farthest {
			return false
		}
		farthest = max(farthest, i+nums[i])
	}
	return true
}