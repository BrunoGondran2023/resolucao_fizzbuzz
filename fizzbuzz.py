def fizz_buzz(n: int) -> list[str]:
    """
    Resolve o desafio FizzBuzz.

    Args:
        n (int): O número até o qual o desafio será resolvido.

    Returns:
        list[str]: Uma lista com os resultados do desafio FizzBuzz.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def main() -> None:
    """
    Função principal para executar o FizzBuzz e exibir os resultados.
    """
    n = 100
    fizz_buzz_results = fizz_buzz(n)
    for res in fizz_buzz_results:
        print(res)


if __name__ == "__main__":
    main()
