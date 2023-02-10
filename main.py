opcao = 1
f = 0
while opcao != 5:
  f += 1
  if opcao == 4 or f == 1:
    n1 = float(input('Primeiro Valor: '))
    n2 = float(input('Segundo Valor: '))
  print('''  [ 1 ] Somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números
  [ 5 ] sair do programar''')
  opcao = int(input('>>>>> Qual é a sua opção? '))
  if opcao == 1:
    print('O resultado da soma entre os dois números é {}'.format(n1 + n2))
  if opcao == 2:
    print('O resultado da multiplicação entre os dois números é {}'.format(n1 * n2))
  if opcao == 3:
    if n1 > n2:
      print('O maior valor é {}'.format(n1))
    if n1 < n2:
      print('O maior valor é {}'.format(n2))
    if n1 == n2:
     print('Os valores são iguais!')
  if opcao == 5:
    print('Fim do programa!')
  