from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.lists = [v1, v2]
        self.lengths = [len(l) for l in self.lists]
        self.elements_count = sum(self.lengths)
        self.elements_returned = 0
        self.list_idx = 0
        self.element_idx = 0

    def iterate(self):
        new_list_idx = self.list_idx + 1
        new_element_idx = self.element_idx
        if new_list_idx >= len(self.lists):
            new_list_idx = 0
            while new_list_idx < len(self.lists):
                new_element_idx = self.element_idx + 1
                if new_element_idx >= self.lengths[new_list_idx]:
                    new_list_idx += 1
                else:
                    break
        return new_list_idx, new_element_idx

    def next(self) -> int:
        try:
            element = self.lists[self.list_idx][self.element_idx]
        except IndexError:
            self.list_idx, self.element_idx = self.iterate()
            element = self.lists[self.list_idx][self.element_idx]
        finally:
            new_list_idx, new_element_idx = self.iterate()
            self.list_idx = new_list_idx
            self.element_idx = new_element_idx
            self.elements_returned += 1
        return element

    def hasNext(self) -> bool:
        return self.elements_returned < self.elements_count


if __name__ == '__main__':
    test_data = [
        ([1], [2], [1, 2]),
        [[1, 2], [3, 4, 5, 6], [1, 3, 2, 4, 5, 6]],
        [[1], [], [1]],
        [[], [1], [1]]
    ]
    for v1, v2, expected_result in test_data:
        result = []
        i = ZigzagIterator(v1, v2)
        while i.hasNext():
            result.append(i.next())
        print(f'{v1=}')
        print(f'{v2=}')
        print(f'{expected_result=}')
        print(f'{result=}')
        assert expected_result == result
