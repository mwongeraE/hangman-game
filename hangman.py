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

