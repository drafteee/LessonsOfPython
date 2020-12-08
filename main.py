

#name = input("What is your name?")
#if(n:= len(name)) > 5:
#  print(name, n)

a,b,c, *other, five = 1,2,3,4,5
print(a,b,c, other, five)

list0 = [1, 2, 3, 4, 5]
newList = list0[:] #copy items, no equal prev list

list0.reverse() #reverse original
revList = list0[::-1] #reverse list and return new list
print(list0[0:5:2])

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




class Test:
  def __init__(self, name):
    self.__name = name

  def run(self):
    print('run', self.name)

  @classmethod
  def add(cls, num1, num2):
    return cls(f'{num1 + num2}')

  def __call__(self):
    return('dsadsadas?????')

test1 = Test('dsadsa')
test2 = Test('11111')
test3 = Test.add(1,2)
print(dir(test1))
print(test1())

#print(test1.__name, test2.__name, test3.__name)


list1 = [1,2,3]
list2 = [10,11,12]
print(zip(list1,list2))
print(list(map(lambda item: item*2, list1)))

a = [(0,2), (4,3), (10, -1), (9,9)]
a.sort(key= lambda x:x[1])
print(a) 

list4 = [char for char in 'hello']
list5 = [num*2 for num in range(100) if num %2==0]
print(list5)

simpleDict ={
  'a': 1,
  'b': 2
}

nextDict = {key: value**2 for key, value in simpleDict.items()}

print(nextDict)

myDict = {num: num*2 for num in [1,2,3]}
print(myDict)

duplicates = set([x for x in 'hello' if 'hello'.count(x) > 1])

print(duplicates)



def decorator(func):
  def wrapFunc():
    print('dsadsa')
    func()
    print('dsadsads')
  return wrapFunc

@decorator
def bye():
  print('hello')

bye()


try:
  age=int(input('Input value'))
  print(age)
  raise Exception('throw user exception')
except (ValueError, TypeError, ZeroDivisionError) as err:
  print(err)
else:
  print('thank you')
finally:
  print('end')
   