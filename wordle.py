import os
import random

os.system('clear')

print('LEODLE\n')

word_list = ['blood','skulk','bonus','chuck', ]
word = random.choice(word_list)


for turn in range(6):
    input_word = input()
    print()
    while not len(input_word) == 5:

        if len(input_word) > 5:
            input_word = input('word too long, try again: ')
            print()
        if len(input_word) < 5:
            input_word = input('word too short, try again: ')
            print()

    for i in range(5):
        
        if input_word[i] == word[i]:
            print('🟩', end='')

        if input_word[i] in word and input_word[i] != word[i]:
            print('🟨', end='')

        if input_word[i] not in word:
            print('⬜️', end='')
    print('\n')

    if input_word == word:
        print('you got it!')
        if turn+1 == 1:
            print('you took 1 try')
            break
        else:
            print('you took', turn+1, 'tries')
            break
    if turn+1 == 6:
        print('you lose')
        print('the word was', word)

    if 5-turn == 1:
        print('1 turn left')
    else:
        print(5-turn,'turns left')
    


