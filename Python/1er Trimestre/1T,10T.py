print("Bienvendio a Pipkin lacalabaza ")
producto1=(input('ingresa un producto:'))
numero1=int(input('ingresa precio:'))

producto2=(input('ingresa un producto:'))
numero2=int(input('ingresa precio:'))

producto3=(input('ingresa un producto:'))
numero3=int(input('ingresa precio:'))

producto4=(input('ingresa un producto:'))
numero4=int(input('ingresa precio:'))

producto5=(input('ingresa un producto:'))
numero5=int(input('ingresa precio:'))

resultado1=numero1+numero2+numero3+numero4+numero5
print('el resultado del subtotal es:', resultado1)

resultado2=resultado1*.16
print('el resultado del Iva es:', resultado2)

resultado3=resultado1+resultado2
print('el total a pagar es:', resultado3)

print('producto1 precio:',numero1)
print('producto2 precio:',numero2)
print('producto3 precio:',numero3)
print('prodcuto4 precio:',numero4)
print('producto5 precio:',numero5)
print('total a pagar:',resultado3)
