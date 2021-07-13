from itertools import zip_longest
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        range_start = None
        for first_num, second_num in zip_longest(nums[0:len(nums)], nums[1:]):
            if range_start is None:
                range_start = first_num
            if first_num + 1 != second_num:
                range_end = first_num
                if range_start == range_end or range_end is None:
                    range = f'{range_start}'
                else:
                    range = f'{range_start}->{range_end}'
                ranges.append(range)
                range_start = None
        return ranges


if __name__ == '__main__':
    test_data = [0, 1, 2, 4, 5, 7]

    s = Solution()
    result = s.summaryRanges(test_data)
    print(test_data)
    print(result)
