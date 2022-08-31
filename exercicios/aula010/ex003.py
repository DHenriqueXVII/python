from random import randint

def main():
    print('\nHello, welcome to the guessing game!')

    randomNumber = randint(1,100)

    attemptsNumber = 1

    running = True

    while running:
        userNumber = int(input('\nEnter a integer between 1 and 100: '))

        if userNumber == randomNumber:
            running == False

            print('\nCongratulations, you got it right!')
            print(f'Attempts number: {attemptsNumber}\n')

            answer = str(input('Do you want to continue ? Y/N ')).lower().strip()

            if answer == 'y':
                main()
            else:
                print('\nIt was good to play with you!')
                break
        elif attemptsNumber == 10:
            running = False

            print('\nGame over! you lost all attempts!')

            answer = str(input('\nDo you want to continue ? Y/N ')).lower().strip()

            if answer == 'y':
                main()
            else:
                print('\nIt was good to play with you!')
                break
        else:
            if userNumber != randomNumber:
                print('\nIncorret answer! ','very high number!' if userNumber > randomNumber else 'very low number!')
                print(f'Attempts number: {attemptsNumber}')

                attemptsNumber += 1

main()