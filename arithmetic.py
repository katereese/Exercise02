def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / float(num2)

def square(num1, num2):
    return num1 ** num2

def cube(num1, num2):
    return num1 ** num2

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calculator(operator, num1, num2):
    if operator == '+':
        print add(num1, num2)

    elif operator == '-':
        print subtract(num1, num2)

    elif operator == '*':
        print multiply(num1, num2)

    elif operator == '/':
        print divide(num1, num2)

    elif operator == '**' and num2 == 2:
        print square(num1, num2)

    elif operator == '**' and num2 == 3:
        print cube(num1, num2)

    elif operator == '**' and num2 != 2 and num2 != 3:
        print power(num1, num2)

    elif operator == '%':
        print mod(num1, num2)

    else:
        print "Sorry, I don't understand."

def process_and_run():
    while True:
        input = raw_input()
        if input == "end":
            break
        else:
            input = input.split(' ')
            operator = input[0]
            num1 = int(input[1])
            num2 = int(input[2])
            calculator(operator, num1, num2)
        

process_and_run()