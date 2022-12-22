
from CRUD import Products

p1=Products(1,1,'sarah','saaa','asqs','qs','wsq',True,'ws',11,221,21,'sqws','qwsx',True,12,43)

print(p1)

print(type(Products))

print(p1.create())

print(p1.read())

print(p1.update())

print(p1.delete)

print(isinstance(p1,Products))