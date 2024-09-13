from random import randint


def guess():
    min_num, max_num = 1, 10
    random_num: int = int(randint(min_num, max_num))
    print(f'Guess number from {min_num} to {max_num}')

    while True:
        try:
            user_input: int = int(input("Guess: "))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if user_input > random_num:
            print('The number is lower')
        elif user_input < random_num:
            print('The number is upper')
        else:
            print('You guessed it!')
            break

