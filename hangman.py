def game():
    cur_word = input("Please enter a word: ")
    tries = 5
    guessed = []
    hidden = ""
    for i in range(len(cur_word)):
        hidden += "_"
    
    while (tries < 0):
        cur_guess = input("Enter a character in the alphabet: ")
        guess_num(cur_guess, tries, guessed, cur_word, hidden)
        if (hidden==cur_word):
            print("Congratulations! You guessed the word!")
            return
    print("Game over! You have run out of tries...")
    repeat = input("Play again? (Y/N): ")
    if (repeat.lower=="y"):
        game()


def guess_num(cur_guess, tries, guessed, cur_word, hidden):
    if len(cur_guess)==1 and cur_guess.isalpha() and cur_guess not in guessed: ## if guess is valid
        if (cur_guess in cur_word): ## correct guess, reveals places in which guessed num are in word
            for i in range(len(cur_word)):
                if cur_word[i] == cur_guess:
                    hidden[i] = cur_guess
            print("Current word: ", hidden)
            guessed.append(cur_guess)
        else: ## wrong guess, tries--
            tries -= 1
    else: # gets another input
        cur_guess = input("Guess invalid, enter a character in the alphabet: ")
        guess_num(cur_guess, tries, guessed, cur_word)

        

    