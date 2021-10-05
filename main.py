import random

word_list = ("aardvark,baboon,camel").split(",")
chosen_word = random.choice(word_list)
lives = 6
display = []

for n in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    lives = 0
    guess = (input("Choose a letter: ")).lower()
    lst_chosenWord = list(chosen_word)
    for n in range(len(chosen_word)):
        
        if guess == lst_chosenWord[n]:
            display[n] = guess
        elif "_" not in display:
            end_of_game = True
        elif guess not in lst_chosenWord[n]:
            lives += 1
       
        
    print (display)
    print (lives)



