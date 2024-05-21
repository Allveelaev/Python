from random import choice
from hangman_words import word_list
from hangman_stages import stages,logo
print(logo)
lives = 6
chosen_word = choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for i in chosen_word:
    display.append("_")
word_length = len(chosen_word)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed this letter: {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print("Wrong guess!")
        lives -= 1
    print(stages[lives])
    if lives == 0:
        print("You lose!")
        end_of_game = True

    print(f"You have {lives} lives")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")


