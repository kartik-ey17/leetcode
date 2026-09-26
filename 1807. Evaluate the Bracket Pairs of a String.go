package main

import (
	"strings"
)

func evaluate(s string, knowledge [][]string) string {
	knowledgeMap := make(map[string]string)

	for _, pair := range knowledge {
		knowledgeMap[pair[0]] = pair[1]
	}
	var res strings.Builder
	for i := 0; i < len(s); {
		if s[i] == '(' {
			j := i + 1
			for s[j] != ')' {
				j++
			}
			key := s[i+1 : j]
			if value, exists := knowledgeMap[key]; exists {
				res.WriteString(value)
			} else {
				res.WriteByte('?')
			}
			i = j + 1
		} else {
			res.WriteByte(s[i])
			i++
		}
	}
	return res.String()
}
