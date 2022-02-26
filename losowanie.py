import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

word = random.choice(WORDS)
correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Zgadnij, jakie to słowo:", jumble)
guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    if guess == correct:
        print("Zgadza się! Zgadłeś!\n")
