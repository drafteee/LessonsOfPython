import pdb
import re


def add(num1, num2):
    # pdb.set_trace()
    return num1 + num2


add(1, 2)

with open('main.py', mode='r') as my_file:  # r w r+w a
    print(my_file.readline())

pattern = re.compile('this')
string = 'search inside of this this text plesase!'

print(pattern.search(string))
print(pattern.findall(string))
print(pattern.match(string))
