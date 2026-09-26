package main

import (
	"fmt"
	"strings"
)

func countAndSay(n int) string {
	s := "1"
	for iteration := 2; iteration <= n; iteration++ {
		var result strings.Builder
		for i := 0; i < len(s); {
			j := i
			for j < len(s) && s[j] == s[i] {
				j++
			}
			fmt.Fprintf(&result, "%d%c", j-i, s[i])
			i = j
		}
		s = result.String()
	}
	return s
}
