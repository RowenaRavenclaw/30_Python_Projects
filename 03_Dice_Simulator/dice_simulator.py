import random


def roll_dace(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")

            if user_input.lower() == "exit":
                print("Thank you for playing")
                break
            roll_list = roll_dace(int(user_input))
            print(*roll_list, f"({sum(roll_list)})", sep=", ")

        except ValueError:
            print("please type valid Number")


if __name__ == "__main__":
    main()
