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
        'num': lambda: input(title)
    }
    return data[answer_type]()


def is_user_agree(answer):
    get_joke(answer)
    return answer == 'yes' or answer == 'ye' or answer == 'y' or answer == 'ha' or answer == 'ayo' or answer == 'da'


def get_joke(answer):
    data = {
        'yes': 'cerin tqes',
        'da': 'lambda',
        'ayo': 'vazmi mayo',
        'ha': ['hanem xaxa', 'hanem hamp ara', 'hanem lva']
    }

    joke = data.get(answer)
    if joke:
        if (answer == 'ha'):
            print(random.choice(joke))
        else:
            print(joke)


def guess_user_number():
    data = get_numbers_list()
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        current = data[mid]

        if is_user_agree(get_user_answer(f'Is {data[mid]} your number? ')):
            return 'ok'

        if is_user_agree(get_user_answer(f'Is your number bigger than {current} ? ')):
            low = mid + 1
        else:
            high = mid - 1


# guess_user_number()


# Task 5

def guess_computer_number(data_length=100):
    numbers = get_numbers_list()
    target = random.choice(numbers)

    low = 0
    high = len(numbers) - 1

    while low < high:
        optimal_mid = (low + high) // 2
        user_guess = get_user_answer(f'Tiv asa ara!! cankalia {numbers[optimal_mid]} ', 'num')

        try:
            mid = numbers.index(int(user_guess))
            if numbers[mid] != numbers[optimal_mid]:
                mid = numbers[optimal_mid]
                print(f'Es angam ognum em!! {numbers[mid]} es petqa aseyr.')

        except ValueError:
            print('Jur es canum.')

        print(numbers[mid], target)
        if numbers[mid] == target:
            return 'maladec'

        if target > numbers[mid]:
            low = mid + 1

        if target < numbers[mid]:
            high = mid - 1



print(guess_computer_number())


# Research
# 1. Decorator, Կատակ ենք անում :)
# 2. Ackermann function

# Ackermann function@ stanum erku argument voronq petq linen drakan integerner, base ev recursive casery erku hat darcnelu hamara vonc haskaca))