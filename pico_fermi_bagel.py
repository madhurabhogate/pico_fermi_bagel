"""
    *** PICO FERMI BAGEL ***

The object of the game is to guess a 3 digit number correctly.
'Pico' means a digit is correct but it’s in the wrong place value or location.

'Fermi' means a digit is correct AND it’s in the correct place value or location.

'Bagels' means nothing is correct.

Fun facts:
“pico” means “a little” so when you get a pico in the game, it means you’re a little bit right;
“Fermi” is the name of a famous Italian mathematician so when you get a Fermi in the game,
you’re thinking like a mathematician and getting very close;
“bagels”, What does a bagel look like? A zero! it means you got zero correct.

"""
import random


def generate_guess_number():
    return str(random.randrange(100, 999))


def validate_user_input(user_data):
    if user_data.isdigit():
        if int(user_data) in range(100,1000):
            return True
    else:
        return False


def check_user_number(user_number, guess_number):
    result = ''
    for index in range(0,3):
        if user_number[index] == guess_number[index]:
            result += 'F '
        elif user_number[index] in list(guess_number):
            result += 'P '

    if not result:
        return 'B'
    else:
        return result


def main():
    print_banner = "*** Welcome to PICO FERMI BAGEL game. ***\n\n\
The object of the game is to guess a 3 digit number correctly.\n\
PICO means a digit is correct but it’s in the wrong place value or location.\n\
FERMI means a digit is correct AND it’s in the correct place value or location.\n\
BAGELS means nothing is correct.\n\n\
Fun facts:\n\
PICO means 'a little', so when you get a pico in the game, it means you’re a little bit right.\n\
FERMI is the name of a famous Italian mathematician so when you get a Fermi in the game,\n\
you’re thinking like a mathematician and getting very close.\n\
BAGELS, What does a bagel look like? A zero! it means you got zero correct.\n\n\
Enter 'exit' to end the game."

    print(print_banner)
    number_to_be_guessed = generate_guess_number()
    print('\nGuess the 3 digit number')
    correct = False
    while not correct:
        user_data = input('>')
        if user_data != 'exit':
            if validate_user_input(user_data):
                output = check_user_number(user_data, number_to_be_guessed)
                if 'F F F ' in output:
                    correct = True
                    print('FERMI FERMI FERMI!!. You win.')
                elif 'B' in output:
                    print('Bagels, Sadly none of the digits match')
                else:
                    print(output)
            else:
                print('Invalid 3 digit number')
        else:
            break


if __name__ == "__main__":
    main()
