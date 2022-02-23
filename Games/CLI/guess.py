'''A Python Game To guess A Number'''

#Module to get a random integer
from random import randint

#To check if the start and end values are integer
while True :
    try:
        start = int(input('Enter Starting Number: '))
        end = int(input('Enter Ending Number: '))
        break
    except:
        print('Start Or End Must Be an Integer')

#To check if the starting number is smaller than the number by a margin of 25
if start > end-25 :
    print('Start should be smaller than end by 25')
    start = int(input('Enter Starting Number: '))
    end = int(input('Enter Ending Number: '))

# Getting The Random Number
value = randint(start, end)


#First clue
print("I'm thinking of a number between", start, 'and', end)
print('If want you can forfeit by typing /"forfeit/" /n (Only after 10th guess)')

#Starting Conditions
guess = None
guessNum = 0


while True:
    text = input('Guess the number: ')
    guess = int(text)
    guessNum += 1

    if guess < value:
        print('Give A Bigger Number.')
    elif guess > value:
        print('Give A Lower Number.')
    else :
        print('Congratulations! You guessed the right answer:', value)
        print('Number of guesses is:', guessNum)
        break

    if guessNum > 10 and text == 'forfeit':
        print(value)
        print('You forfeited')
        break
  

while True:
    x = 0
    x += 0
    