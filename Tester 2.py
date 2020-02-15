import random
from collections import Counter


def MakeHiddenCode():
    hidden_code = []
    all_colors = ('red', 'green', 'blue', 'yellow', 'brown', 'orange')

    for color_pick in range(1, 5):
        all_colors_index_picked = random.randint(0, 5)
        hidden_code.append(all_colors[all_colors_index_picked])
    return hidden_code


def checkPins(guess, hidden_code):
    # Check how many red and white pins represent the answer given.

    white_pin_check_hidden_code, white_pin_check_guess = [], []
    amount_red, white_amount = 0, 0

    # Check how many correct / red pins
    for check_index in range(0, 4):
        if guess[check_index] == hidden_code[check_index]:
            amount_red += 1
        else:
            # if its incorrect, it could still give a white pin, this is saved here to calculate later.
            white_pin_check_guess.append(guess[check_index])
            white_pin_check_hidden_code.append(hidden_code[check_index])

    # to check how many white pins are needed
    for values in white_pin_check_guess:
        for values2 in white_pin_check_hidden_code:
            if values == values2:
                white_pin_check_hidden_code.remove(values2)  # so that if the player guessed with 2 of the same colors, but the answers contains only 1 of said color, it wont give 2 white pins.
                white_amount += 1
                break

    return amount_red, white_amount


def make_all_possibilities():
    all_colors = ('red', 'green', 'blue', 'yellow', 'brown', 'orange')
    all_possibilities = []
    for i in all_colors:
        for j in all_colors:
            for k in all_colors:
                for l in all_colors:
                    all_possibilities.append([i, j, k, l])
    return all_possibilities


def make_next_guess(all_possible_combinations):

    best_expected_size = float('inf')
    for items in all_possible_combinations:
        guess = items
        List_Data_to_calculate = []

        allfeedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                       (1, 0), (1, 1), (1, 2), (1, 3),
                       (2, 0), (2, 1), (2, 2),
                       (3, 0), (4, 0)]

        for items_feedback in allfeedback:

            Templist = []
            for items in all_possible_combinations:
                if checkPins(guess, items) != items_feedback:
                    Templist.append(items)

            Data_to_calculate = len(all_possible_combinations) - len(Templist)
            List_Data_to_calculate.append(Data_to_calculate)

        Expectend_size = 0
        for items in List_Data_to_calculate:
            Expectend_size += ((items ** 2) / len(all_possible_combinations))

        if Expectend_size < best_expected_size:
            best_expected_size = Expectend_size
            bestcombi = guess
    return bestcombi


def main():
    gemtries = 0
    for total in range(1,11):  # om het spel 10 keer gespeeld te laten worden
        hidden_code = MakeHiddenCode()

        all_possible_combinations = make_all_possibilities()

        tries = 0
        guess = ['red', 'red', 'green', 'blue']

        for numbers in range(1, 24, 1):

            redPinCount, whitePinCount = checkPins(guess, hidden_code)
            if redPinCount == 4:
                break
            tries += 1
            for items in all_possible_combinations:
                if checkPins(guess, items) != (redPinCount, whitePinCount):
                    all_possible_combinations.remove(items)

            guess = make_next_guess(all_possible_combinations)


        print(tries)
        gemtries += tries
    gemtries = gemtries / 10
    return gemtries


if __name__ == "__main__":
    totalGem = 0
    for data in range(1,11):
        print(main())
        totalGem += main()
    print(totalGem/10)