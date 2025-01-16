import random

vareable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
largo = int(input("de cuantos digitos quieres que sea tu contraseña"))
contraseña = ""

for i in range(largo):
    x=random.choice(vareable)
    contraseña += x
print(contraseña)
