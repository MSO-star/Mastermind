import random

hidden_code = []
all_colors = ('red', 'green', 'blue', 'yellow', 'brown', 'orange', 'black', 'white')

for color_pick in range(1, 5, 1):
    all_colors_index_picked = random.randint(0, 7)
    hidden_code.append(all_colors[all_colors_index_picked])
print(all_colors)
win = False
tries = 0
while not win:
    guess = []
    print('')

    # asking the player to make a guess in order.
    while len(guess) < len(hidden_code):
        string_guess = str((len(guess)+1))
        pick1 = input('Pick color '+string_guess+': ')
        guess.append(pick1)

    # Check how many correct / red pins
    amount_correct = 0
    white_pin_check_hidden_code, white_pin_check_guess = [], []

    for check_index in range(0, 4, 1):
        if guess[check_index] == hidden_code[check_index]:
            amount_correct += 1
        else:
            # if its incorrect, it could still give a white pin, this is saved here to calculate later.
            white_pin_check_guess.append(guess[check_index])
            white_pin_check_hidden_code.append(hidden_code[check_index])


    # to check how many white pins are needed
    white_amount = 0
    for values in white_pin_check_guess:
        for values2 in white_pin_check_hidden_code:
            if values == values2:
                white_pin_check_hidden_code.remove(values2)  # so that if the player guessed with 2 of the same colors, but the answers contains only 1 of said color, it wont give 2 white pins.
                white_amount += 1
                break

    # Show the data of guess
    if amount_correct != 4:
        tries += 1
        while amount_correct != 0:
            print('Red', end='. ')
            amount_correct -= 1
        while white_amount != 0:
            print('White', end='. ')
            white_amount -= 1
    else:
        win = True

    if tries == 10:
        break

if win:
    print('Win')
else:
    print('Lose')

print(hidden_code)