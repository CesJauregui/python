def numero_par(num):
    if num % 2 == 0:
        return True
lista1=[16,17,35,12,25,27,64]
print("-----Función filter sin lambda-----")
print(list(filter(numero_par,lista1)))

#Función filter con lambda
lista2=[16,17,35,12,25,27,64]
print("-----Con función lambda------")
print(list(filter(lambda numero: numero%2==0, lista2)))