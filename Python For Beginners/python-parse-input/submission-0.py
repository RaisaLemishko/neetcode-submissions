from typing import List

def read_integers() -> List[int]:
    init_list = input().split(",")
    result = []
    for i in init_list:
        result.append(int(i))   
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
