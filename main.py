
from CRUD import Products

p1=Products(1,1,'sarah','saaa','asqs','qs','wsq',True,'ws',11,221,21,'sqws','qwsx',True,12,43)

print(p1)

print(p1.create())

print(p1.read())

print(p1.update())

print(p1.delete())


# class type
print(type(Products)) # <class 'type'>

# isinstance
print(isinstance(p1,Products)) # True