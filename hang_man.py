stages = ['''_______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___,
_______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___,
 _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___,
_______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___,
 _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___
 _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___,
 _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___,
 _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  '''
word_list = ["aardvark", "baboon", "camel"]
import random 

#step 1: Randomly choose a word from the word_list and assign to a variable called chosen_word, also print the blanks matching th word
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
lives = 6
print(logo)

for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters= []

while not game_over:
    guessed_letter = input("Guess a letter that you think is in the word:\n")
    guessed_letter = guessed_letter.lower()
    display = ""

    if guessed_letter not in chosen_word:
        lives -= 1
        print(lives)
    
    for letter in chosen_word:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"You have {lives} lives.")
    print(display)

    if lives == 0:
        game_over = True
        print("You lose!")
    
    if "_" not in display:
        print("You win !")
        game_over = True
  #  print(stages[lives])           this is only commented out bc ASCII art was not working correctly