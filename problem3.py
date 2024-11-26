import random

words = ["engineer","doctor","cinema","alahly"]

selected_word = random.choice(words)

shuffled_word = list(selected_word)

random.shuffle(shuffled_word)

shuffled_word = ''.join(shuffled_word)

print(f"shuffled word is :  {shuffled_word}")

attempts = 4

for attempt in range(attempts, -1, -1):
    guess = input("enter your guess")
    if guess == selected_word:
        print("congratulations! you guessed the correct word")
        exit()
    else:
        print(f"wrong! try again.  you have {attempt}attempt left")

print(f"  you are out of attempts! the correct word was : {selected_word}")