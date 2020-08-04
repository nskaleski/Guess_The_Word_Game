import random

wordList = ["packers", "bears", "vikings", "lions", "patriots", "colts", "chargers"]
print("there is a list containing " + str(len(wordList)) + " words. try to guess the chosen word.")
print("You get three guesses")

chosenWord = random.choice(wordList)
guesses = 1

while guesses <= 3:
    user_guess = input("guess word: ")
    if user_guess == chosenWord:
        print("correct! You win!")
        break
    if guesses == 3:
        print("sorry, you couldn't guess the word. it was " + chosenWord)
        break
    if user_guess != chosenWord:
        print("Wrong! Guess again")
        guesses += 1