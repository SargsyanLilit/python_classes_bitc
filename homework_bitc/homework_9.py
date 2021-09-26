# 1
def update_list_dictionary(list_: list) -> dict:
    new_dict = {}
    for i in list_dict:
        new_dict.update(i)
    return new_dict


# 2 +
def generate_x_times_x_dictionary(number_: int) -> dict:
    new_dict = {}
    for i in range(1, number_ + 1):
        new_dict[i] = i * i
    return new_dict


# 3
def drop_empty_items(my_dict: dict) -> dict:
    new_dict = {}
    for i in my_dict:
        if my_dict[i] is not None:
            new_dict[i] = my_dict[i]
    return new_dict


# 4
def count_words(my_string: str) -> dict:
    my_string_list = string_1.replace(",", "").replace(".", "").split()
    new_dict = {}
    for i in my_string_list:
        new_dict[i] = my_string_list.count(i)
    return new_dict

