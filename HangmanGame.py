import random

# Predefined word list
word_list = ["python", "code", "alpha", "script", "debug"]
secret_word = random.choice(word_list)

# Game setup
guessed_word = ["_"] * len(secret_word)
attempts_left = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word: ", " ".join(guessed_word))

while attempts_left > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct! Word now: ", " ".join(guessed_word))
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess. Attempts left: {attempts_left}")
        print("Word: ", " ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print(f"🎉 You won! The word was '{secret_word}'.")
else:
    print(f"💀 Game over! The word was '{secret_word}'.")
