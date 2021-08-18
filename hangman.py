import random
import string

print("H A N G M A N")
while True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        secret = random.choice(words)
        blanks = ["-"]*len(secret)
        letters = set(secret)
        guessed = set()
        tries = 8
        while tries > 0:
            print()
            print("".join(blanks))
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif guess not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
            elif guess in guessed:
                print("You've already guessed this letter")
            elif guess in letters:
                for index, character in enumerate(secret):
                    if guess == character:
                        blanks[index] = guess
                letters.remove(guess)
                guessed.add(guess)
                if not letters:
                    print("You guessed the word!")
                    print("You survived!")
                    break
            else:
                tries -= 1
                guessed.add(guess)
                print("That letter doesn't appear in the word")
        else:
            print("You lost!")
    elif play == "exit":
        break
