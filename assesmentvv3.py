import random
from timeit import repeat

'''
Filename: Zayaan Hussein
Author: Zayaan
Date: 28/06/2022
Description: Multi choice quiz
'''

# this is asking the user for his/her name
name_boundry = True

while name_boundry:
    name = input('what is your name?:')
    if not name.isdigit():
        name_boundry = False
    else:
        print('Please enter a valid name')

# this is informing the user of how the game works and what they are playing
instructions = print(
    'Hello {}, this is a multichoice quiz, enjoy playing :)'.format(name))
print('        ')

# just a score counter
score = 0

repeat_cycle = True
while repeat_cycle == True:

    # these are lists of answers for each of the questions. a = answer.
    a1 = ['1. one', '2. four', '3. five', '4. seven']
    a2 = ['1. Wellington', '2. Auckland', '3. Christchurch', '4. Otaki']
    a3 = ['1. Oxygen', '2. Lithium', '3. Potassium', '4. Hydrogen']
    a4 = ['1. China', '2. Fiji', '3. Antarctica', '4. Australia']
    a5 = ['1. India', '2 China', '3. USA', '4. Brazil']
    a6 = ['1. Hong Kong', '2. Japan', '3. Macao', '4. USA']
    a7 = ['1. Soccer', '2. Rugby', '3. Football', '4. Hockey']
    a8 = ['1. Blue', '2. Violet', '3. Green', '4. Turquoise']
    a9 = ['1. Green', '2. Blue', '3. Clear', '4. Black']
    a10 = ['1. Egg', '2. Chicken']

    # what the code is going to say to you if you input the right or wrong answer
    answer_choices_right = ['Nice work!', 'Good job!', 'Amazing!', 'Well Done!',
                            'Fantastic!', 'Bravo!', 'Way to go!', 'Perfect!', 'Good on you!', 'Nice one!', 'Great!']
    answer_choices_wrong = ['Wrong', 'Incorrect', 'False']

    # place holder for the enter user_variable
    user_variable = 'enter either a integer or the word: '

    # the 10 questions for the quiz having used format to add the answers with the questions.
    questions = [
        '''How many stars are in the Chinese flag?:
    {}'''.format(a1),
        '''What is the capital of New Zealand?:
    {}'''.format(a2),
        '''What does the letter O stand for in the periodic table?:
    {}'''.format(a3),
        '''What is the closest country to New Zealand?:
    {}'''.format(a4),
        '''What country has the biggest population?:
    {}'''.format(a5),
        '''What country has the highest life expectancy?:
    {}'''.format(a6),
        '''What is the most popular sport?:
    {}'''.format(a7),
        '''What colour is the sky?:
    {}'''.format(a8),
        '''What colour is water?:
    {}'''.format(a9),
        '''What came first the egg or the chicken?
    {}'''.format(a10)]

    # just lets the code pick one of the questions along with the answers
    random_question = random.choice(questions)
    index = questions.index(random_question)
    user_answer = print(random_question)
    print()
    # these are just asking if the questions answers are right or wrong
    if random_question == questions[0]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'five' or user_ans == '3' or user_ans == '5':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[1]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'wellington' or user_ans == 'Wellington' or user_ans == 'w' or user_ans == '1':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[2]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'oxygen' or user_ans == '1' or user_ans == 'o':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[3]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'australia' or user_ans == '4':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[4]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'china' or user_ans == '2' or user_ans == 'c':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[5]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'hong kong' or user_ans == 'hongkong' or user_ans == 'h' or user_ans == '1':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[6]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'foot ball' or user_ans == 'football' or user_ans == '3':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[7]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'violet' or user_ans == '2' or user_ans == 'v':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[8]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'clear' or user_ans == '3' or user_ans == 'c':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    elif random_question == questions[9]:
        user_ans = input(user_variable).strip().lower()
        if user_ans == 'e' or user_ans == 'egg' or user_ans == '1':
            print(random.choice(answer_choices_right))
            score += 1
            print('your score is now {}'.format(score))
        else:
            print(random.choice(answer_choices_wrong))

    retry = str(input('do you want to play again:')).strip().lower()
    while retry != "yes" and retry != "y" and retry != "n" and retry != "no":
        retry = str(input('yes or no?: ')).strip().lower()
    if retry == 'yes' or retry == 'y':
        repeat_cycle == True
    elif retry == 'no' or retry == 'n':
        print('Bye!')
        repeat_cycle = False
