import random
from time import sleep

def main():
    word = get_word()
    rounds = len(word) + 3
    print("The game is about to begin! Ready up!")
    count = 3
    for i in range(3):
        print(count)
        count -= 1
        sleep(1)
    game_start(word,rounds)

def game_start(word, remaining_rounds): 
    print(f"Game start!\n This is a {len(word)} letter word, you have {remaining_rounds} rounds to guess!")
    hidden = ["_" for letter in word]
    print(" ".join(hidden))

    while remaining_rounds != 0: 

        guessed_letter = input("Guess a letter: ").lower() 

        if guessed_letter.isdigit() or len(guessed_letter) > 1:
            print("Type a valid answer you bozo")
            continue

        if guessed_letter in word:
            index = -1 
            for letter in word:
                index += 1
                if letter == guessed_letter:
                    hidden[index] = guessed_letter
            print(f"Correct! Keep going!\n")
            print(" ".join(hidden))
            remaining_rounds -= 1

        else:
            print("Wrong guess! Try again\n")
            remaining_rounds -= 1
            continue

        if "_" not in hidden:
            print("You won!")
            break

        if remaining_rounds <= 4:
            print(f"Here's a hint the word contains an {word[random.randint(0,len(word))]}")
    if remaining_rounds == 0:
        print(f"You lose! The word was {word}!")



def get_word(): 
    words_list = ["Toe", "Rich", "Lizard", "Happy", "Parallelogram", "Velociraptor", "Dog", "Jazz", "British", "Saphire", "Potato","Saxophone"]
    word_list = [word.lower() for word in words_list]
    return random.choice(word_list)

if __name__ == "__main__": 
    main()