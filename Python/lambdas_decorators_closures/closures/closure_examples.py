# Exam 1 - Data encapsulation
def outer(x):
    def inner(y):
        return x + y

    return inner


inner_func = outer(10)

result_closure = inner_func(15)
print(f'The result is: {result_closure}')


# Exam 2 - Maintaining State
def counter():
    count = 0

    def inner_counter():
        nonlocal count
        count += 1

        return count

    return inner_counter


inner_func = counter()
print(f'Started counter: {inner_func()}')
print(f'Started counter: {inner_func()}')
print(f'Started counter: {inner_func()}')
print(f'Started counter: {inner_func()}')


# Exam 3 - Reusable function template
def create_operation(operation):
    def inner_operation(*args):
        return operation(*args)

    return inner_operation


def add(*args):
    return sum(args)


def subtract(a, b):
    return a - b


def multiply(a, b, c):
    return a * b * c


add_operation_template = create_operation(add)
sub_operation_template = create_operation(subtract)
multiply_operation_template = create_operation(multiply)

result_add_operation = add_operation_template(1, 2, 3)
result_sub_operation = sub_operation_template(1, 2)
result_multiply_operation = multiply_operation_template(1, 2, 3)

print(f'The result of add operation is: {result_add_operation}')
print(f'The result of subtract operation is: {result_sub_operation}')
print(f'The result of multiply operation is: {result_multiply_operation}')


# Example 4 - Data encapsulation / Maintaining State / Reusable function template

def create_bank_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount

        return balance

    def withdraw(amount):
        nonlocal balance
        balance = balance - amount if balance >= amount else 'Insufficient funds'

        return balance

    return deposit, withdraw


deposit, withdraw = create_bank_account(3000)

add_deposit = deposit(1000)
print(f'The current balance is: {add_deposit}')

withdraw_balance = withdraw(2000)
print(f'The current balance is: {withdraw_balance}')

withdraw_balance = withdraw(3000)
print(f'The current balance is: {withdraw_balance}')

deposit2, withdraw2 = create_bank_account(5000)
add_deposit2 = deposit2(5000)
print(f'The current balance is: {add_deposit2}')
