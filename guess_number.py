import random  # we need it for the 2nd function: game_guessing_play


def check_guess(lucky_number: int, user_guess: str) -> str:
    try:
        guess = int(user_guess)
    except ValueError:
        raise ValueError("Invalid input: must be an integer")

    if guess < 1 or guess > 100:
        raise ValueError("number out of range")

    if guess == lucky_number:
        return "!!BINGO"
    elif guess < lucky_number:
        return "higher guess"
    else:
        return "lower guess"


def game_guessing_play():
    lucky_number = random.randint(1, 100);
    while True:
        try:
            user_guess = input("Guess a number between 1-100: ");
            feedback = check_guess(lucky_number, user_guess);
            print(feedback);
            if feedback == "!!BINGO":
                break
        except Exception as ex:
            print(ex);
