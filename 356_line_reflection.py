from collections import defaultdict
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points_dict = defaultdict(set)
        middle_y = None
        for point in points:
            x, y = point
            points_dict[y].add(x)
        for y, grouped_points in points_dict.items():
            new_middle_x = (max(grouped_points) + min(grouped_points)) / 2
            if middle_y and new_middle_x != middle_y:
                return False
            middle_y = new_middle_x

            for point in grouped_points:
                point_to_point_distance = 2 * abs(middle_y - point)
                if point > middle_y:
                    if point - point_to_point_distance not in grouped_points:
                        return False
                elif point < middle_y:
                    if point + point_to_point_distance not in grouped_points:
                        return False
        return True

if __name__ == '__main__':
    test_data = [
        ([[1, 1], [-1, -1]], False),
        ([[1, 1], [-1, 1]], True),
        ([[0, 0], [1, 0], [3, 0]], False),
        ([[-16, 1], [16, 1], [16, 1]], True),
        ([[1, 2], [2, 2], [3, 2], [4, 2]], True),
        ([[0, 0]], True),
        ([[1, 1], [0, 1], [-1, 1], [0, 0]], True),
        ([[1,1],[-3,1]], True),
    ]

    s = Solution()
    for points, expected_result in test_data:
        result = s.isReflected(points)
        print(f'{points=}')
        print(f'{result=}')
        print(f'{expected_result=}')
        assert result == expected_result
        print('----------------------')
