# 1
import random
from homework_7 import lists_intersections

game_display_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_display = [" "] * 9
available_moves_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
user_moves = []
computer_moves = []

print("Welcome to the X/O game!!!",  "You will play with 'X'", game_display_choice[:3], game_display_choice[3:6], game_display_choice[6:], sep="\n")
game_continue = True

while game_continue and len(available_moves_positions) >= 1:
    if len(available_moves_positions) <= 1:
        print("It is draw!!!")
        break
    user_move = int(input("Please enter the number, where you want to place the 'X'\n"))-1
    if user_move in available_moves_positions:

        game_display.pop(user_move)
        game_display.insert(user_move, "X")
        available_moves_positions.remove(user_move)
        user_moves.append(user_move)

        computer_move = random.choice(available_moves_positions)
        game_display.pop(computer_move)
        game_display.insert(computer_move, "O")
        available_moves_positions.remove(computer_move)
        computer_moves.append(computer_move)

        print(game_display[:3], game_display[3:6], game_display[6:], sep="\n")
    else:
        print(f"You cannot place 'X' in the {user_move+1} position")
        continue

    for i in winning_positions:
        if sorted(lists_intersections(user_moves, i)) == i:
            print("You won!!!")
            game_continue = False
        elif sorted(lists_intersections(computer_moves, i)) == i:
            print("You Lost!!!")
            game_continue = False


# 2
def remove_duplicates_list_of_lists(my_list: list) -> list:
    for item_ in my_list:
        if my_list.count(item_) >= 2:
            my_list.remove(item_)
    return my_list


# 3
def unpacked_list(my_list: list) -> list:
    new_list = []
    for item_ in my_list:
        if type(item_) == list:
            new_list.extend(item_)
        else:
            new_list.append(item_)
    return new_list


def slice_list_into_two(my_list: list, length: int) -> tuple:
    return (my_list[:length], my_list[length:])



