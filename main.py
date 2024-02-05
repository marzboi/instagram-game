from art import logo, vs
from game_data import data
from random import choice
# from replit import clear
from clear import clear


def print_options(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, {b['country']}.")


def get_higher(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'


def move_correct(a, b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b


def remove_from_local_list(item, data_list):
    data_list.remove(item)


def play_game():
    is_game_over = False
    score = 0
    game_data = data.copy()

    while not is_game_over:
        print(logo)
        if score > 0:
            print(f'You are right! Current score: {score}')

        if score == 0:
            a = choice(game_data)
            remove_from_local_list(a, game_data)

        b = choice(game_data)
        remove_from_local_list(b, game_data)

        print_options(a, b)
        higher_count = get_higher(a, b)
        moving_next = move_correct(a, b)

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_guess == higher_count:
            clear()
            score += 1
            a = moving_next

        else:
            is_game_over = True
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score {score}")


replay = True
while replay:
    clear()
    play_game()
    user_replay = input("Do you wish to play again? 'Y' or 'N': ").lower()
    if user_replay == "n":
        replay = False
        clear()
        print('Goodbye!')
