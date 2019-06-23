import random


class Game:
    user_name = ''
    guessed_number = False
    random_number = 0
    count = 0
    tries = 1
    limit = 0
    max_highest_number = 0

    def gameInit(self):
        print('Welcome to guess game')
        print('What is your name?')

        Game.user_name = input("Enter your name: ")
        if len(Game.user_name) == 0:
            Game.user_name = 'Player 1'

        print(f'Nice to meet you {Game.user_name}')

        print('')
        print('Would you like to set number of tries and random number range')

        # Check if user want to add private settings
        set_min_max = Game.__setMinMax(self)
        if set_min_max:
            print('Please enter a maximum possible random number')
            new_rand = self.__setNumber()
            if new_rand > 0:
                print('Please enter limit of tries')
                new_limit = self.__setNumber()
                # Check if tries greater than 0
                # And make sure user didn't set tries same amount as random
                if new_limit > 0 and new_rand-4 >= new_limit:
                    Game.random_number = random.randint(1, new_rand)
                    Game.limit = new_limit
                    Game.max_highest_number = new_rand
                else:
                    self.__standartSetting()  # Resset to standart settings
            else:
                self.__standartSetting()  # Resset to standart settings
        else:
            self.__standartSetting()  # Resset to standart settings

        self.__startGame()

    def __standartSetting(self):
        Game.random_number = random.randint(1, 10)
        Game.limit = 6
        Game.max_highest_number = 10

    def __setMinMax(self):
        ui = ''
        loc_count = 0
        set_values = False

        while loc_count < 3:
            ui = input('Enter Y or N: ')
            if(ui.lower() == 'y'):
                set_values = True
                break
            elif ui.lower() == 'n':
                break
            else:
                loc_count += 1
            print(loc_count)
        return set_values

    def __setNumber(self):
        new_num = 0
        loc_count = 0
        while new_num > 0 or loc_count != 3:
            ui = input('Enter number: ')
            if(Game.__checkIfNumber(self, ui)):
                new_num = int(ui)
                break

            print('Wrong input: Make sure you enter a number')
            print(loc_count)
            loc_count += 1

        if loc_count == 3:
            new_num = 0
        return new_num

    def __startGame(self):
        print('=============================')
        print(f'Enter number between 1 and {Game.max_highest_number}')
        print(f'You have {Game.limit} tries')
        tries_left = Game.limit

        # User Guess
        while Game.tries <= Game.limit:
            user_number = input('Number: ')
            isInputNumber = Game.__checkIfNumber(self, user_number)
            if isInputNumber:
                user_number = int(user_number)
                if user_number == Game.random_number:
                    Game.guessed_number = True
                    break
                tries_left -= 1
                print(f'Tries left: {tries_left}')
                Game.tries += 1
                print('Sorry wrong guessed number, try again:')

            else:
                print(
                    f'Unknown input {user_number} please enter a number between 1 adn 10')
                print(f'Please {Game.user_name}, try again')

        Game.__gameResultPrint(self)

    def __checkIfNumber(self, value):
        try:
            if(value.isdigit()):
                return True
            else:
                return False
        except ValueError:
            print("An exception occurred")

    def __gameResultPrint(self):
        if Game.guessed_number:
            print('********************************************')
            print(f'*** Congratulation {Game.user_name}, You WON!')
            print(f'*** From {Game.tries} tries                  ')
            print('********************************************')
        else:
            print('********************************************')
            print(f'*** Sorry {Game.user_name}, You lost!')
            print(f'*** The number was {Game.random_number}')
            print('********************************************')


g = Game()
g.gameInit()
