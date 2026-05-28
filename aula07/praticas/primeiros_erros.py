try:
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira outro número: '))

    resultado = num1 / num2
    print(resultado)

except (ZeroDivisionError, FileNotFoundError):
    print(f'Ei, tu pode dividir {num1} por zero não. Tas ficando doido, é?')
except ValueError:
    print('Você está tentando converter um valor inválido. Faz isso não!')
except Exception as erro:
    print(f'{type(erro).__name__}')
    print(f'Algo de errado não está certo: {erro}')

print('-- acabou --')