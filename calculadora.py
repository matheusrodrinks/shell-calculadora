while True: 

  num1 = int(input("Digite o primeiro número: "))

  num2 = int(input("Digite o segundo número: "))

  print("\nEscolha a operação:")

  print('1; adição')

  print('2; subtração')

  print('3; multiplicação')

  print('4; divisão') 

  escolha = int(input("Digite o número equivalente ao da operação:"))

  if escolha == 1:

    res = num1 + num2

    print(res)

  elif escolha == 2:

    res = num1 - num2

    print(res)

  elif escolha == 3:

    res = num1 * num2

    print(res)

  elif escolha == 4:

    res = num1 / num2

    print(res)