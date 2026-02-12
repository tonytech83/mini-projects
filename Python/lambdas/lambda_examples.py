import random

# lambda arguments: expression

# Exam 1
lambda_multiply = lambda x, y: x * y

result = lambda_multiply(3, 4)
print(f'The result is {result}')

lst = [random.randint(1, 100) for _ in range(10)]
print(f'The list is: {lst}')


# Exam 2
def even_numbers(lst_numbers):
    even_lst_numbers = []

    for num in lst_numbers:
        if num % 2 == 0:
            even_lst_numbers.append(num)

    return even_lst_numbers


print(f'Even numbers with func: {even_numbers(lst)}')

lambda_even_numbers = filter(lambda num: num % 2 == 0, lst)
print(f'Even numbers with lambda: {list(lambda_even_numbers)}')


def even_numbers2(lst):
    return filter(lambda num: num % 2 == 0, lst)


print(f'Even numbers with func and lambda: {list(even_numbers2(lst))}')


# Exam 3
def increment(lst_nums):
    new_lst = []

    for num in lst_nums:
        num += 1
        new_lst.append(num)

    return new_lst


print(f'Increment with func: {increment(lst)}')

lambda_increment = map(lambda num: num + 1, lst)
print(f'Increment with lambda: {list(lambda_increment)}')

# Exam 4
students = [
    {'name': 'John', 'age': 24},
    {'name': 'Ken', 'age': 33},
    {'name': 'Sarah', 'age': 22},
    {'name': 'Albert', 'age': 54},
]

sorted_students = sorted(students, key=lambda student: student['age'], reverse=True)
print(f'Sorted students by age: {sorted_students}')
