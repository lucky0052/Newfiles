# Guess the no. if your ans. is correct then you'll be winner.
import random

count = 0
comp = random.randrange(1,10)
while(True):
    user = input('Enter the number :' )
    if user == comp:
        print('You\'re Winner')
        break

    if user != '' :
        if user != comp :
            print('You\'re Loser') 
            choice = input('yes/no : ')
            if choice == 'yes':
                pass
            else:
                break
    else:
        if count < 3 :
            print('You didn\'t give any input. ')
            count += 1
        else:
            print('You didn\'t enter anything many times. ')
            break
        