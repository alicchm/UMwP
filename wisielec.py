import random

def choose_word():
    words = ["python", "komputer", "programowanie", "sztuczna", "inteligencja", "algorytm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Witaj w grze Wisielec!")

    word = choose_word()
    guessed_letters = set()
    attempts = 7

    while attempts > 0:
        print("\nSłowo: ", display_word(word, guessed_letters))
        print("Pozostałe próby: ", attempts)
        print("Zgadnięte litery: ", " ".join(sorted(guessed_letters)))

        guess = input("Podaj literę: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Proszę podaj pojedynczą literę!")
            continue

        if guess in guessed_letters:
            print("Już zgadywałeś tę literę.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Dobrze! Litera znajduje się w słowie.")
        else:
            print("Niestety, ta litera nie znajduje się w słowie.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nGratulacje! Odgadłeś słowo: ", word)
            break
    else:
        print("\nPrzegrałeś! Słowo to: ", word)

if __name__ == "__main__":
    hangman()
