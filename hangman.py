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
    ## helper function for taking a guess
    ## ask for letter input
    ## if not a letter, ask for another input
    ## else if go through characters of cur_word and "reveal" letters w/ print statement
    ## if guess is wrong then -= from tries counter

def guess_num(cur_guess, tries, guessed, cur_word, hidden):
    if len(cur_guess)==1 and cur_guess.isalpha() and cur_guess not in guessed:
        if (cur_guess in cur_word):
            for i in range(len(cur_word)):
                if cur_word[i] == cur_guess:
                    hidden[i] = cur_guess
        else:
            tries -= 1
    else:
        cur_guess = input("Guess invalid, enter a character in the alphabet: ")
        guess_num(cur_guess, tries, guessed, cur_word)

        

    