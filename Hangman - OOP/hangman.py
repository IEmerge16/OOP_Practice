ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


class Hangman:
    @staticmethod
    def welcome_players():
        print("Welcome to Hangman!")

    def __init__(self):
        self.welcome_players()
        self.run = True
        self.play = False
        self.used_letters = {letter: False for letter in ALPHABET}

    def get_guesser(self):
        print("Enter the name of the guesser.")
        self.guesser = input("Guesser's name: ")

    def get_host(self):
        print("Enter the name of the host.")
        self.host = input("Host's name: ")

    def get_guess_word(self):
        while True:
            print(f"{self.host}, enter your word. Don't let {self.guesser} see it!")
            self.guess_word = input("Word: ").lower()
            is_valid_word = True
            for letter in self.guess_word:
                if letter != " " and letter not in ALPHABET:
                    is_valid_word = False
                    break
            if is_valid_word:
                self.current_word = ["_" if letter !=
                                     " " else " " for letter in self.guess_word]
                break
            print("The word is not valid. Please enter only english alphabet letters.")

    def set_number_of_lives(self):
        while True:
            print(
                f"{self.host}, how many times (from 1 to 26) do you want {self.guesser} to guess your word?")
            try:
                self.lives = int(input("Lives: "))
            except ValueError:
                print("The input is not a number.")
                continue
            if 1 <= self.lives and self.lives <= 26:
                return
            print("Please pick a number from 1 to 26, inclusive.")

    def get_guess_letter(self):
        while True:
            print(f"{self.guesser}, please enter your guess letter.")
            self.guess_letter = input("Letter: ").lower()
            if self.guess_letter not in ALPHABET:
                print("The character is not an English Alphabet letter.")
                continue
            if self.used_letters[self.guess_letter]:
                print("The letter is already used.")
                continue
            return

    def add_letter_to_used(self):
        self.used_letters[self.guess_letter] = True

    def update_current_word(self):
        for idx, letter in enumerate(self.guess_word):
            if letter == self.guess_letter:
                self.current_word[idx] = self.guess_letter

    def print_current_word(self):
        word_to_print = "".join(self.current_word)
        print(f"Current word: {word_to_print}")

    def update_number_of_lives(self):
        if self.guess_letter in self.guess_word:
            return
        print("Oh no! The letter is not in the word.")
        self.lives -= 1

    def print_number_of_lives(self):
        print(f"Current lives: {self.lives}")

    def compare_word_to_guess_word(self):
        self.word_is_correct = self.guess_word == "".join(self.current_word)

    def check_game_status(self):
        if self.word_is_correct:
            print(f"{self.guesser} guessed {self.host}'s word!")
            self.play = False
        if not self.lives:
            print(f"{self.guesser} ran out of lives!")
            print(f"The word is {self.guess_word}.")
            self.play = False

    def gameplay(self):
        self.play = True
        self.get_guesser()
        self.get_host()
        self.get_guess_word()
        self.set_number_of_lives()
        self.print_current_word()
        while self.play:
            self.get_guess_letter()
            self.add_letter_to_used()
            self.update_current_word()
            self.print_current_word()
            self.update_number_of_lives()
            self.print_number_of_lives()
            self.compare_word_to_guess_word()
            self.check_game_status()

    def reset_used_letters(self):
        self.used_letters = {letter: False for letter in ALPHABET}

    @staticmethod
    def thank_players():
        print("Thank you for playing!")

    def play_again(self):
        while True:
            print("Do you want to play again? Press y to play again, n to exit the game.")
            play_again = input("(y/n): ").lower()
            if play_again not in ("y", "n"):
                print("Press y to play again, n to exit the game.")
                continue
            if play_again == "y":
                self.reset_used_letters()
            else:
                Hangman.thank_players()
                self.run = False
            return


def main():
    hangman = Hangman()
    while hangman.run:
        hangman.gameplay()
        hangman.play_again()


if __name__ == "__main__":
    main()
