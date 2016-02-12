class hangman ():#create class
    def __init__(self):
        print "hangman., ready?"
        print "(1)yes. \n(2)no."
        user_choice_1 = raw_input("->") #user choice

        if user_choice_1 == '1':
            print "loading"
            self.start_game()
        elif user_choice_1 == '2':
            print "goodbye"
            exit()
        else:
            self.__init__()

    def start_game(self):
        print "Make 6 guesses and you are dead"
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = "pizza"
        progress = ["?", "?", "?"]

        while guesses < 6:
            guess = raw_input("Guess a letter ->")

            guess = raw_input("Guess a letter ->")

			if guess in the_word and not in letters_used:
				print "As it turns out, your guess was RIGHT!"
				letters_used += "," + guess
				self.hangman_graphic(guesses)
				print "Progress: " + self.progress_updater(guess, the_word, progress)
				print "Letter used: " + letters_used
			elif guess not in the_word and not(in letters_used):
				guesses += 1
				print "Things aren't looking so good, that guess was WRONG!"
				letters_used += "," + guess
				self.hangman_graphic(guesses)
				print "Progress: " + "".join(progress)
				print "Letter used: " + letters_used
			else:
				print "Try again!"

    def hangman_graphic(self, guesses):
        if guesses == 0:
            print "__________ "
            print "|        | "
            print "|          "
            print "|          "
            print "|          "
            print "|          "

        elif guesses == 1:
            print "__________ "
            print "         | "
            print "         0 "
            print "           "
            print "           "
            print "           "

        elif guesses == 2:
            print "__________ "
            print "         | "
            print "         0 "
            print "        /  "
            print "           "
            print "           "

        elif guesses == 3:
            print "__________ "
            print "         | "
            print "         0 "
            print "        /| "
            print "           "
            print "           "

        elif guesses == 4:
            print "__________ "
            print "         | "
            print "         0 "
            print "        /|\ "
            print "           "
            print "           "

        elif guesses == 5:
            print "__________ "
            print "         | "
            print "         0 "
            print "        /|\ "
            print "        /  "
            print "           "

        else:
            print "__________ "
            print "         | "
            print "         0 "
            print "        /|\ "
            print "        / \  "
            print "           "

            print "GAME OVER!"
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1

        return "".join(progress)

game = Hangman()



