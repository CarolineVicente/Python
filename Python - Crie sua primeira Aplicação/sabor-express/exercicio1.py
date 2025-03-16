
'''numero = int(input('O número é par ou ímpar? '))

if numero % 2 == 0:
    print(f'O  número {numero} é par') 

else:
    print (f'O número {numero} é ímpar')'''

'''usuario = 'Carol'
senha = 1230


valor_usuario = input('Nome de usuario: ')

valor_senha = int(input('Coloque sua senha: '))

if senha == valor_senha and usuario == valor_usuario:
    print('Entrou!')
else:
    print('Senha Incorreta ou Usuario Incorreto! ')'''

'''x= float(input('Digite o valor de x: ')) 
y= float(input('Digite o valor de y: \n')) 

if x > 0 and y > 0:
    print('Esta no primeiro quadrante')
elif x < 0 and y > 0:
    print('Esta no segundo quadrante')
elif x < 0 and y < 0:
    print('Esta no terceiro quadrante')
elif x > 0 and y < 0:
    print('Esta no quarto quadrante')
else:
    print('Esta no ponto de origem')'''

soma_impares = 0

for i in range(1,11,2):
    soma_impares += i
    print(soma_impares)

for i in range(10, 0, -1):
    print(i)

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

    lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")