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
        elif count== 2:
            print('This is Git conflict.')
            print('This is a last chance to enter input. ')
            break
        
