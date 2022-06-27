#comentarios son lineas que no se ejecutan y son de uso del programador

#aqui modifique algo
#print('hola')

'''print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')

#contantes tiene inormacion que NO cambia

pie=3.1416

#variables por lo que la informacion que contiene PUEDE cambiar

fecha=7
fecha=8

#######ejemplo de comentar una linea que no quiero usar ahorita#######
#while Trie:
    #fecha=fecha+1


#tipos de Datos

#INT o integers o enteros 

entero=456

#FLOAT o floting o flotantes

flotante=456.5

#string o cadenas

ejemplo1='hola que hace'
ejemplo2='nada tomo clase'
emeplo3="123445344 y letras y sdkindnnekdkdnji{L:L<BGLGHT"

#bool o boolean o boleanos estos evaluan un falso o verdadero

aprobado=True
teprobadotodogrupo=False

#comandos

#print(mensaje):es mandar a la CONSOLA informacion del codigo 

#print para imprimir datos ya guardados en variable/const
print(ejemplo1)
print(aprobado)
print(ejemplo3)
print(fecha)

#print para imprimir algo directamente
print('hola k ace')
print(32345345)

#print combinado

print('el mensaje eviado fue:', ejemplo1)
print(fecha, "de enero")
print('primer mensaje', ejemplo1, "segundo mensaje")

#input() permite que el USUARIO ingrese informacion al CODIGO, el codigo no avanza hasta que detecta un entero del teclado


nombre=input()
print("hola", nombre)

apellido=input('ingrese su apellido')
print("su nombre completo es ", nombre, apellido)

#SOLO INGRESA CADENAS(STRINGS)

num=input('ingrese un numero')
print('el numero 10 veces es',(10*num))

#int()sirve para convertir una STRING en en INT
#float()sirve para comvertir una STRING en un FLOAT
num=int(input('ingrese un numero'))
print('el numero 10 veces es:',(10*num))

#while(): es una estructura que permite repetir un codigo practicamente de forma infinita

#evaluan para falso o verdadero

while True:
    input()
    print("hola")

#comparadores

# == identico 
# >< mayor o menor 
#!= diferente
# >= o <= mayor o igual   menor o igual

  zeta=int(input("numero: "))

  while (zeta>=5):
      print("tu numero es mayor o iguak que 5")

  pasw=input("pasword: ")

  while (pasw!='hola'):
    print("volver a intentar")