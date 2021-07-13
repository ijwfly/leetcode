package main

import "fmt"

func expand(s string, left int, right int) string {
	var palindromeFound bool
	sLen := len(s)
	for {
		var sLeft uint8
		if left >= 0 {
			sLeft = s[left]
		} else {
			break
		}
		var sRight uint8
		if right < sLen {
			sRight = s[right]
		} else {
			break
		}
		if sLeft != sRight {
			break
		}
		palindromeFound = true
		left -= 1
		right += 1
	}
	if palindromeFound {
		return s[left+1 : right]
	} else {
		return ""
	}
}

func longestPalindrome(s string) string {
	sLen := len(s)
	var maxLength = 1
	var maxSubstr = string(s[0])
	var left = 0
	var right = 1
	for {
		if (left == right) && (right >= (sLen - 1)) {
			break
		}
		palindrome := expand(s, left, right)
		if len(palindrome) != 0 {
			palindromeLength := len(palindrome)
			if palindromeLength > maxLength {
				maxLength = palindromeLength
				maxSubstr = palindrome
			}
		}
		if left == right {
			right += 1
		} else {
			left += 1
		}
	}
	return maxSubstr
}


func main() {
	fmt.Println(longestPalindrome("a"))
}