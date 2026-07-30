from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    result = []
    for i in range(3, 0, -1):
        result.append(my_list[len(my_list) - i])
    return result


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))