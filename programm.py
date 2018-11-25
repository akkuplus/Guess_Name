print ('----------------------------')
print ('       GUESS THE NUMBER     ')
print ('----------------------------')


# generate random number
import random
ran_num = random.randint(0, 100)

# get user number and compare
foundNumber  = False
while not foundNumber:
    # get user input
    user_num = int( input('Guess a number between 0 and 100: ') )
    if user_num == ran_num:
        foundNumber = True
    elif user_num > ran_num:
        print ('Sorry but {} is HIGHER then the number.'.format(user_num) )
    else :
        print('Sorry but {} is LOWER then the number.'.format(user_num))



print ( '''YES! You've got it. The number was {}'''.format(ran_num) )