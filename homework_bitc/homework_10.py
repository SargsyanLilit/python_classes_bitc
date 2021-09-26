# 1
import random


def password_generator(length_):
    for i in range(length_):
        order = random.randint(65, 90)
        yield chr(order)


# 2
def even_number_generator():
    i = 0
    while True:
        check = yield i
        i += 2
        if check == "restart":
            i = 0
