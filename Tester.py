import sys
import random


def PlayerInput_HiddenCode():
    hidden_code = []
    print('Make a code for the computer to guess. \nChoose from: \033[36m(red, green, blue, yellow, brown, orange)\033[35m')
    for code_amount in range(1, 5):
        pick = input('Pick color '+str(code_amount)+': ')
        hidden_code.append(pick)

    print('Your hidden code is: \033[34m' + str(hidden_code) + '\033[35m')
    return hidden_code #secret code


def PlayerInput_Feedback(): #####Moet ik nog maken
    print('Give the computer the\033[32m correct\033[35m feedback about the guess')  # bron: https://ozzmaker.com/add-colour-to-text-in-python/
    Redpins = int(input('Amount\033[31m red\033[35m: '))
    Whitepins = int(input('Amount\033[39m white\033[35m: '))
    return Redpins, Whitepins


def make_all_possibilities():
    # Makes a large list of every single possible combination of guesses.
    all_colors = ('red', 'green', 'blue', 'yellow', 'brown', 'orange')
    all_possibilities = []
    for i in all_colors:  # Looks at every possible color and via 4 nested loops it puts every color once, with every other color.
        for j in all_colors:
            for k in all_colors:
                for l in all_colors:
                    all_possibilities.append([i, j, k, l])
    return all_possibilities


def Remove_possibilities(all_possible_combinations, guess, redPinCount, whitePinCount):
    # removing ever possibility that can never be the answer
    Return_list = []
    all_possible_combinations.remove(guess)  # removing the last guess specifically
    for items in all_possible_combinations:
        if checkPins(guess, items) == (redPinCount, whitePinCount):
            Return_list.append(items)

    return Return_list


def make_next_guess(all_possible_combinations):
    print('Calculating new guess...')

    best_expected_size = float('inf')
    wait_animation = [" [=     ]", " [ =    ]", " [  =   ]", " [   =  ]", " [    = ]", " [     =]", " [    = ]", " [   =  ]", " [  =   ]", " [ =    ]"]
    animation_loop_counter = 0
    bestcombi = None #https://www.educative.io/edpresso/what-is-the-none-keyword-in-python
    for Every_combination_as_guess in all_possible_combinations:

        guess = Every_combination_as_guess
        List_Data_to_calculate = []

        allfeedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                       (1, 0), (1, 1), (1, 2), (1, 3),
                       (2, 0), (2, 1), (2, 2),
                       (3, 0), (4, 0)]

        for items_feedback in allfeedback:
            sys.stdout.write("\r" + wait_animation[animation_loop_counter % len(wait_animation)])  # bron: https://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python
            sys.stdout.flush()
            animation_loop_counter += 1

            Templist = []
            for Every_combination_as_code in all_possible_combinations:
                if checkPins(guess, Every_combination_as_code) != items_feedback:
                    Templist.append(Every_combination_as_code)

            Data_to_calculate = len(all_possible_combinations) - len(Templist)
            List_Data_to_calculate.append(Data_to_calculate)

        Expectend_size = 0
        for items in List_Data_to_calculate:
            Expectend_size += ((items ** 2) / len(all_possible_combinations))

        if Expectend_size < best_expected_size:
            best_expected_size = Expectend_size
            bestcombi = guess

    return bestcombi


def make_hidden_code():
    hidden_code = []
    all_colors = ('red', 'green', 'blue', 'yellow', 'brown', 'orange')

    for color_pick in range(4):
        all_colors_index_picked = random.randint(0, 5)
        hidden_code.append(all_colors[all_colors_index_picked])
    return hidden_code


def player_make_guess():
    guess = []
    while len(guess) < 4:
        string_guess = str((len(guess) + 1))
        pick1 = input('Pick color ' + string_guess + ': ')
        guess.append(pick1)

    return guess


def Show_manual():
    print('How to play: To outsmart your opponent with a clever code or great guesswork.\n'
          '------------------------------------------------------------------------------------------------------------------------------------\n'
          'As the Codemaker: your goal is to set a mystery code so cunning that it will keep your opponent guessing for as long as possible.\n'
          'You provide feedback per guess with white and red pins, a red pins states a correct color in the correct player,\n'
          'a white color states a correct color in the wrong place\n'
          '------------------------------------------------------------------------------------------------------------------------------------\n'
          'As the Guesser: you must break the secret code in the fewest number of guesses.\n'
          'You provide 4 colors as a guess of the secret code, if it is not the secret code you will be provided with feedback about your guess\n'
          'A red pins states a correct color in the correct player, a white color states a correct color in the wrong place')


def End_screen(win):
    if win:
        print('\033[32m█████████████████████████████████████████████\n'
              '█▄─█─▄█─▄▄─█▄─██─▄█████▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█\n'
              '██▄─▄██─██─██─██─███████─█─█─█─███─███─█▄▀─██\n'
              '▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀\033[35m')
    else:
        print('\033[32m███████████████████████████████████████\n'
              '█▄─▄▄─█─▄▄▄─█████▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█\n'
              '██─▄▄▄█─███▀██████─█─█─█─███─███─█▄▀─██\n'
              '▀▄▄▄▀▀▀▄▄▄▄▄▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀\033[35m')


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


def main():

    def player_as_guesser():
        hidden_code = make_hidden_code()
        print('De computer has made a secret code, try to guess it. \nChoose from: \033[36m(red, green, blue, yellow, brown, orange)\033[35m')

        for tries in range(1, 12):
            guess = player_make_guess()

            amount_correct, white_amount = checkPins(guess, hidden_code)

            if amount_correct == 4:
                End_screen(True)
                print('Tries needed: '+str(tries))
                break
            elif tries == 11:
                End_screen(False)
                break

            print('Amount\033[31m red\033[35m pins: '+str(amount_correct))
            print('Amount\033[39m white\033[35m pins: '+str(white_amount))

        print('The secret code was: \033[36m'+str(hidden_code)+'\033[35m')

    def computer_as_guesser():
        all_possible_combinations = make_all_possibilities()
        hidden_code = PlayerInput_HiddenCode()
        guess = ['red', 'red', 'green', 'blue']  # First guess

        # Game starts here
        for tries in range(1, 12):
            print('\nThe computer gave \033[36m'+str(guess)+'\033[35m as guess')

            redPinCount, whitePinCount = None, None
            Check_player_honesty = checkPins(guess, hidden_code)  # The computer also calculates the correct feedback to check if the player has given the correct feedback.
            while Check_player_honesty != (redPinCount, whitePinCount):
                redPinCount, whitePinCount = PlayerInput_Feedback()

            if redPinCount == 4:
                End_screen(False)
                print('Tries needed: ' + str(tries))
                break
            if tries == 11:
                End_screen(True)
                break

            all_possible_combinations = Remove_possibilities(all_possible_combinations, guess, redPinCount, whitePinCount)
            guess = make_next_guess(all_possible_combinations)

    while True:
        print('Do you want to play as guesser or codemaker?')
        Game_mode = input('Guesser / Codemaker / Manual: ')
        Game_mode = Game_mode.lower()
        if 'gues' in Game_mode:
            player_as_guesser()
            break
        elif 'man' in Game_mode:
            Show_manual()
        else:
            computer_as_guesser()
            break


if __name__ == "__main__":  # bron: Casper
    print('\033[35mWelcome to Mastermind.')
    while True:  # replay the game unless specified otherwise.
        main()
        # break out of main loop if player says no.
        print('Do you want to play again?')
        replay = input('Yes / No: ')
        replay = replay.lower()
        if 'n' in replay:
            break
    print('Goodbye')