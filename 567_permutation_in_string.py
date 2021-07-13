from collections import defaultdict
from typing import List


class Solution:
    def calculate_letters(self, s: str) -> List[int]:
        s_letters = [0] * (ord('z') - ord('a') + 1)
        for char in s:
            char_num = self.char_num(char)
            s_letters[char_num] += 1
        return s_letters

    @staticmethod
    def char_num(char):
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_letters = self.calculate_letters(s1)
        window_letters = [0] * (ord('z') - ord('a') + 1)

        for idx in range(len(s1)):
            char_num = self.char_num(s2[idx])
            window_letters[char_num] += 1

        left_char_idx = 0
        right_char_idx = left_char_idx + len(s1) - 1
        while True:
            if window_letters == s1_letters:
                return True

            left_char_num = self.char_num(s2[left_char_idx])
            window_letters[left_char_num] -= 1
            left_char_idx += 1

            right_char_idx += 1
            if right_char_idx >= len(s2):
                break
            right_char_num = self.char_num(s2[right_char_idx])
            window_letters[right_char_num] += 1

        return False


if __name__ == '__main__':
    test_data = [
        ["ab", "eidbaooo", True],
        ["ab", "eidboaoo", False],
        ["adc", "dcda", True],
    ]
    s = Solution()
    for s1, s2, expected_result in test_data:
        result = s.checkInclusion(s1, s2)
        print(f'{s1=} {s2=}')
        print(f'{result=}')
        print(f'{expected_result=}')
        assert result == expected_result
        print('-------------------')
