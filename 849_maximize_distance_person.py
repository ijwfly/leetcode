import math
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distances = []
        current_distance = 0
        for seat in seats:
            if not seat:
                current_distance += 1
            else:
                if current_distance:
                    distances.append(current_distance)
                    current_distance = 0
                distances.append(0)
        else:
            if current_distance:
                distances.append(current_distance)

        # hack for edge case when there is no people on edge of chairs
        if distances[0] != 0:
            distances[0] *= 2
        if distances[-1] != 0:
            distances[-1] *= 2
        return math.ceil(max(distances) / 2)


if __name__ == '__main__':
    test_data = [
        ([1, 0, 0, 0, 1, 0, 1], 2),
        ([1, 0, 0, 0], 3),
        ([0, 1], 1),
    ]

    s = Solution()
    for seats, expected_result in test_data:
        result = s.maxDistToClosest(seats)
        print(f'{seats=}')
        print(f'{result=}')
        print(f'{expected_result=}')
        assert result == expected_result
        print('----------------------')
