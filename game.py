from time import sleep

entrance = "Welcome To The Guessing Game\n We will be giving you 3 tries to guess a word."
print(entrance)

print("Are you ready?")
proceed = input("Y/N: ")
words = ["cat", "dog", "rabbit", "panda"]
print("Guess An Animal.")

def guessing():
    guess_count = 3
    while guess_count !=0:
        guess = input("Enter: ")
        if guess in words:
            print("Correct, You got it!")
            exit()
        elif guess_count != 0:
            guess_count = guess_count - 1
            print(f"You got it wrong! You have {guess_count} guesses left!")
        else:
            print("You have ran out of guesses")
            sleep(2)
            exit()
guessing()