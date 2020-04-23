level1 = 'Easy'
level2 = 'Medium'
level3 = 'Hard'
level = input('Choose_a_level(Easy, Medium or Hard): ')
easy_secret_number = 9
medium_secret_number = 12
hard_secret_number = 30
guess_count = 0
easy_guess_limit = 6
medium_guess_limit = 4
hard_guess_limit = 3
while level1 == level and guess_count < easy_guess_limit:
    guess = int(input('Guess_a_number: '))
    guess_count += 1
    if guess == easy_secret_number:
        print('You got it right!')
        break
    elif guess != easy_secret_number:
        print('That was wrong')
while level2 == level and guess_count < medium_guess_limit:
    guess = int(input('Guess_a_number: '))
    guess_count += 1
    if guess == medium_secret_number:
        print('You got it right!')
        break
    elif guess != medium_secret_number:
        print('That was wrong')
while level3 == level and guess_count < hard_guess_limit:
    guess = int(input('Guess_a_number: '))
    guess_count += 1
    if guess == hard_secret_number:
        print('You got it right!')
        break
else:
    print('Game Over!')

























































