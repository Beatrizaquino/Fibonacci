print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)

def fibonacci(posicao):
  if posicao <= 1:
    
    return posicao
    
  else:
    return fibonacci(posicao - 1) + fibonacci(posicao - 2)

a= int(input('Digite a posição ibonacci: '))
res = fibonacci(a)
print('~'*30)
print(f'Na posição {a} o valor é {res}')
print('~'*30)