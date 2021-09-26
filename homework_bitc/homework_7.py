# 1-a
def remove_duplicates(my_list: list) -> list:
    for item_ in my_list:
        if my_list.count(item_) >= 2:
            my_list.remove(item_)
            my_list.remove(item_)
    return my_list


# 1-b
def lists_intersections(list_1: list, list_2: list) -> list:
    intersection_list = []
    for item_ in list_1:
        if item_ in list_2 and item_ not in intersection_list:
            intersection_list.append(item_)
    return intersection_list


# 2
def divisor_5(my_list: list) -> list:
    for item_ in my_list:
        if item_ % 5 == 0:
            print(item_)


# 3
def string_backwards(text: str) -> str:
    text_list = text.split()
    print(" ".join(text_list[::-1]))


# 4
def tuple_reverse(my_tuple: tuple) -> tuple:
    return my_tuple[::-1]


# 5
def sort_list(my_list: list) -> list:
    sorted_list = []
    for _ in range(len(my_list)):
        min_item = my_list[0]
        for item_ in my_list:
            if item_ <= min_item:
                min_item = item_
        sorted_list.append(min_item)
        my_list.remove(min_item)
    return sorted_list


# 6
def sort_list_second_largest(my_list: list) -> int:
    return sort_list(my_list)[-2]
