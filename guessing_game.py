from random import randint
# generate a number 1-5
answer = randint(1,5)
# input from user
#check input is a mumber from 1-5
while True:
    try:
        guess = int(input('Guess a number 1~5 :- ').strip())
        if 0 < guess < 5:
            if guess == answer:
                print('you are a genius')
                break
        else:
            print('Please enter a number between 1~5')
            continue
    except ValueError:
        print('Please enter a number')
        continue
    
# check a numner is right

#ask again
