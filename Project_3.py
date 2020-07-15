import random


def hangman():
    word = random.choice(
        ["mensuration", "kite", "doctor", "police", "water", "computer", "laptop", "mouse", "vatican", "cockroach"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guess_made = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print("You Won")
            break
        print("Guess the word", main)
        guess = input()

        if guess in valid_letters:
            guess_made = guess_made + guess
        else:
            print("Enter a valid letter")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns are left")
                print(" ---------- ")
            if turns == 8:
                print("8 turns are left")
                print(" ---------- ")
            if turns == 7:
                print("7 turns are left")
                print(" ---------- ")
                print("     0      ")
                print("     |      ")
            if turns == 6:
                print("6 turns are left")
                print(" ---------- ")
                print("     0      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns are left")
                print(" ---------- ")
                print("     0      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns are left")
                print(" ---------- ")
                print("   \ 0      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns are left")
                print(" ---------- ")
                print("   \ 0/     ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns are left")
                print(" ---------- ")
                print("   \ 0/|    ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns are left")
                print("Last breathe is counting, Take care")
                print(" ---------- ")
                print("   \ 0_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("0 turns are left")
                print("You let your kind man die...")
                print(" ---------- ")
                print("     0_|    ")
                print("    /|\     ")
                print("    / \     ")
                break


name = input("Enter your name:  ")
print("Welcome,", name)
print("------------------")
print("Try to get this word before your hangman die")
hangman()
print()
