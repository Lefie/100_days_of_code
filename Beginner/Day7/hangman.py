import random
from sketch import word_list
from sketch import stages
from sketch import logo


class Hangman():
    def __init__(self, chosen_word: str):
        self.chosen_word = chosen_word  # randomly choose a word
        self.word_length = len(chosen_word)  # Tell user the length of the chosen word
        self.chosen_letters = []  # fill chosen word boilerplate
        self.total_lives = 6

    def print_word_hint(self):
        print(f'This word is {self.word_length} characters long')

    def generate_guessed_word(self) -> str:
        guessed_word = []

        for letter in self.chosen_word:
            if letter not in self.chosen_letters:
                guessed_word.append('_')
            else:
                guessed_word.append(letter)

        return ''.join(guessed_word)

    def guess_letters(self):
        while True:
            # check if game over
            if not "_" in self.generate_guessed_word():
                print("You won!")
                break
            elif self.total_lives <= 0:
                print("You lose!")
                print(f"The word is {self.chosen_word}")
                break

            print(f'Current Guess: {self.generate_guessed_word()}\nRemaining Lives: {self.total_lives}\n')
            letter = input("Guess a letter! ").lower()

            if len(letter) > 1:
                print("Guess a single letter!")
                continue

            if not(ord(letter) >= 97 and ord(letter) <= 122):
                print("Guess an actual letter!")
                continue

            if letter in self.chosen_letters:
                print("You already guessed this letter!")
                continue

            self.chosen_letters.append(letter)

            if letter not in self.chosen_word:
                print(f"You guessed {letter} and it is not in the word. You lost a life! >:(")
                self.total_lives -= 1
                print(stages[self.total_lives])
                continue

if __name__ == "__main__":
    print(logo)
    continuePlaying = True
    while continuePlaying:
        hangman = Hangman(chosen_word=word_list[random.randint(0,len(word_list)-1)])
        hangman.print_word_hint()
        hangman.guess_letters()
        continuePlaying = input('Continue playing? (y/n) ') == 'y'











