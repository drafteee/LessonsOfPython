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

