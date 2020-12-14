import pdb


def add(num1, num2):
    # pdb.set_trace()
    return num1 + num2


add(1, 2)

with open('main.py', mode='r') as my_file:  # r w r+w a
    print(my_file.readline())
