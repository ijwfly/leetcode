class Solution:
    def expand(self, s, left, right):
        pal = False
        while True:
            try:
                sleft = s[left] if left >= 0 else None
                if sleft != s[right]:
                    break
            except IndexError:
                break
            pal = True
            left -= 1
            right += 1
        if pal:
            return s[left+1:right]
        else:
            return None

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        max_len = 1
        max_substr = s[0]
        left = 0
        right = 1
        while True:
            if left == right and right >= (s_len - 1):
                break
            palindrome = self.expand(s, left, right)
            if palindrome:
                palindrome_len = len(palindrome)
                if palindrome_len > max_len:
                    max_len = palindrome_len
                    max_substr = palindrome
            if left == right:
                right += 1
            else:
                left += 1
        return max_substr


if __name__ == '__main__':
    test_data = {
        'babad': 'bab',
        'cbbd': 'bb',
        'a': 'a',
        'ac': 'a',
    }

    s = Solution()
    for input, expected_result in test_data.items():
        result = s.longestPalindrome(input)
        print(f'{result=}')
        print(f'{expected_result=}')
        assert result == expected_result
        print('--------------------')
