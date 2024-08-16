#hangman's project 
import hangman;
import random;
words_list=[hangman];
choosen_word=random.choice(words_list)
print(choosen_word);
placeholder="";
word_length=len(choosen_word);
for position in range(word_length):
    placeholder += "_ "
print(placeholder)
lives=6;
correct_letter=[]
game_over=False
while not game_over:
    guess_the_letter=input("guess the letter:").lower();
    display=" "
    for letter in choosen_word:
        if letter==guess_the_letter:
            display+=letter;
            correct_letter.append(guess_the_letter);
        elif letter in correct_letter:
            display +=letter;
        else:
            display+= " _";
    if guess_the_letter not in choosen_word:
        lives=lives-1;
        if lives== 0:
            game_over=True;
            print("game over! you loose");  
    print(display);
    if "_"not in display:
        game_over=True
        print("you win");