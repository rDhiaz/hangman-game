import random
from hangman_art import logo , stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
lives = 6
display = []

print(logo)

for n in chosen_word:
    display += "_"
print (' '.join(display))

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    chosen_word_lst = list(chosen_word)

    if guess in display:
        print(f"You already choose {guess}, please guess different letter.")

    for n in range(len(chosen_word_lst)):
        if guess == chosen_word_lst[n]:
            display[n] = guess
    print(' '.join(display))

    if '_' not in display:
        end_of_game = True
        print("You win.")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word.")
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print("You lose.")
    



    


