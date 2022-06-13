from RandomWord import random_word


class HangMan:

    @staticmethod
    def hang_man(guess):
        print('\033[1m \033[92m-------------------------------------------------------------------\033[92m\n'
              '\n'
              '    \033[96m                       HANGMAN                     \033[96m            \n'
              '\n'
              '\033[92m--------------------------------------------------------------------\033[0m\n'
              )

        choice = 'y'

        while choice == 'y':
            # word = random.choice(lst)  # SELECTING A RANDOM WORD FROM word_list.py
            word = str(random_word())
            life = j = win = count = 0
            print(word)

            ges_word = []
            entered_letter = []
            list_ = 1

            for i in word:
                if i.isalpha():
                    ges_word.append('_')  # (_ _ _ ......)
                    j += 1  # LENGTH OF STRING

            life = 5  # total five life left
            print("\nLET'S START\n")
            while life != 0 and j != win:
                print(*ges_word)
                while guess in ges_word:
                    guess = input("\nYou have already guessed this letter ! Try another letter : ")
                for char in range(j):
                    # to check all elements in word
                    if guess.lower() in word[char]:  # checking our guess is
                        ges_word[char] = word[char]  # assigning the correct word to the char th position of ges_word
                        win += 1  # counting number of wins
                if win == count:  # if guess is wrong
                    life -= 1
                    print(f"INCORRECT \033[91m{life} life's left\033[0m ")
                else:
                    print('\033[92m you got it right \033[0m')

                count = int(win)  # assigning number of wins to count

            if life == 0:
                print('\nsorry you have used all of you life !\n\nThe word was : ' + word + '\n Better luck next time .')
            else:
                print(*ges_word, '\nhurry ! , you have guessed the word right\n\033[95m\033[1m YOU WON!\033[0m')

            choice = input('\nDo you want to play again (y/n) :')

