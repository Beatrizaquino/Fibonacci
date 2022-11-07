print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)

n = int(input('Digite '))
cont = 3
t1 = 1
t2 = 2
print(f'{t1} -> {t2}', end =' ')
while cont <=n:
  t3 = t1 + t2
  print('~'*30)
  print(f'->{t3}', end =' ')
  print('~'*30)
  t1 = t2
  t2 = t3
  cont+=1