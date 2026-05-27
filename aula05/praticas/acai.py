def pedido_acai(*ingredientes, tamanho='M'):
    print('*'*10)
    for item in ingredientes:
        print(f' - {item}')
    print(f'Tamanho: {tamanho}')
    print('*'*10)

pedido_acai('Granola', tamanho='P')
pedido_acai('Granola', 'Leite em Pó', 'Nutela', tamanho='G')
pedido_acai('Granola', 'Leite em Pó', 'Nutela', 'Jujuba', 'Sucrilhos', 'Banana', tamanho='G')
pedido_acai('aaa', 'bbbb', 'cccc')
