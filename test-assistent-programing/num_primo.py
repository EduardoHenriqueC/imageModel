from math import isqrt


def is_prime(number: int) -> bool:
    """Verifica se um número inteiro é primo.

    Args:
        number (int): O número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    # Números menores ou iguais a 1 não são considerados primos.
    if number <= 1:
        return False
    # 2 é o menor primo e também o único primo par.
    if number == 2:
        return True
    # Elimina todos os números pares maiores que 2 antes de testar divisores ímpares.
    if number % 2 == 0:
        return False

    # Só precisamos verificar divisores até a raiz quadrada do número.
    max_divisor = isqrt(number)
    # Testa apenas candidatos ímpares, porque os pares já foram descartados.
    for divisor in range(3, max_divisor + 1, 2):
        if number % divisor == 0:
            return False

    return True


def run_tests() -> None:
    try:
        number = int(input("Digite um número inteiro: "))
        result = is_prime(number)
        if result:
            print(f"O número {number} é primo!")
        else:
            print(f"O número {number} não é primo.")
    except ValueError:
        # Trata entradas não numéricas para evitar falha no programa.
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    run_tests()