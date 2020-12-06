#name = input("What is your name?")
#if(n:= len(name)) > 5:
#  print(name, n)

a,b,c, *other, five = 1,2,3,4,5
print(a,b,c, other, five)

list = [1, 2, 3, 4, 5]
newList = list[:] #copy items, no equal prev list

list.reverse() #reverse original
revList = list[::-1] #reverse list and return new list
print(list[0:5:2])

dict1 = {
  'a': 1,
  'B': True,
  'x':[1,2]
}

print(dict1)

tuple1 = (1,2,3,4,5) #immutable list
print('tuple', tuple1)

set1 = {1,2,3,4,5} #uniq list( set1[1] not working, 1 in set1) типа множеств(пересечений, подмножество и т.д.)

#ternary operator

result = 'dsadas' if 1 else 'dsadqweqwrwq'

a = [1, 2]
b = [1, 2]
print('equal list', a is b, a == b) #1 in memory, 2 all items

for i in 'lesson3':
  print(i)

range1 = range(100, 0, -2)

for i in range1:
  print(i)

for i, char in enumerate([1,2,3]):
  print(i, char)


def func(*args, **kwargs):
  '''
  Info
  '''
  print(kwargs)

print(func(1,2,3, name=3, namw=5))
print(func.__doc__)

if((n:= len("dsaddsadsadsaas")) > 10):
  print('n', n)

#scope
def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print(x)
  
  inner()
  print(x)

outer()