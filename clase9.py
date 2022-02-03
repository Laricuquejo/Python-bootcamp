from audioop import add


def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")

say_hello()

def say_hello(name= 'Deafault'): # 44, 4:10
    print(f'Hello {name}')

say_hello('Lari')
say_hello()

def add_num(num1, num2):
    return num1+num2
result = add_num(10, 10)
print(result)

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_list([1, 3, 5]))
print(check_even_list([2, 4, 5]))
