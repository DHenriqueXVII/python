from random import randint
from os import system, name

clear = 'cls' if name == 'nt' else 'clear'

system(clear)

print('Hello, welcome to the guessing game!\n')

def main():    
    randomNumber = randint(1,100)

    attemptsNumber = 1

    running = True

    while running:
        userNumber = int(input('Enter a integer between \33[1;33m1\33[m and \33[1;33m100\33[m: '))

        if userNumber == randomNumber:
            running == False

            system(clear)

            print('\33[1;32mCongratulations, you got it right!\33[m')
            print(f'Attempts number: \33[1;33m{attemptsNumber}\n\33[m')

            answer = str(input('Do you want to continue ? \33[1;32mY\33[m/\33[1;31mN\33[m ')).lower().strip()

            if answer == 'y':
                system(clear)

                main()
            else:
                system(clear)

                print('\33[1;32mIt was good to play with you!\33[m')

                exit()
        elif attemptsNumber == 10:
            running = False

            system(clear)

            print('\33[1;31mGame over! you lost all attempts!\33[m')

            print(f'\nThe number was \33[1;33m{randomNumber}\33[m')

            answer = str(input('\nDo you want to continue ? \33[1;32mY\33[m/\33[1;31mN\33[m ')).lower().strip()

            if answer == 'y':
                system(clear)

                main()
            else:
                system(clear)

                print('\33[1;32mIt was good to play with you!\33[m')

                exit()
        else:
            if userNumber != randomNumber:
                system(clear)

                print('Incorret answer! ','\33[1;33mvery high number!\33[m' if userNumber > randomNumber else '\33[1;33mvery low number!\33[m')
                print(f'Attempts number: \33[1;33m{attemptsNumber}\33[m\n')
                
                attemptsNumber += 1

main()