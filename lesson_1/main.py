# Task 1
import math
import random


# print(math.log2(256) + 1) // banadzevy nayeci

# Task 2

# mek qayl

# Task 3


# Task 4

def get_numbers_list(length=100):
    return [num for num in range(1, length + 1)]


def get_user_answer(title, answer_type='str'):
    data = {
        'str': lambda: input(title).lower(),
        'num': lambda: int(input(title))
    }
    return data[answer_type]()


def is_user_agree(answer):
    acceptableAnswers = ['yes', 'ye', 'y', 'ha', 'ayo', 'da']
    notAcceptableAnswers = ['no', 'net', 'voch', 'nine']
    answers = {
        **dict(zip(acceptableAnswers, [True] * len(acceptableAnswers))),
        **dict(zip(notAcceptableAnswers, [False] * len(notAcceptableAnswers)))
    }

    if answer not in answers:
        raise KeyError(f'Please write answer to equivalent {acceptableAnswers} or {notAcceptableAnswers} .')
    return answers[answer]


def guess_user_number():
    data = get_numbers_list()
    low = 0
    high = len(data) - 1
    print(low + high, 'high')
    while low <= high:
        mid = (low + high) // 2
        current = data[mid]

        if is_user_agree(get_user_answer(f'Is {data[mid]} your number? ')):
            print('You win.')
            if is_user_agree(get_user_answer(f'Do you want to play again ? ')):
                guess_user_number()
                return 'By'
            return 'win'

        if is_user_agree(get_user_answer(f'Is your number bigger than {current} ? ')):
            low = mid + 1
        else:
            high = mid - 1
    print('Do not lie.')

    if is_user_agree(get_user_answer(f'Do you want to play again ? ')):
        guess_user_number()
        return 'By'
    print('You lose.')
    return 'lose'


# guess_user_number()


# Task 5

def guess_computer_number():
    numbers = get_numbers_list()
    target = random.choice(numbers)
    low = 0
    high = len(numbers) - 1

    while low <= high:
        user_guess = None
        try:
            user_guess = get_user_answer(f'Guess the my kept number. Between 1-100. ', 'num')
        except ValueError as e:
            print('Please type integer.')

        if user_guess < numbers[0] or user_guess > numbers[-1]:
            print('Select number between 1-100.')
            continue

        mid = (low + high) // 2
        if user_guess != numbers[mid]:
            print(f'It would have been good to say {numbers[mid]} .')

        if numbers[mid] == target:
            print('You win')
            if is_user_agree(get_user_answer(f'Do you want to play again ? ')):
                guess_computer_number()
                return 'By'
            return 'win'

        if target > numbers[mid]:
            print('My number is higher.')
            low = mid + 1

        if target < numbers[mid]:
            print('My number is lesser.')
            high = mid - 1

    print('You lose!')
    if is_user_agree(get_user_answer(f'Do you want to play again ? ')):
        guess_computer_number()
        return 'By'
    return 'lose'

print(guess_computer_number())

# Research
# 1. Decorator, Կատակ ենք անում :)
# 2. Ackermann function

# Ackermann function@ stanum erku argument voronq petq linen drakan integerner, base ev recursive casery erku hat darcnelu hamara vonc haskaca))
