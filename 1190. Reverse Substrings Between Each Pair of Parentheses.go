package leetgoat

func reverseParantheses(s string) string {
	stack := []string{""}
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, "")
		} else if s[i] == ')' {
			current := stack[len(stack)-1]
			stack := stack[:len(stack)-1]

			runes := []rune(current)
			for l, r := 0, len(runes)-1; l < r; l, r = l+1, r-1 {
				runes[l], runes[r] = runes[r], runes[l]
			}
			stack[len(stack)-1] += string(runes)
		} else {
			stack[len(stack)-1] += string(s[i])
		}
	}
	return stack[0]
}
