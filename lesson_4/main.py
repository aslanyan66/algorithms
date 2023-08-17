# Task 1

# On qarakusi

# Task 2

# depi achman karg 1 popoxutyamb kani

# Task 3

# function bubble_sort(numbers):
#     for i in range(0, len(numbers)):
#         for j in range(0, len(numbers) - 1 - i):
#             current = numbers[j]
#
#             if current < numbers[j + 1]:
#                 continue
#
#             if current > numbers[j + 1]:
#                 numbers[j] = numbers[j + 1]
#                 numbers[j + 1] = current
#
#     return numbers


# Task 4

def bubble_sort(numbers, isDecreaseOrder=False):
    index_helper = -1 if isDecreaseOrder else 1
    for i in range(int(isDecreaseOrder), len(numbers)):
        for j in range(int(isDecreaseOrder), len(numbers) - 1 - i):
            current = numbers[j]

            if current < numbers[j + index_helper]:
                continue

            if current > numbers[j + index_helper]:
                numbers[j] = numbers[j + index_helper]
                numbers[j + index_helper] = current

    return numbers


print(bubble_sort([10, 23, 2, 3, 4, 5, 3, 1, 3, 13, 41, 5, 35, 65, 37, 537, 385, 3, 35], False))

# Research
# 1.	Ինչ algorithm է օգտագործում python-ի list-ի sort() method-ը:

# Timsort-a ogtagorcum vornel ira mech insertion u merge sorta use anum, lav complex algorithma vonc hasakaca, bbavakanin mec lister kara sortavori shat arag,
# vonc haskaca