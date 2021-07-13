from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sums = []
        sum = 0
        for num in nums:
            if num == 0:
                if sum:
                    sums.append(sum)
                    sum = 0
                sums.append(0)
            else:
                sum += 1
        else:
            if sum:
                sums.append(sum)
        print(f'{sums=}')

        if len(sums) == 1:
            return sums[0] - 1

        left = 0
        middle = 1
        right = 2
        pre_results = []
        while right < len(sums):
            l = sums[left]
            m = sums[middle]
            r = sums[right]
            pre_results.append(l + m + r)
            left += 1
            middle += 1
            right += 1
        print(f'{pre_results=}')
        return max(pre_results)


if __name__ == '__main__':
    test_data = [
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
        ([1, 1, 0, 0, 1, 1, 1, 0, 1], 4),
        ([0, 0, 0], 0),
    ]

    s = Solution()
    for nums, expected_result in test_data:
        result = s.longestSubarray(nums)
        print(f'{nums=}')
        print(f'{result=}')
        print(f'{expected_result=}')
        assert result == expected_result
        print('----------------------')
